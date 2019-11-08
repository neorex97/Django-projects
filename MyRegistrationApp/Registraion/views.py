from django.shortcuts import render

# Create your views here.
from Registraion.models import Person
from .forms import Reg_frm,login_frm


def register(request):
    if request.method=='GET':
        form=Reg_frm()
        # return render(request,'home.html',{'form':form})

    if request.method=="POST":
        form=Reg_frm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']

            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            pwd = form.cleaned_data['pwd']
            print(name,email,phone,pwd)
            q=Person.objects.filter(username=name).count()
            if q>0:
                print("user already exist")
                return render(request, 'error.html', {'form': form})
            else:

                obj=Person(username=name,email=email,phone=phone,pwd=pwd)
                obj.save()






    return render(request, 'home.html', {'form': form})

def login(request):
    if request.method=='GET':
        form=login_frm()

    if request.method=='POST':
        form=login_frm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            print("log")
            if Person.objects.filter(username=username).filter(pwd=pwd):
                print("login successfull")
            else:
                print("invalid username or password")



    return render(request,'login.html',{'form':form})