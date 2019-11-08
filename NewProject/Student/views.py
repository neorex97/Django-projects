from django.shortcuts import render
from Student.models import Students
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    return render(request,'register.html')

def viewdata(request):
    return render(request,'viewdata.html')

def search(request):
    return render(request,'search.html')


def insertToStudent(request):
    print("inside sum")
    name = request.POST.get("name")
    addr = request.POST.get("address")
    pho = request.POST.get("phone")
    cour = request.POST.get("course")
    print(name,addr)


    s=Students(name=name,address=addr,phone=pho,course=cour)
    s.save()
    return getdetails(request)
def getdetails(request):
    print("insert getdetails")
    s=Students.objects.all()
    return render(request,'viewdata.html',{"stdlist":s})

