from django.contrib import admin
from .models import Student,Subject,Assessment
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): list_display=("student_id","full_name","course","semester","is_active"); search_fields=("student_id","full_name","email"); list_filter=("course","semester","is_active")
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin): list_display=("code","name","max_marks","pass_marks"); search_fields=("code","name")
@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin): list_display=("student","subject","assessment_name","marks_obtained","assessment_date"); list_filter=("subject","assessment_name","assessment_date")
