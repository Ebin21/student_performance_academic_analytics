from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
class Student(models.Model):
 student_id=models.CharField(max_length=20,unique=True)
 full_name=models.CharField(max_length=120)
 email=models.EmailField(blank=True)
 course=models.CharField(max_length=100,default="MSc Computer Applications")
 semester=models.PositiveSmallIntegerField(default=3,validators=[MinValueValidator(1),MaxValueValidator(12)])
 joined_on=models.DateField(default=timezone.localdate)
 is_active=models.BooleanField(default=True)
 class Meta: ordering=["student_id"]
 def __str__(self): return f"{self.student_id} - {self.full_name}"
class Subject(models.Model):
 code=models.CharField(max_length=15,unique=True)
 name=models.CharField(max_length=100)
 max_marks=models.PositiveSmallIntegerField(default=100,validators=[MinValueValidator(1)])
 pass_marks=models.PositiveSmallIntegerField(default=40,validators=[MinValueValidator(0)])
 class Meta: ordering=["code"]
 def __str__(self): return f"{self.code} - {self.name}"
class Assessment(models.Model):
 student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="assessments")
 subject=models.ForeignKey(Subject,on_delete=models.PROTECT,related_name="assessments")
 assessment_name=models.CharField(max_length=100,default="Semester Examination")
 assessment_date=models.DateField(default=timezone.localdate)
 marks_obtained=models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(0)])
 remarks=models.CharField(max_length=250,blank=True)
 class Meta:
  ordering=["student__student_id","subject__code","-assessment_date"]
  constraints=[models.UniqueConstraint(fields=["student","subject","assessment_name"],name="unique_student_subject_assessment")]
 def clean(self):
  from django.core.exceptions import ValidationError
  if self.subject_id and self.marks_obtained is not None and self.marks_obtained>self.subject.max_marks: raise ValidationError({"marks_obtained":f"Marks cannot exceed {self.subject.max_marks}."})
 @property
 def percentage(self): return round(float(self.marks_obtained)/self.subject.max_marks*100,2) if self.subject.max_marks else 0
 @property
 def passed(self): return self.marks_obtained>=self.subject.pass_marks
 @property
 def grade(self):
  p=self.percentage
  return "A+" if p>=90 else "A" if p>=80 else "B" if p>=70 else "C" if p>=60 else "D" if p>=50 else "E" if p>=40 else "F"
 def __str__(self): return f"{self.student.student_id} - {self.subject.code}: {self.marks_obtained}"
