# Student Performance & Academic Analytics System
MSc Computer Applications Semester 3 starter project using Python, Django, SQLite, Bootstrap and Chart.js.

## Features
- Login with Django authentication
- Student and subject management
- Marks entry, percentages, grades and pass/fail
- Attendance tracking and percentage calculation
- Dashboard KPIs, subject-average and grade-distribution charts
- Student detail pages, academic report and CSV export
- Django admin and starter automated tests

## Demo rules
Grade bands: A+ >=90, A >=80, B >=70, C >=60, D >=50, E >=40, F <40. Subject pass/fail uses each subject's configured pass mark. Summary report uses 40% overall average as a demonstration rule; actual university regulations can differ.
Attendance = Present records / all recorded attendance x 100. Excused records remain in the denominator but not the numerator in this prototype.

## Windows setup
1. Install Python 3.11+ and enable Add Python to PATH.
2. Extract ZIP and open folder in VS Code.
3. `py -m venv .venv`
4. `.\.venv\Scripts\Activate.ps1` (or `.venv\Scripts\activate.bat` in Command Prompt)
5. `python -m pip install --upgrade pip`
6. `pip install -r requirements.txt`
7. `python manage.py makemigrations academics`
8. `python manage.py migrate`
9. `python manage.py createsuperuser`
10. `python manage.py runserver`
11. Visit http://127.0.0.1:8000/ and sign in. Admin: http://127.0.0.1:8000/admin/

Run tests: `python manage.py test`

## Demo sequence
Add subjects, add students, record marks, record attendance, inspect dashboard/student detail, then export the report CSV.

## Limitations and security
This is an academic prototype. All authenticated users can view academic records; add role-based permissions before real use. Subjects/marks/attendance can be managed through Django Admin; their edit/delete UI is not implemented in this first version. Use synthetic data. Before deployment, set DEBUG=False, move SECRET_KEY to environment variables, configure ALLOWED_HOSTS, HTTPS, secure cookies, backups, access permissions and a production database.

GitHub description: A Django academic analytics app for managing students, marks, attendance, grades, dashboards and CSV performance reports.
