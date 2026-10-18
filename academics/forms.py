from django import forms
from .models import Student, Subject, Mark, Attendance
class StyledForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for f in self.fields.values():
            f.widget.attrs["class"]="form-select" if isinstance(f.widget,forms.Select) else "form-control"
class StudentForm(StyledForm):
    class Meta:
        model=Student; fields=["student_id","full_name","email","course","semester","joined_on","is_active"]
        widgets={"joined_on":forms.DateInput(attrs={"type":"date"})}
class SubjectForm(StyledForm):
    class Meta: model=Subject; fields=["code","name","semester","max_marks","pass_marks"]
class MarkForm(StyledForm):
    class Meta:
        model=Mark; fields=["student","subject","exam_name","marks_obtained","recorded_on"]
        widgets={"recorded_on":forms.DateInput(attrs={"type":"date"})}
class AttendanceForm(StyledForm):
    class Meta:
        model=Attendance; fields=["student","subject","date","status"]
        widgets={"date":forms.DateInput(attrs={"type":"date"})}
