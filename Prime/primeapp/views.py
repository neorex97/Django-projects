from django.shortcuts import render
from .forms import pform

# Create your views here.

def index(request):
    return render(request,'index.html')

def getform(request):
    if request.method=='GET':
        form = pform()
        return render(request,'eval.html',{'form': form})

    if request.method=='POST':
        form = pform(request.POST)
        if form.is_valid():
            u = request.POST.get('maxlimit')
            l = request.POST.get('minlimit')

            if u>l:
                res= sumprime(u,l)

                return render(request, 'result.html', {"s":res})
            else:
                return render(request,'val.html',{'form': form})



def sumprime(x,y):

    s=0
    x=int(x)
    y=int(y)
    for num in range(y, x+1):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                s=s+num
    print(s)
    return s





