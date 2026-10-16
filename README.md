# Student Performance & Academic Analytics System
MSc Computer Applications Semester 3 starter project using Python, Django, SQLite, Bootstrap and Chart.js.

Features: login, student CRUD/search/edit, subject setup, mark entry and validation, percentage/grade/pass-fail, dashboard charts, filtered assessment reports, CSV export, Django admin and automated tests.

Demo grade bands: A+ >=90, A >=80, B >=70, C >=60, D >=50, E >=40, F <40. Replace with official university grading rules if different.

## Windows setup
1. Install Python 3.11+ and VS Code; extract this folder.
2. `py -m venv .venv`
3. PowerShell: ` .\.venv\Scripts\Activate.ps1` (Command Prompt: `.venv\Scripts\activate.bat`)
4. `python -m pip install --upgrade pip`
5. `pip install -r requirements.txt`
6. `python manage.py makemigrations academics`
7. `python manage.py migrate`
8. `python manage.py createsuperuser`
9. `python manage.py runserver`
10. Open http://127.0.0.1:8000/ and log in. Admin: /admin/.
11. Run tests with `python manage.py test`.

Demo flow: add subjects, add students, record assessment marks, review dashboard, export CSV.

Limitations: authenticated users currently share access; add role-based permissions before real use. Use synthetic data only. Grade thresholds are examples. Dashboard averages are unweighted averages of assessment percentages, not credit-weighted GPA/CGPA. Before deployment, set DEBUG=False, use environment secrets, HTTPS, backups, production database and strict access control.
