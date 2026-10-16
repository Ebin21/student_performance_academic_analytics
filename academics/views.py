import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect,render
from .forms import StudentForm,SubjectForm,AssessmentForm
from .models import Student,Subject,Assessment
@login_required
def dashboard(request):
 students=Student.objects.filter(is_active=True); assessments=Assessment.objects.select_related("student","subject")
 rows=list(assessments); avg=round(sum(a.percentage for a in rows)/len(rows),2) if rows else 0
 passrate=round(sum(a.passed for a in rows)/len(rows)*100,1) if rows else 0
 subjects=[]
 for s in Subject.objects.all():
  sr=[a.percentage for a in rows if a.subject_id==s.id]; subjects.append((s.name,round(sum(sr)/len(sr),2) if sr else 0))
 perstudent=[]
 for st in students:
  sr=[a.percentage for a in rows if a.student_id==st.id]
  if sr: perstudent.append((st,round(sum(sr)/len(sr),2),len(sr)))
 top=sorted(perstudent,key=lambda x:x[1],reverse=True)[:5]
 return render(request,"academics/dashboard.html",{"total_students":students.count(),"total_subjects":Subject.objects.count(),"total_assessments":len(rows),"overall_average":avg,"pass_rate":passrate,"subject_labels":[x[0] for x in subjects],"subject_values":[x[1] for x in subjects],"student_labels":[x[0].student_id for x in top],"student_values":[x[1] for x in top],"top_students":top,"recent":rows[:10]})
@login_required
def student_list(request):
 qs=Student.objects.all(); q=request.GET.get("q","").strip()
 if q: qs=qs.filter(Q(student_id__icontains=q)|Q(full_name__icontains=q)|Q(course__icontains=q))
 return render(request,"academics/student_list.html",{"students":qs,"q":q})
@login_required
def student_create(request):
 form=StudentForm(request.POST or None)
 if form.is_valid(): form.save(); messages.success(request,"Student added."); return redirect("student_list")
 return render(request,"academics/form.html",{"form":form,"heading":"Add student"})
@login_required
def student_update(request,pk):
 obj=get_object_or_404(Student,pk=pk); form=StudentForm(request.POST or None,instance=obj)
 if form.is_valid(): form.save(); messages.success(request,"Student updated."); return redirect("student_list")
 return render(request,"academics/form.html",{"form":form,"heading":"Edit student"})
@login_required
def subject_list(request): return render(request,"academics/subject_list.html",{"subjects":Subject.objects.all()})
@login_required
def subject_create(request):
 form=SubjectForm(request.POST or None)
 if form.is_valid(): form.save(); messages.success(request,"Subject added."); return redirect("subject_list")
 return render(request,"academics/form.html",{"form":form,"heading":"Add subject"})
@login_required
def assessment_list(request):
 qs=Assessment.objects.select_related("student","subject"); student=request.GET.get("student",""); subject=request.GET.get("subject","")
 if student: qs=qs.filter(student_id=student)
 if subject: qs=qs.filter(subject_id=subject)
 return render(request,"academics/assessment_list.html",{"assessments":qs,"students":Student.objects.all(),"subjects":Subject.objects.all(),"selected_student":student,"selected_subject":subject})
@login_required
def assessment_create(request):
 form=AssessmentForm(request.POST or None)
 if form.is_valid(): form.save(); messages.success(request,"Assessment marks recorded."); return redirect("assessment_list")
 return render(request,"academics/form.html",{"form":form,"heading":"Record assessment"})
@login_required
def export_csv(request):
 qs=Assessment.objects.select_related("student","subject"); student=request.GET.get("student",""); subject=request.GET.get("subject","")
 if student: qs=qs.filter(student_id=student)
 if subject: qs=qs.filter(subject_id=subject)
 res=HttpResponse(content_type="text/csv; charset=utf-8"); res["Content-Disposition"]='attachment; filename="student_performance_report.csv"'; w=csv.writer(res)
 w.writerow(["Student ID","Student Name","Course","Semester","Subject Code","Subject","Assessment","Date","Marks","Maximum Marks","Percentage","Grade","Result"])
 for a in qs: w.writerow([a.student.student_id,a.student.full_name,a.student.course,a.student.semester,a.subject.code,a.subject.name,a.assessment_name,a.assessment_date.isoformat(),a.marks_obtained,a.subject.max_marks,a.percentage,a.grade,"Pass" if a.passed else "Fail"])
 return res
