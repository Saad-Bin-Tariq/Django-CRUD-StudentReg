from django.shortcuts import render, redirect
from .models import Student, Poi

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

def dis_map(request):
    poi=Poi.objects.all()

    return render(request,'std/map.html',{'poi':poi})

def dis(request):
    poi=Poi.objects.all()

    return render(request,'std/test.html',{'poi':poi})

def add_pt(request):
    if request.method=='POST':
        print('Added')
        #user inputs
        pt_name=request.POST.get('name')
        pt_lat=request.POST.get('lat')
        pt_long=request.POST.get('long')
       

        #creating object for model
        m=Poi()
        m.name=pt_name
        m.lat=pt_lat
        m.long=pt_long
        
        m.save()
        return redirect('/std/dis/')

       
    return render(request,'std/test.html',{})

def delete_map(request,gid):
    m=Poi.objects.get(pk=gid)
    m.delete()
    return redirect('/std/dis-map/')

def update_map(request,gid):
    m=Poi.objects.get(pk=gid)
    return render(request,'std/update_map.html',{'m':m})

def do_update_map(request,gid):
    pt_name=request.POST.get('pt_name')
    pt_lat=request.POST.get('pt_lat')
    pt_long=request.POST.get('pt_long')
    

    m=Poi.objects.get(pk=gid)

    m.name=pt_name
    m.lat=pt_lat
    m.long=pt_long
    
    m.save()
    return redirect('/std/dis-map')
