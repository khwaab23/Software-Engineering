from django.shortcuts import render

def cv_view(request):
    cv_data = {
        "name": "Khwaab Thareja",
        "contact": {
            "phone": "(934)-204-7656",
            "email": "kt3180@nyu.edu",
            "linkedin": "https://www.linkedin.com/in/khwaab-thareja-23t/",
            "github": "https://github.com/khwaab23"
        },
        "education": [
            {
                "institution": "New York University, NY, USA",
                "degree": "Master of Science in Computer Science",
                "duration": "Sep 2024 - May 2026",
                "cgpa": "3.9/4",
                "coursework": ["Software Engineering-1", "Machine Learning (ML)", "Artificial Intelligence (AI)"]
            },
            {
                "institution": "Vellore Institute of Technology, Vellore, India",
                "degree": "B.Tech Computer Science",
                "duration": "Jul 2018 - May 2022",
                "cgpa": "8.75/10",
                "coursework": ["Machine Learning (ML)", "Artificial Intelligence (AI)", "Data Analytics"]
            }
        ],
        "experience": [
            {
                "position": "Unit Manager - Payments - Data Science",
                "company": "Bajaj Finance Limited",
                "duration": "Aug 2023 - Aug 2024",
                "location": "Pune, India",
                "responsibilities": [
                    "Engineered a document management system for QR Pay operations with Python, achieving 87% accuracy.",
                    "Analyzed clickstream data for 60M+ users using CleverTap, Python, C#, and JavaScript.",
                    "Developed Power BI dashboards, reducing manual reporting time by 15 hours per month.",
                    "Enhanced UPI fraud detection by 35% using Python-based anomaly detection."
                ]
            },
            {
                "position": "Deputy Unit Manager - Insurance COE - Data Analyst",
                "company": "Bajaj Finance Limited",
                "duration": "Jul 2022 - Aug 2023",
                "responsibilities": [
                    "Designed an advanced Insurance Recommendation Model with Python and SQL, increasing engagement by 25%.",
                    "Built ARIMA models for revenue forecasting, reducing payment processing time from 3 days to 2 hours.",
                    "Enhanced software solutions with C#, .NET, JavaScript, and Angular, improving efficiency by 30%."
                ]
            }
        ],
        "projects": [
            {
                "title": "Advanced Stock Market Visualization",
                "link": "https://github.com/khwaab23/InfoVizProject",
                "description": "Developed interactive stock market visualizations using Streamlit, Dash, D3.js, and Matplotlib."
            },
            {
                "title": "Welcome Home - Full-Stack Donation System",
                "link": "https://github.com/khwaab23/WelcomeHome",
                "description": "Developed a full-stack donation management system with Flask & MySQL, improving inventory accuracy by 30%."
            }
        ],
        "leadership": {
            "title": "Deputy Managing Director",
            "organization": "Entrepreneurship Cell VIT",
            "duration": "Apr 2020 - Mar 2021",
            "responsibilities": [
                "Led a team of 150+ students, organized 30+ events promoting startup culture and entrepreneurial initiatives."
            ]
        }
    }
    return render(request, 'cv.html', cv_data)
