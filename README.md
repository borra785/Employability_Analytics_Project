# Employability Analytics Application

*A web-based dashboard to analyze job market trends for software developers.*

## 📋 Project Description

This project is a web-based employability analytics application designed to help software developers and career analysts understand the evolving job market. It analyzes job postings to extract insights on top companies, in-demand skills, preferred job locations, salary trends, and job types.

The application empowers users to explore job market dynamics through interactive charts and dashboards, making it easier to identify hiring patterns, skill gaps, and employment opportunities in the software development field.

## 📂 Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Dashboard](#dashboard)

  * [Live Dashboard](#61-live-dashboard)
  * [Embed via GitHub Pages](#62-embed-in-github-pages-static-website)
  * [Dashboard Preview](#63-dashboard-preview)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## ⚙️ Installation / Setup (Windows)

Follow the steps below to set up and run the project on a Windows machine using Visual Studio:

1. **Install Required Tools**

   * [Visual Studio](https://visualstudio.microsoft.com/)
   * [Python](https://www.python.org/downloads/windows/) (3.8 or higher)
   * ✅ Ensure "Add Python to PATH" is selected during installation.

2. **Clone the Repository**

```bash
git clone https://github.com/yourusername/EmployabilityAnalyticsApp.git
cd EmployabilityAnalyticsApp
```

3. **Set Up a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate
```

4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

*If not available, manually install:* `flask pandas plotly`

5. **Open in Visual Studio**

   * Open the `Flask_Project` folder
   * Adjust code formatting via `Tools > Options > Text Editor > Python`
   * Select the correct Python environment

6. **Run the Flask App**

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

7. **Upload to GitHub (Optional)**

```bash
git init
git remote add origin https://github.com/yourusername/EmployabilityAnalyticsApp.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 🚀 Usage

Start the Flask server:

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Key Features:

* Sign up/login to access insights
* Navigate through:

  * **Overview**: Top 20 companies, skills, job titles
  * **Dashboard**: Filter job title to view skills, companies, and locations
  * **Analysis**: Date-wise company jobs and salaries
  * **Location**: City-based job title insights with pie charts

## ✨ Features

* Flask-based web application
* Data analysis using Pandas
* Interactive charts with Plotly
* CSV dataset integration
* Dashboard with filters and visual drilldowns
* Power BI visualization integration

## 📊 Dashboard

### 6.1 Live Dashboard

Check out the interactive Power BI dashboard here:
👉 [View Dashboard](https://app.powerbi.com/view?r=eyJrIjoiEXAMPLE123...)

> 🔐 Note: "Publish to Web" makes the dashboard publicly visible.

### 6.2 Embed via GitHub Pages

Create a `dashboard.html` file:

```html
<!DOCTYPE html>
<html>
<head><title>Power BI Dashboard</title></head>
<body>
  <h1>Interactive Power BI Dashboard</h1>
  <iframe width="1000" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiEXAMPLE123..." frameborder="0" allowFullScreen="true"></iframe>
</body>
</html>
```

Enable GitHub Pages under Settings → Pages and access:
`https://yourusername.github.io/your-repo/dashboard.html`

### 6.3 Dashboard Preview

```markdown
[![Dashboard Screenshot](images/dashboard-preview.png)](https://app.powerbi.com/view?r=eyJrIjoiEXAMPLE123...)
```

## 📁 Project Structure

```bash
Flask_Project/
├── app.py
├── users.json
├── static/
│   ├── script.js
│   └── styles.css
├── templates/
│   ├── analysis.html
│   ├── dashboard.html
│   ├── forgot_password.html
│   ├── location.html
│   ├── login.html
│   ├── overview.html
│   ├── reset_password.html
│   └── signup.html
├── uploads/
│   └── data.csv
├── requirements.txt
└── README.md
```

## 👥 Contributing

Pull requests are welcome! To contribute:

1. Fork the repo
2. Create a branch (`git checkout -b feature-name`)
3. Commit your changes
4. Push to your fork and submit a PR

For more guidelines, refer to [CONTRIBUTING.md](CONTRIBUTING.md) (if available).

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgements

* [Flask](https://flask.palletsprojects.com/)
* [Plotly](https://plotly.com/python/)
* [Power BI](https://powerbi.microsoft.com/)
* [Python](https://www.python.org/)
* [Visual Studio](https://visualstudio.microsoft.com/)
* [Kaggle Job Listings Dataset](https://www.kaggle.com/datasets/jobspikr/software-developer-job-listings-usa)
* Open-source community for resources and documentation
