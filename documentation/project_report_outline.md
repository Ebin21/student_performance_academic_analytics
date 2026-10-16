# MSc Project Report Outline

## Title
Student Performance and Academic Analytics System using Python Django

## Chapter 1 — Introduction
Background, problem statement, aim, objectives, scope, significance and limitations.

## Chapter 2 — Literature Review
Review student record systems, spreadsheet-based mark tracking and academic dashboards. Compare existing approaches and cite sources actually read.

## Chapter 3 — Requirements Analysis
Functional requirements: student/subject management, marks entry, validation, grade calculation, dashboard, search/filter, CSV reports, login/admin. Non-functional: usability, data integrity, maintainability, security and performance.

## Chapter 4 — System Design
Include architecture, use-case diagram, ER diagram, DFD, activity diagram, navigation map, schema and UI wireframes. Architecture: Browser -> Django views/forms -> Django ORM -> SQLite. Relationships: Student 1-to-many Assessment; Subject 1-to-many Assessment.

## Chapter 5 — Implementation
Explain setup, models, forms, views, URLs, authentication, mark validation, percentage/grade calculation, dashboard aggregation, charts and CSV export. Explain selected code rather than pasting every file.

## Chapter 6 — Testing
Record test ID, scenario, input, expected result, actual result, Pass/Fail and screenshot. Do not claim a test passed unless you ran it. Suggested tests: login redirect; student creation; duplicate ID rejection; marks above max rejected; grade calculation; search; CSV headers/rows; dashboard login.

## Chapter 7 — Results and Discussion
Add actual screenshots, CSV output and observations from synthetic sample records. Do not make claims about real students based on demo data.

## Chapter 8 — Conclusion and Future Scope
Summarize objective completion. Future work: role permissions, attendance, credit-weighted GPA/CGPA, PDF report cards, email alerts, CSV import, REST API and deployment.

## Data dictionary
Student: student_id (unique identifier), full_name, email, course, semester, joined_on, is_active. Subject: code, name, max_marks, pass_marks. Assessment: student_id FK, subject_id FK, assessment_name, assessment_date, marks_obtained, remarks.

## Appendices
Installation guide, user guide, selected source, test evidence, screenshots, sample CSV and GitHub URL.
