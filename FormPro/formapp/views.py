from django.shortcuts import render
from  .forms import emform
from .models import Student

# Create your views here.
def gohome(request):
    return render(request, 'home.html')

def getform(request):
    if request.method=='GET':
        form = emform()
        return render(request,'registration.html',{'form': form})

    if request.method=='POST':
        form = emform(request.POST)

        if form.is_valid():
            print("form is valid")
            n = form.cleaned_data['name']
            d = form.cleaned_data['desig']
            e = request.POST.get('sal')

            s=Student(name=n,designation=d,sal=e)
            s.save()
            print("data saved")

            return getdetails(request)

def getdetails(request):
    obj=Student.objects.all()
    return render(request, 'viewdata.html', {'list': obj})

