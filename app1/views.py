from django.shortcuts import render
from .forms import StudentForm,StudentForm1

from .models import Student
# Create your views here.

def register1(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if  form.is_valid():
            name=request.POST.get('name')
            age=request.POST.get('age')
            address=request.POST.get('address')
            user=Student(name=name,age=age,address=address)
            user.save()
    form=StudentForm()
    return render(request,'home.html',{'form':form})

def register2(request):
    if request.method=='POST':
        form=StudentForm1(request.POST)
        if form.is_valid():
            form.save()
    form=StudentForm1()
    return render(request,'home1.html',{'form':form})



