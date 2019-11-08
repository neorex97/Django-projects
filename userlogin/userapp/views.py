from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from userapp.forms import reg_frm, login_frm
from userapp.models import user
def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method == 'GET':
        form = reg_frm()


    if request.method == 'POST':
        form = reg_frm(request.POST)
        if form.is_valid():
            print("form is valid")
            name = form.cleaned_data['username']
            pho = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']

            c=user.objects.filter(username=name).count()
            if c>0:
                print("user already exist")
                return render(request, 'message.html',{'msg':"Username already exists"})
            else:
                usr=user(username=name,phone=pho,email=email,password=pwd)
                usr.save()
                return render(request, 'home.html', {'msg':"Registration successfull"})
                print("registration successfull")
    return render(request, 'Registration.html', {'form': form})


def login(request):
    if request.method == 'GET':
        form = login_frm()

    if request.method == 'POST':
            form = login_frm(request.POST)
            if form.is_valid():
                name= form.cleaned_data['username']
                pwd = form.cleaned_data['password']

                if user.objects.filter(username=name).filter(password=pwd):
                    print("login successfull")
                    return render(request, 'mypage.html', {'msg': name})
                else:
                    print("login unsuccessfull")
                    return render(request, 'message.html', {'msg': "invalid username or password"})


    return render(request,'login.html',{'form':form})
