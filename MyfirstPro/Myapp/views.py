from django.shortcuts import render

# Create your views here.
def getloginpage(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html',{"name":['abc','cde','efg']})
def home(request):
    return render(request,'home.html')


def insert(request):
    name=request.POST.get("name")
    address=request.POST.get("Address")
    print(name)
    print(address)
    
    return render(request,'home.html')