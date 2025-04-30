from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import bcrypt
import json
import pandas as pd
import os
import plotly
import plotly.express as px
import plotly.graph_objs as go
from collections import Counter
from collections import defaultdict
import uuid

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load users from users.json or initialize if file not found
try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

# Dictionary for password reset tokens
reset_tokens = {}

# Helper function to save users
def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

# Helper function to load job data
def load_data():
    file_path = os.path.join('uploads', 'mrpdata.csv')
    return pd.read_csv(file_path, encoding='ISO-8859-1')

# Overview route
@app.route('/overview')
def overview():
    if 'user' not in session:
        return redirect(url_for('login'))

    df = load_data()

    # Remove rows missing critical fields
    df = df.dropna(subset=['company_name', 'job_title', 'job_skills', 'salary_offered'])

    # ---- Top 20 Companies by Job Count ----
    top_companies = df['company_name'].value_counts().nlargest(20)
    company_fig = px.bar(
        x=top_companies.index,
        y=top_companies.values,
        labels={'x': 'Company', 'y': 'Job Count'},
        title='Top 20 Companies by Job Count',
        height=500
    )

    # ---- Top 20 Job Titles by Frequency ----
    top_job_titles = df['job_title'].value_counts().nlargest(20)
    job_fig = px.area(
        x=top_job_titles.index,
        y=top_job_titles.values,
        labels={'x': 'Job Title', 'y': 'Frequency'},
        title='Top 20 Job Titles by Frequency',
        height=500
    )

    # ---- Top 20 Skills in Demand ----
    skills_series = df['job_skills'].dropna().apply(
        lambda x: [skill.strip().lower() for skill in str(x).split(',') if len(skill.strip()) < 40]
    )
    all_skills = [skill for skills_list in skills_series for skill in skills_list]
    skill_counts = Counter(all_skills).most_common(20)
    skills, counts = zip(*skill_counts)

    skill_fig = px.pie(
        names=skills,
        values=counts,
        title='Top 20 Skills in Job Listings'
    )
    skill_fig.update_traces(textinfo='label', hoverinfo='none')

    # ---- Salary Mapping for Job Titles (for Modal Popup) ----
    salary_mapping = {}
    for _, row in df[['job_title', 'salary_offered']].dropna().iterrows():
        title = str(row['job_title'])
        salary = float(row['salary_offered']) if pd.notna(row['salary_offered']) else 0
        if title not in salary_mapping:
            salary_mapping[title] = salary

    # ---- Top 20 Job Titles by Highest Salary (Improved) ----
    top_salaries = df.groupby("job_title")["salary_offered"].max().sort_values(ascending=False).head(20)

    salary_bar = go.Bar(
        x=top_salaries.values.tolist(),
        y=top_salaries.index.tolist(),
        orientation='h',
        marker=dict(
            color='rgba(63, 81, 181, 0.7)',
            line=dict(color='rgba(63, 81, 181, 1.0)', width=1.5)
        ),
        text=[f"${int(val):,}" for val in top_salaries.values.tolist()],
        textposition='auto'
    )

    salary_layout = go.Layout(
        title="Top 20 Highest Paying Job Titles",
        xaxis=dict(title='Salary', tickprefix="$", gridcolor='lightgrey'),
        yaxis=dict(title='Job Title', automargin=True),
        height=700,
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9'
    )

    salary_fig = {
        "data": [salary_bar],
        "layout": salary_layout
    }

    return render_template(
        'overview.html',
        user=session['user'],
        company_chart=json.dumps(company_fig, cls=plotly.utils.PlotlyJSONEncoder),
        job_title_chart=json.dumps(job_fig, cls=plotly.utils.PlotlyJSONEncoder),
        skills_chart=json.dumps(skill_fig, cls=plotly.utils.PlotlyJSONEncoder),
        salary_data=json.dumps(salary_mapping),
        highest_salary_chart=json.dumps(salary_fig, cls=plotly.utils.PlotlyJSONEncoder)
    )


# Note: your other routes like login, dashboard, signup etc. will follow here...



@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    df = load_data()
    jobtitles = sorted(df['job_title'].dropna().unique())
    return render_template('dashboard.html', user=session['user'], jobtitles=jobtitles)

