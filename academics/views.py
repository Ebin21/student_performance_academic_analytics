import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect,render
from .forms import StudentForm,SubjectForm,MarkForm,AttendanceForm
from .models import Student,Subject,Mark,Attendance

@login_required
def dashboard(request):
    students=Student.objects.filter(is_active=True); marks=list(Mark.objects.select_related("student","subject")); attendance=Attendance.objects.all()
    average=sum(m.percentage for m in marks)/len(marks) if marks else 0
    pass_rate=sum(1 for m in marks if m.passed)/len(marks)*100 if marks else 0
    att_total=attendance.count(); att_rate=attendance.filter(status="PRESENT").count()/att_total*100 if att_total else 0
    subject_rows=[]
    for sub in Subject.objects.all():
        vals=[m.percentage for m in marks if m.subject_id==sub.id]
        subject_rows.append((sub.name,round(sum(vals)/len(vals),1) if vals else 0))
    grades={g:0 for g in ["A+","A","B","C","D","E","F"]}
    for m in marks: grades[m.grade]+=1
    ranked=[]
    for s in students:
        avg=s.average_percentage
        if avg is not None: ranked.append({"student":s,"average":avg})
    ranked.sort(key=lambda x:x["average"],reverse=True)
    return render(request,"academics/dashboard.html",{
      "student_count":students.count(),"subject_count":Subject.objects.count(),"mark_count":len(marks),
      "average_marks":round(average,1),"pass_rate":round(pass_rate,1),"attendance_rate":round(att_rate,1),
      "subject_labels":[x[0] for x in subject_rows],"subject_values":[x[1] for x in subject_rows],
      "grade_labels":list(grades),"grade_values":list(grades.values()),"top_students":ranked[:5],
      "recent_marks":sorted(marks,key=lambda m:m.recorded_on,reverse=True)[:8]})

@login_required
def student_list(request):
    qs=Student.objects.all(); q=request.GET.get("q","").strip(); semester=request.GET.get("semester","").strip()
    if q: qs=qs.filter(Q(student_id__icontains=q)|Q(full_name__icontains=q)|Q(email__icontains=q))
    if semester.isdigit(): qs=qs.filter(semester=int(semester))
    return render(request,"academics/student_list.html",{"students":qs,"q":q,"semester":semester})
@login_required
def student_create(request):
    form=StudentForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,"Student created."); return redirect("student_list")
    return render(request,"academics/form.html",{"form":form,"heading":"Add student"})
@login_required
def student_update(request,pk):
    obj=get_object_or_404(Student,pk=pk); form=StudentForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,"Student updated."); return redirect("student_detail",pk=pk)
    return render(request,"academics/form.html",{"form":form,"heading":"Edit student"})
@login_required
def student_detail(request,pk):
    s=get_object_or_404(Student,pk=pk)
    return render(request,"academics/student_detail.html",{"student":s,"marks":s.marks.select_related("subject"),"attendance":s.attendance_records.select_related("subject")[:30]})
@login_required
def student_delete(request,pk):
    obj=get_object_or_404(Student,pk=pk)
    if request.method=="POST": obj.delete(); messages.success(request,"Student deleted."); return redirect("student_list")
    return render(request,"academics/confirm_delete.html",{"object":obj})
@login_required
def subject_list(request): return render(request,"academics/subject_list.html",{"subjects":Subject.objects.all()})
@login_required
def subject_create(request):
    form=SubjectForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,"Subject created."); return redirect("subject_list")
    return render(request,"academics/form.html",{"form":form,"heading":"Add subject"})
@login_required
def mark_list(request):
    qs=Mark.objects.select_related("student","subject"); q=request.GET.get("q","").strip()
    if q: qs=qs.filter(Q(student__full_name__icontains=q)|Q(student__student_id__icontains=q)|Q(subject__name__icontains=q)|Q(exam_name__icontains=q))
    return render(request,"academics/mark_list.html",{"marks":qs,"q":q})
@login_required
def mark_create(request):
    form=MarkForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,"Marks recorded."); return redirect("mark_list")
    return render(request,"academics/form.html",{"form":form,"heading":"Record marks"})
@login_required
def attendance_list(request): return render(request,"academics/attendance_list.html",{"records":Attendance.objects.select_related("student","subject")[:300]})
@login_required
def attendance_create(request):
    form=AttendanceForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,"Attendance recorded."); return redirect("attendance_list")
    return render(request,"academics/form.html",{"form":form,"heading":"Record attendance"})
@login_required
def reports(request):
    rows=[]
    for s in Student.objects.filter(is_active=True):
        avg=s.average_percentage; att=s.attendance_percentage
        rows.append({"student":s,"average":avg,"attendance":att,"result":"Pass" if avg is not None and avg>=40 else ("Fail" if avg is not None else "No marks")})
    rows.sort(key=lambda r:(r["average"] is not None,r["average"] or 0),reverse=True)
    return render(request,"academics/reports.html",{"rows":rows})
@login_required
def export_csv(request):
    response=HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"]='attachment; filename="student_performance_report.csv"'
    writer=csv.writer(response); writer.writerow(["Student ID","Student Name","Course","Semester","Average Percentage","Attendance Percentage","Result"])
    for s in Student.objects.filter(is_active=True):
        avg=s.average_percentage; att=s.attendance_percentage
        result="Pass" if avg is not None and avg>=40 else ("Fail" if avg is not None else "No marks")
        writer.writerow([s.student_id,s.full_name,s.course,s.semester,avg if avg is not None else "",att if att is not None else "",result])
    return response
