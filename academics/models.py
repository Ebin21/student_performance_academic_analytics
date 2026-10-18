from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_id=models.CharField(max_length=20, unique=True)
    full_name=models.CharField(max_length=120)
    email=models.EmailField(blank=True)
    course=models.CharField(max_length=100, default="MSc Computer Applications")
    semester=models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1),MaxValueValidator(12)])
    joined_on=models.DateField(default=timezone.localdate)
    is_active=models.BooleanField(default=True)
    class Meta: ordering=["full_name"]
    def __str__(self): return f"{self.student_id} - {self.full_name}"
    @property
    def average_percentage(self):
        marks=list(self.marks.select_related("subject"))
        if not marks: return None
        return round(sum(m.percentage for m in marks)/len(marks),2)
    @property
    def attendance_percentage(self):
        records=list(self.attendance_records.all())
        if not records: return None
        return round(sum(1 for r in records if r.status=="PRESENT")/len(records)*100,2)

class Subject(models.Model):
    code=models.CharField(max_length=15, unique=True)
    name=models.CharField(max_length=100)
    semester=models.PositiveSmallIntegerField(default=3, validators=[MinValueValidator(1),MaxValueValidator(12)])
    max_marks=models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(1)])
    pass_marks=models.PositiveSmallIntegerField(default=40, validators=[MinValueValidator(0)])
    class Meta: ordering=["semester","name"]
    def __str__(self): return f"{self.code} - {self.name}"

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="marks")
    subject=models.ForeignKey(Subject,on_delete=models.PROTECT,related_name="marks")
    exam_name=models.CharField(max_length=80,default="Semester Exam")
    marks_obtained=models.DecimalField(max_digits=6,decimal_places=2,validators=[MinValueValidator(Decimal("0"))])
    recorded_on=models.DateField(default=timezone.localdate)
    class Meta:
        ordering=["student__full_name","subject__name"]
        constraints=[models.UniqueConstraint(fields=["student","subject","exam_name"],name="unique_student_subject_exam")]
    def clean(self):
        if self.subject_id and self.marks_obtained > self.subject.max_marks:
            raise ValidationError({"marks_obtained":f"Marks cannot exceed {self.subject.max_marks}."})
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
    @property
    def percentage(self): return round(float(self.marks_obtained)/self.subject.max_marks*100,2)
    @property
    def grade(self):
        p=self.percentage
        if p>=90:return "A+"
        if p>=80:return "A"
        if p>=70:return "B"
        if p>=60:return "C"
        if p>=50:return "D"
        if p>=40:return "E"
        return "F"
    @property
    def passed(self): return self.marks_obtained >= self.subject.pass_marks

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT="PRESENT","Present"
        ABSENT="ABSENT","Absent"
        EXCUSED="EXCUSED","Excused"
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="attendance_records")
    subject=models.ForeignKey(Subject,on_delete=models.PROTECT,related_name="attendance_records")
    date=models.DateField(default=timezone.localdate)
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PRESENT)
    class Meta:
        ordering=["-date"]
        constraints=[models.UniqueConstraint(fields=["student","subject","date"],name="unique_student_subject_attendance_day")]
    def __str__(self): return f"{self.student} - {self.subject} - {self.date}"
