# 💼 Django Job Board

A full-featured **Job Board** web application built with **Django**, designed to help employers post job vacancies and allow job seekers to find and apply for jobs easily.  
The platform supports user roles, job applications, search, filtering, and an admin dashboard.

---

## 📌 Features

- 🧑‍💼 Employers can:
  - Post, edit, and delete jobs
  - View applications
  - Manage job status (active/closed)

- 👨‍🎓 Job Seekers can:
  - Search and filter jobs by keyword, location, or category
  - Apply for jobs directly
  - Track submitted applications

- 🔒 User Authentication:
  - Role-based access for Admin, Employer, Job Seeker
  - Secure registration and login

- 📊 Admin Panel:
  - View all users, jobs, applications
  - Control platform settings (via Django Admin)

- 🌍 Responsive Design (Bootstrap or Tailwind)
- 🌐 Multilingual-ready (optional)

---

## 🧑‍💻 Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Framework     | Django (Python)   |
| Templating    | Django Templates  |
| Database      | SQLite / PostgreSQL |
| Styling       | Bootstrap 5       |
| Auth          | Django's built-in auth system |
| Admin Panel   | Django Admin      |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mo7amedshaban/Job_Board.git
cd Job_Board

```

2. Create Virtual Environment

```bash

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. Install Requirements
```bash

pip install -r requirements.txt
```
4. Set Up the Database
```bash

python manage.py migrate
```
5. Create Superuser
```bash

python manage.py createsuperuser
```
6. Run the Development Server
```bash

python manage.py runserver
Access the app at: http://127.0.0.1:8000/
```
