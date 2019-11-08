from django.shortcuts import render

# Create your views here.
from BasicformApp.forms import new_frm
from BasicformApp.models import Usr


def getfrm(request):
    if request.method == 'GET':
        form = new_frm()
        return render(request,'BasicformApp/index.html',{'form':form})

    if request.method == 'POST':
        form = new_frm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save(commit=True)
            print("saved")
            p = Usr.objects.all()
            print(p)

        else:
            print("ERROR")


    return render(request, 'BasicformApp/index.html', {'form': form})