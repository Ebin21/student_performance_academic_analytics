from django.contrib import admin
from .models import Student,Subject,Mark,Attendance
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("student_id","full_name","course","semester","is_active")
    list_filter=("course","semester","is_active"); search_fields=("student_id","full_name","email")
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=("code","name","semester","max_marks","pass_marks"); search_fields=("code","name")
@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display=("student","subject","exam_name","marks_obtained","recorded_on"); list_filter=("subject","exam_name")
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=("student","subject","date","status"); list_filter=("subject","date","status")
