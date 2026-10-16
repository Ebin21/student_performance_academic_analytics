from django.urls import path
from . import views
urlpatterns=[path("students/",views.student_list,name="student_list"),path("students/new/",views.student_create,name="student_create"),path("students/<int:pk>/edit/",views.student_update,name="student_update"),path("subjects/",views.subject_list,name="subject_list"),path("subjects/new/",views.subject_create,name="subject_create"),path("assessments/",views.assessment_list,name="assessment_list"),path("assessments/new/",views.assessment_create,name="assessment_create"),path("reports/csv/",views.export_csv,name="export_csv")]
