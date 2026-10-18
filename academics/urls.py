from django.urls import path
from . import views
urlpatterns=[
 path("students/",views.student_list,name="student_list"),path("students/new/",views.student_create,name="student_create"),
 path("students/<int:pk>/",views.student_detail,name="student_detail"),path("students/<int:pk>/edit/",views.student_update,name="student_update"),
 path("students/<int:pk>/delete/",views.student_delete,name="student_delete"),
 path("subjects/",views.subject_list,name="subject_list"),path("subjects/new/",views.subject_create,name="subject_create"),
 path("marks/",views.mark_list,name="mark_list"),path("marks/new/",views.mark_create,name="mark_create"),
 path("attendance/",views.attendance_list,name="attendance_list"),path("attendance/new/",views.attendance_create,name="attendance_create"),
 path("reports/",views.reports,name="reports"),path("reports/export.csv",views.export_csv,name="export_csv"),
]
