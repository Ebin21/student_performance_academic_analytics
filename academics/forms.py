from django import forms
from .models import Student,Subject,Assessment
class StyledForm(forms.ModelForm):
 def style(self):
  for f in self.fields.values(): f.widget.attrs["class"]="form-select" if isinstance(f.widget,forms.Select) else "form-check-input" if isinstance(f.widget,forms.CheckboxInput) else "form-control"
class StudentForm(StyledForm):
 class Meta:
  model=Student; fields=["student_id","full_name","email","course","semester","joined_on","is_active"]
  widgets={"joined_on":forms.DateInput(attrs={"type":"date"})}
 def __init__(self,*a,**kw): super().__init__(*a,**kw); self.style()
class SubjectForm(StyledForm):
 class Meta: model=Subject; fields=["code","name","max_marks","pass_marks"]
 def __init__(self,*a,**kw): super().__init__(*a,**kw); self.style()
class AssessmentForm(StyledForm):
 class Meta:
  model=Assessment; fields=["student","subject","assessment_name","assessment_date","marks_obtained","remarks"]
  widgets={"assessment_date":forms.DateInput(attrs={"type":"date"}),"marks_obtained":forms.NumberInput(attrs={"step":"0.01","min":"0"})}
 def __init__(self,*a,**kw): super().__init__(*a,**kw); self.style()
 def clean(self):
  data=super().clean(); sub=data.get("subject"); marks=data.get("marks_obtained")
  if sub and marks is not None and marks>sub.max_marks: self.add_error("marks_obtained",f"Marks cannot exceed {sub.max_marks}.")
  return data
