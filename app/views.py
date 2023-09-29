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