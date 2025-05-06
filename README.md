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
  * ![image](https://github.com/user-attachments/assets/73d84375-83ad-4798-b575-830ddcdcb0d6)
  * **Dashboard**: Filter job title to view skills, companies, and locations
  * ![image](https://github.com/user-attachments/assets/70669544-5606-4df4-bee9-6c2e68c62add)
  * **Analysis**: Date-wise company jobs and salaries
  * ![image](https://github.com/user-attachments/assets/2baf3063-ddd7-4c05-9641-bf7073eed10f)
  * **Location**: City-based job title insights with pie charts
  * ![image](https://github.com/user-attachments/assets/e5fa8f23-e393-4e8e-831f-5d5b2b7b31d0)


## ✨ Features

* Flask-based web application
* Data analysis using Pandas
* Interactive charts with Plotly
* CSV dataset integration
* Dashboard with filters and visual drilldowns

## 📊 Dashboard
### Dashboard Preview

```markdown
[![Dashboard Screenshot](![image](https://github.com/user-attachments/assets/821a8e56-edd6-49ae-a05e-75a044cbf52b)
)
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
