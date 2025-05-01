# Employability_Analytics_Project
For job seekers and Career Advisors

## 📝 Project Description  
This project is a web-based employability analytics application designed to help software developers and career analysts understand the evolving job market. It analyzes job postings to extract insights on top companies, in-demand skills, preferred job locations, salary trends, and job types.

The application empowers users to explore job market dynamics through interactive charts and dashboards, making it easier to identify hiring patterns, skill gaps, and employment opportunities in the software development field.

## 📚 Table of Contents  
- [Project Description](#-project-description)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Features](#-features)  
- [📊 Dashboard](#-dashboard)  
  - [Live Dashboard](#61-live-dashboard)  
  - [Embed via GitHub Pages](#62-embed-in-github-pages-static-website)  
  - [Dashboard Preview](#63-embed-a-screenshot--link-in-readme)  
- [📁 Project Structure](#-project-structure)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)  
- [🙏 Acknowledgements](#-acknowledgements)

## ⚙️ Installation / Setup (Windows)

Follow the steps below to set up and run the project on a Windows machine using Visual Studio:

### 1. Install Required Tools

- **Visual Studio** (Community Edition or higher)  
  Download from: [https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/)

- **Python** (3.8 or higher recommended)  
  Download from: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)  
  ✅ Make sure to check the box **"Add Python to PATH"** during installation.

### 2. Clone the Repository

Open Command Prompt or Git Bash and run:
```bash
git clone https://github.com/yourusername/EmployabilityAnalyticsApp.git
cd EmployabilityAnalyticsApp

git clone https://github.com/yourusername/EmployabilityAnalyticsApp.git
cd EmployabilityAnalyticsApp

## 3. Set Up a Virtual Environment
In the project folder:
python -m venv venv
venv\Scripts\activate

4. Install Dependencies
Ensure you're inside the activated virtual environment, then install all required packages:
pip install -r requirements.txt
pip install flask pandas plotly


## 🚀 Usage

Once the project is set up and running, you can use the application to explore employability trends for software developers.

### 🔧 Starting the Application

After activating your virtual environment, start the Flask server with:

```bash
python app.py

By default, the app will run at:
📍 http://127.0.0.1:5000/

Open this URL in your browser to interact with the application.

🔍 How to Use the Application
Sign Up or Log In

Create an account or log in with existing credentials to access the dashboard.

Overview Page

Explore top 20 companies, job titles, and in-demand skills via bar, area, and pie charts.

Dashboard Page

Select a job title to filter and view:

Relevant skills

Hiring companies

Job locations

Analysis Page

View company-wise job trends with salaries and roles across different dates.

Location Page

Select a location or company to see jobs available and get pie-chart breakdowns of:

Skills

Job types

Salaries


── Flask_Project/
│   ├── app.py                      # Main Flask application
│   ├── users.json                  # User authentication data
│   ├── static/                     # Static assets (CSS, JS)
│   │   ├── script.js
│   │   └── styles.css
│   ├── templates/                  # HTML templates (pages)
│   │   ├── analysis.html
│   │   ├── dashboard.html
│   │   ├── forgot_password.html
│   │   ├── location.html
│   │   ├── login.html
│   │   ├── overview.html
│   │   ├── reset_password.html
│   │   └── signup.html
│   └── uploads/                    # Folder for uploaded or used datasets
│       └── data.csv


## 9. 🙏 Acknowledgements

This project wouldn't have been possible without the support and tools provided by the following:

- [Flask](https://flask.palletsprojects.com/) — for building the web application backend.
- [Plotly](https://plotly.com/python/) — for creating interactive data visualizations.
- [Visual Studio](https://visualstudio.microsoft.com/) — as the development environment.
- [Python](https://www.python.org/) — the programming language that powers the application.
- [Job Listings Dataset (Kaggle)](https://www.kaggle.com/datasets/jobspikr/software-developer-job-listings-usa?resource=download) — for providing real-world job posting data for analysis.
- The open-source community — for tutorials, libraries, and documentation.

Special thanks to all contributors and mentors who supported this project.



  





  


