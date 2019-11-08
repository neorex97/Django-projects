from django.shortcuts import render
from  .forms import pform
from .models import Product

# Create your views here.
def gohome(request):
    return render(request, 'home.html')

def getform(request):
    if request.method=='GET':
        form = pform()
        return render(request,'create_product.html',{'form': form})

    if request.method=='POST':
        form = pform(request.POST)

        if form.is_valid():
            print("form is valid")
            n = form.cleaned_data['nam']
            c = form.cleaned_data['cat']
            p = request.POST.get('pri')
            s =form.cleaned_data['spe']

            obj=Product(name=n,category=c,price=p,spec=s)
            obj.save()
            print("data saved")

            return getdetails(request)

def getdetails(request):
    obj=Product.objects.all()
    return render(request, 'Productdata.html', {'list': obj})

