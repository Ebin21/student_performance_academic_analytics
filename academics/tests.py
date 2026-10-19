from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Student,Subject,Mark,Attendance
class ModelTests(TestCase):
 def setUp(self):
  self.student=Student.objects.create(student_id="MCA001",full_name="Sample Student")
  self.subject=Subject.objects.create(code="PY301",name="Python Django",max_marks=100,pass_marks=40)
 def test_grade_and_percentage(self):
  m=Mark.objects.create(student=self.student,subject=self.subject,marks_obtained=Decimal("85"))
  self.assertEqual(m.percentage,85.0); self.assertEqual(m.grade,"A"); self.assertTrue(m.passed)
 def test_attendance_percentage(self):
  Attendance.objects.create(student=self.student,subject=self.subject,status="PRESENT")
  Attendance.objects.create(student=self.student,subject=self.subject,status="ABSENT")
  self.assertEqual(self.student.attendance_percentage,50.0)
 def test_marks_above_max_rejected(self):
  with self.assertRaises(Exception):
   Mark.objects.create(student=self.student,subject=self.subject,marks_obtained=Decimal("120"))
class ViewTests(TestCase):
 def setUp(self): self.user=get_user_model().objects.create_user(username="admin",password="Testpass123!")
 def test_dashboard_login_required(self):
  self.assertEqual(self.client.get(reverse("dashboard")).status_code,302)
 def test_dashboard_after_login(self):
  self.client.login(username="admin",password="Testpass123!")
  self.assertEqual(self.client.get(reverse("dashboard")).status_code,200)
