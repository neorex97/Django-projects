from django.shortcuts import render
from stdapp.models import User,Course,Batch,Feedback
# Create your views here.
from stdapp.forms import std_frm

def home(request):
    return render(request,'registration/home.html')

def reg(request):
    if request.method == 'GET':
        form = std_frm()
        return render(request,'signup.html',{'form':form})

    if request.method == 'POST':
        form = std_frm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            print("data saved successfully")

            return render(request,'registration/home.html',{'form':form})

def login(request):
    if request.method == 'GET':
        form = std_frm()
        return render(request, 'registration/login.html', {'form': form})
    if request.method == 'POST':
        form = std_frm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            name = form.cleaned_data['Name']
            password = form.cleaned_data['password']





