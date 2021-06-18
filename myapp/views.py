from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Resume
from .forms import ResumeForm,UserForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request,'register.html',{"form":form})

    
@login_required
def home(request):
    obj = Resume.objects.all()
    if request.method == "POST":
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ResumeForm()
       
    return render(request,'home.html',{'form':form, "obj":obj})
@login_required
def detailview(request,pk):
    obj = Resume.objects.get(pk = pk)
    return render(request,'users.html',{"obj":obj})