@app.route('/analysis')
def analysis():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    df = load_data()
    
    # Get unique company names
    companies = sorted(df['company_name'].dropna().unique())

    # Structure: job_data[company][post_date] = list of {title, salary}
    job_data = defaultdict(lambda: defaultdict(list))

    for _, row in df.iterrows():
        company = row.get("company_name")
        post_date = str(row.get("post_date"))
        title = row.get("job_title")
        salary = row.get("salary_offered")

        if pd.notna(company) and pd.notna(post_date) and pd.notna(title) and pd.notna(salary):
            job_data[company][post_date].append({
                "title": title,
                "salary": salary
            })

    return render_template(
        'analysis.html',
        user=session['user'],
        companies=companies,
        job_data=json.dumps(job_data)
    )

@app.route('/location')
def location_view():
    if 'user' not in session:
        return redirect(url_for('login'))

    df = load_data()
    df['location'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')
    locations = sorted(df['location'].dropna().unique())
    companies = sorted(df['company_name'].dropna().unique())
    return render_template('location.html', user=session['user'], locations=locations, companies=companies)

@app.route('/get_jobs_by_location', methods=['POST'])
def get_jobs_by_location():
    df = load_data()
    data = request.json
    location = data.get("location")

    # Combine city, state, country into one location string
    df['location_combined'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')

    # Filter by selected location
    filtered = df[df['location_combined'] == location]

    # Get unique job titles at that location
    job_list = sorted(filtered['job_title'].dropna().unique().tolist())
    return jsonify({"jobs": job_list})



@app.route('/get_jobs_by_company', methods=['POST'])
def get_jobs_by_company():
    df = load_data()
    data = request.json
    company = data.get("company")

    # Filter by selected company
    filtered = df[df["company_name"] == company]

    # Get unique job titles for the company
    job_list = sorted(filtered['job_title'].dropna().unique().tolist())
    return jsonify({"jobs": job_list})




@app.route('/get_companies_by_jobtitle', methods=['POST'])
def get_companies_by_jobtitle():
    df = load_data()
    data = request.json
    jobtitle = data.get("jobtitle")

    if not jobtitle:
        return jsonify({"error": "Job title is required."})

    filtered = df[df['job_title'] == jobtitle]
    if filtered.empty:
        return jsonify({"error": "No data found for this job title."})

    company_counts = filtered['company_name'].value_counts().nlargest(20)

    fig = px.pie(
        names=company_counts.index,
        values=company_counts.values,
        title=f"Top Companies Offering '{jobtitle}' Roles"
    )
    fig.update_traces(textinfo='label', hoverinfo='none')

    return jsonify({"graph": fig.to_json()})


@app.route('/get_skills_by_jobtitle', methods=['POST'])
def get_skills_by_jobtitle():
    df = load_data()
    data = request.json
    jobtitle = data.get("jobtitle")

    if not jobtitle:
        return jsonify({"error": "Job title is required."})

    filtered = df[df["job_title"] == jobtitle]
    if filtered.empty:
        return jsonify({"error": "No data found for this job title."})

    skill_series = filtered['job_skills'].dropna().apply(lambda x: [s.strip().lower() for s in str(x).split(',')[:3]])
    all_skills = [s for sublist in skill_series for s in sublist]
    skill_counts = Counter(all_skills).most_common(10)
    skills, counts = zip(*skill_counts)

    fig = px.pie(
        names=skills,
        values=counts,
        title=f"Top Skills Required for {jobtitle}"
    )

    return jsonify({"graph": fig.to_json()})


@app.route('/get_stacked_skills_by_title', methods=['POST'])
def get_stacked_skills_by_title():
    df = load_data()
    data = request.json
    jobtitle = data.get("jobtitle")

    if not jobtitle:
        return jsonify({"error": "Job title is required."})

    filtered = df[df["job_title"] == jobtitle]
    if filtered.empty:
        return jsonify({"error": "No jobs found for this title."})

    skills_by_loc = defaultdict(Counter)

    for _, row in filtered.iterrows():
        location = ", ".join(filter(None, [row.get("city", ""), row.get("state", ""), row.get("country", "")]))
        skills = [s.strip().lower() for s in str(row.get("job_skills", "")).split(',') if s.strip()]
        for skill in skills:
            skills_by_loc[skill][location] += 1

    locations = sorted({loc for skill in skills_by_loc for loc in skills_by_loc[skill]})
    top_skills = sorted(skills_by_loc.keys())

    traces = []
    for skill in top_skills:
        y_vals = []
        text_vals = []
        for loc in locations:
            count = skills_by_loc[skill][loc]
            y_vals.append(count)
            text_vals.append(f"Skill: {skill}<br>Location: {loc}<br>Count: {count}")

        traces.append({
            'name': skill,
            'x': locations,
            'y': y_vals,
            'type': 'bar',
            'hoverinfo': 'text',
            'text': text_vals
        })

    layout = {
        'barmode': 'stack',
        'title': f"Top Skills by Location for {jobtitle}",
        'xaxis': {'title': 'Location'},
        'yaxis': {'title': 'Skill Count'},
        'height': 600,
        'width': 1000
    }

    return jsonify({"graph": json.dumps({'data': traces, 'layout': layout})})

@app.route('/get_locations_by_jobtitle', methods=['POST'])
def get_locations_by_jobtitle():
    df = load_data()
    data = request.json
    jobtitle = data.get("jobtitle")

    if not jobtitle:
        return jsonify({"error": "Job title is required."})

    filtered = df[df['job_title'] == jobtitle]

    if filtered.empty:
        return jsonify({"error": "No data found for this job title."})

    # Combine city, state, and country into one location string
    filtered['Location'] = filtered[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')

    location_counts = filtered['Location'].value_counts().nlargest(20)  # Top 20 locations

    fig = px.pie(
        names=location_counts.index,
        values=location_counts.values,
        title=f"Skills by Location for {jobtitle}"
    )

    # 👇 Show only label on the chart, remove hover and percent
    fig.update_traces(textinfo='label', hoverinfo='none')

    return jsonify({"graph": fig.to_json()})

@app.route('/get_post_dates', methods=['POST'])
def get_post_dates():
    df = load_data()
    data = request.json
    company = data.get("company")

    if not company:
        return jsonify({"dates": []})

    dates = df[df["company_name"] == company]["post_date"].dropna().unique().tolist()
    return jsonify({"dates": sorted(dates)})

@app.route('/get_jobs_by_company_date', methods=['POST'])
def get_jobs_by_company_date():
    df = load_data()
    data = request.json
    company = data.get("company")
    postdate = data.get("postdate")

    if not company or not postdate:
        return jsonify({"jobs": []})

    filtered = df[(df["company_name"] == company) & (df["post_date"] == postdate)]
    jobs = [{"title": row["job_title"], "salary": row["salary_offered"]} for _, row in filtered.iterrows()]
    return jsonify({"jobs": jobs})

@app.route('/get_job_details_by_location', methods=['POST'])
def get_job_details_by_location():
    df = load_data()
    data = request.json
    location = data.get("location")
    jobtitle = data.get("jobtitle")

    if not location or not jobtitle:
        return jsonify({"error": "Location and job title are required."})

    # Combine city, state, and country into a single column
    df['location_combined'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')
    filtered = df[(df['location_combined'] == location) & (df['job_title'] == jobtitle)]

    if filtered.empty:
        return jsonify({"error": "No data found for the selected job at this location."})

    # Use first match
    first = filtered.iloc[0]
    skills_raw = first.get('job_skills', '')
    skills_list = [s.strip().lower() for s in str(skills_raw).split(',') if s.strip()][:3]  # top 3 skills

    company = first.get('company_name', 'N/A')
    values = [1] * len(skills_list)  # equal distribution for skill labels

    # Add job type, salary, and company to pie slices
    skills_list.extend(['Job Type', 'Salary', 'Company'])
    values.extend([
        1,
        float(first['salary_offered']) if pd.notna(first['salary_offered']) else 0,
        1
    ])

    fig = px.pie(
        names=skills_list,
        values=values,
        title=f"Job Details for '{jobtitle}' in '{location}'"
    )
    fig.update_traces(textinfo='label', hoverinfo='none')

    return jsonify({"graph": fig.to_json()})



@app.route('/get_job_details_by_company', methods=['POST'])
def get_job_details_by_company():
    df = load_data()
    data = request.json
    company = data.get("company")
    jobtitle = data.get("jobtitle")

    if not company or not jobtitle:
        return jsonify({"error": "Company and job title are required."})

    filtered = df[(df["company_name"] == company) & (df["job_title"] == jobtitle)]

    if filtered.empty:
        return jsonify({"error": "No data found for the selected job at this company."})

    # Use first matching row
    first = filtered.iloc[0]
    skills_raw = first.get('job_skills', '')
    skills_list = [s.strip().lower() for s in str(skills_raw).split(',') if s.strip()][:3]  # limit to 3 skills

    location = ", ".join([str(first.get(c, "")) for c in ['city', 'state', 'country']]).strip(', ')
    values = [1] * len(skills_list)  # dummy values just to show labels equally

    # Add job type, salary, and location
    skills_list.extend(['Job Type', 'Salary', 'Location'])
    values.extend([
        1,
        float(first['salary_offered']) if pd.notna(first['salary_offered']) else 0,
        1
    ])

    fig = px.pie(
        names=skills_list,
        values=values,
        title=f"Job Details for '{jobtitle}' at '{company}'"
    )
    fig.update_traces(textinfo='label', hoverinfo='none')

    return jsonify({"graph": fig.to_json()})


@app.route('/get_companies_by_location', methods=['POST'])
def get_companies_by_location():
    df = load_data()
    data = request.json
    location = data.get("location")

    df['location_combined'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')
    filtered = df[df['location_combined'] == location]
    companies = sorted(filtered['company_name'].dropna().unique().tolist())
    return jsonify({"companies": companies})

@app.route('/get_jobs_by_location_and_company', methods=['POST'])
def get_jobs_by_location_and_company():
    df = load_data()
    data = request.json
    location = data.get("location")
    company = data.get("company")

    df['location_combined'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')
    filtered = df[(df['location_combined'] == location) & (df['company_name'] == company)]

    job_list = sorted(filtered['job_title'].dropna().unique().tolist())
    return jsonify({"jobs": job_list})

@app.route('/get_job_details_by_location_and_company', methods=['POST'])
def get_job_details_by_location_and_company():
    df = load_data()
    data = request.json
    location = data.get("location")
    company = data.get("company")
    jobtitle = data.get("jobtitle")

    df['location_combined'] = df[['city', 'state', 'country']].fillna('').agg(', '.join, axis=1).str.strip(', ')
    filtered = df[
        (df['location_combined'] == location) &
        (df['company_name'] == company) &
        (df['job_title'] == jobtitle)
    ]

    if filtered.empty:
        return jsonify({"error": "No data found for the selected filters."})

    job = filtered.iloc[0]
    skills = [s.strip() for s in str(job['job_skills']).split(',') if s.strip()]
    job_type = job.get('job_type', 'Unknown')
    salary = job.get('salary_offered', 'Not Available')

    fig = px.pie(
        names=skills,
        values=[1] * len(skills),
        title=f"{jobtitle} | Job_Type: {job_type} | Salary: {salary}"
    )
    fig.update_traces(textinfo='label', hoverinfo='none')

    return jsonify({"graph": fig.to_json()})





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['username']
        password = request.form['password'].encode('utf-8')

        user = next((u for u, d in users.items() if u == identifier or d.get("email") == identifier), None)
        if user and bcrypt.checkpw(password, users[user]["password"].encode('utf-8')):
            session['user'] = user
            return redirect(url_for('dashboard'))
        flash("Invalid username/email or password", "error")

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            flash("Username already exists", "error")
        elif any(u.get("email") == email for u in users.values()):
            flash("Email already registered", "error")
        elif password != confirm_password:
            flash("Passwords do not match", "error")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users[username] = {
                "email": email,
                "password": hashed_password
            }
            save_users()
            flash("Account created! Please log in.", "success")
            return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = next((u for u, d in users.items() if d.get("email") == email), None)

        if user:
            token = str(uuid.uuid4())
            reset_tokens[token] = user
            reset_url = url_for('reset_password', token=token, _external=True)
            flash(f"<a href='{reset_url}'>Click here to reset your password</a>", "info")
        else:
            flash("Email not found", "error")

    return render_template('forgot_password.html')

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if token not in reset_tokens:
        flash("Invalid or expired reset link", "error")
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash("Passwords do not match", "error")
        else:
            user = reset_tokens.pop(token)
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users[user]['password'] = hashed_password
            save_users()
            flash("Password reset successful! Please login.", "success")
            return redirect(url_for('login'))

    return render_template('reset_password.html', token=token)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)