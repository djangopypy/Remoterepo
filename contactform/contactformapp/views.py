from django.shortcuts import render
from.forms import EmpForm
from.models import EmpDATA

def Emp_view(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        if eform.is_valid():
            name1=request.POST.get('name')
            email1=request.POST.get('email')
            salary1=request.POST.get('salary')
            location1=request.POST.get('location')

            data=EmpDATA(
                name=name1,
                email=email1,
                salary=salary1,
                location=location1
            )
        data.save()
        eform=EmpForm()
        return render(request,'empdata.html',{'abcd':eform})
    else:
        eform=EmpForm()
        return render(request,'empdata.html',{'abcd':eform})

def fetchingdata(request):
        edata=EmpDATA.objects.all()
        return render(request,'Empdatadisplay.html',{'edata':edata})



