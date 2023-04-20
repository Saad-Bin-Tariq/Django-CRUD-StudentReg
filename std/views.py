from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def home(request):
    std=Student.objects.all()

    return render(request,'std/home.html',{'std':std})

def add_std(request):
    if request.method=='POST':
        print('Added')
        #user inputs
        st_roll=request.POST.get('std_roll')
        st_name=request.POST.get('std_name')
        st_email=request.POST.get('std_email')
        st_phone=request.POST.get('std_phone')

        #creating object for model
        s=Student()
        s.roll=st_roll
        s.name=st_name
        s.email=st_email
        s.phone=st_phone

        s.save()
        return redirect('/std/home/')

       
    return render(request,'std/add_std.html',{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect('/std/home/')

def update_std(request,roll):
    std=Student.objects.get(pk=roll)
    return render(request,'std/update_std.html',{'std':std})

def do_update_std(request,roll):
    std_roll=request.POST.get('std_roll')
    std_name=request.POST.get('std_name')
    std_email=request.POST.get('std_email')
    std_phone=request.POST.get('std_phone')

    std=Student.objects.get(pk=roll)

    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.phone=std_phone
    
    std.save()
    return redirect('/std/home')
