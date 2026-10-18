# MSc Project Report Outline

## Title
Student Performance and Academic Analytics System using Python Django

## Chapter 1 — Introduction
Background, problem statement, aim, measurable objectives, scope, assumptions and limitations.

## Chapter 2 — Literature Review
Discuss manual academic records, spreadsheets and student information systems. Compare accuracy, access, reporting and auditability. Cite sources actually consulted.

## Chapter 3 — Requirements Analysis
Functional: student CRUD, subjects, marks, grade calculation, attendance, dashboard, reports, CSV export.
Non-functional: usability, data integrity, maintainability, authentication and reasonable performance.
Document roles and prototype access-control limitations.

## Chapter 4 — System Design
Include architecture (Browser → Django views/forms → ORM → SQLite), use-case diagram, ER diagram, data-flow diagram, activity diagram, UI wireframes and data dictionary.

## Chapter 5 — Implementation
Explain setup, models, forms, views, URLs, templates, validation, grade logic, attendance calculation, charts and CSV generation.

## Chapter 6 — Testing
Record test ID, scenario, input, expected result, actual result, evidence and Pass/Fail. Do not claim a test passed unless executed.

## Chapter 7 — Results and Discussion
Dashboard screenshots, sample CSV, observed patterns, edge cases and limitations. Use synthetic data.

## Chapter 8 — Conclusion and Future Enhancements
Objective completion; future work: role-based permissions, GPA/CGPA, subject-specific rules, attendance alerts, PDF reports, bulk CSV import, pagination, audit logs, PostgreSQL and deployment.

## Data dictionary
Student: student_id (unique identifier), full_name, email, course, semester, joined_on, is_active.
Subject: code (unique), name, semester, max_marks, pass_marks.
Mark: student_id FK, subject_id FK, exam_name, marks_obtained, recorded_on.
Attendance: student_id FK, subject_id FK, date, status.

## Example test cases
TC-01 dashboard without login redirects to login.
TC-02 unique student ID saves successfully.
TC-03 duplicate student ID is rejected.
TC-04 marks above subject maximum produce validation error.
TC-05 85/100 produces 85%, grade A, pass.
TC-06 one present and one absent record produces 50% attendance.
TC-07 CSV export downloads expected columns.
TC-08 adding a subject makes it visible in subject list.
TC-09 empty dashboard renders without errors.

Appendices: installation guide, user guide, selected source code, screenshots, test evidence, sample CSV and GitHub URL.
