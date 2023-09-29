from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_schlinfo(request):
    so=school()
    d={'so':so}
    if request.method=='POST':
        schlname=request.POST['schlname']
        pname=request.POST['pname']
        address=request.POST['add']
        S=school.objects.get_or_create(schlname=schlname,principal=pname,address=address)[0]
        S.save()
        info=school.objects.all()
        d={'info':info}
        return render(request,'display_schlinfo.html',d)

    return render(request,'insert_schlinfo.html')

def insert_student(request):
    st=student()
    d={'st':st}
    if request.method=='POST':
        sid=request.POST['sid']
        sname=request.POST['sname']
        semail=request.POST['semail']
        schlname=request.POST['schlname']

        S=school.objects.get(schlname=schlname)
        s=student.objects.get_or_create(sid=sid,sname=sname,semail=semail,schlname=S)[0]
        
        s.save()
        stinfo=student.objects.all()
        d={'stinfo':stinfo}
        return render(request,'display_student.html',d)
    

    return render(request,'insert_student.html')

        