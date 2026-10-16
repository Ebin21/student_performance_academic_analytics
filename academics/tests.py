from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Student,Subject,Assessment
class AcademicTests(TestCase):
 def setUp(self):
  self.student=Student.objects.create(student_id="ST001",full_name="Test Student")
  self.subject=Subject.objects.create(code="PY101",name="Python",max_marks=100,pass_marks=40)
 def test_grade_and_pass(self):
  a=Assessment.objects.create(student=self.student,subject=self.subject,assessment_name="Midterm",assessment_date=date(2026,1,1),marks_obtained=85)
  self.assertEqual(a.percentage,85.0); self.assertEqual(a.grade,"A"); self.assertTrue(a.passed)
 def test_fail(self):
  a=Assessment.objects.create(student=self.student,subject=self.subject,assessment_name="Quiz",marks_obtained=25)
  self.assertEqual(a.grade,"F"); self.assertFalse(a.passed)
 def test_login_required(self): self.assertEqual(self.client.get(reverse("dashboard")).status_code,302)
 def test_dashboard_after_login(self):
  u=get_user_model().objects.create_user(username="testuser",password="Testpass123!"); self.client.login(username="testuser",password="Testpass123!")
  self.assertEqual(self.client.get(reverse("dashboard")).status_code,200)
