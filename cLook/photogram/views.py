# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from .code import *
from police.models import CriminalDetails
# Create your views here.
us=""
def p_login(request):
    if request.method == 'POST':
        n = request.POST
        global us
        us = n["username"]
        form = RegisterForm(n,request.FILES)
        if form.is_valid():
            if Register.objects.filter(username=us).exists():
                return redirect('p_login')
            else:
                form.save()
                obj=Register.objects.get(username=us)
                image_string="C:\\Users\\Hp\\PycharmProjects\\cLook\\cLook"+str(obj.profile_pic.url)
                print(image_string)
                try:
                    f=resize(image_string)
                    if f[0]!="Not Found":
                        g=str(f[0])
                        obj_police=CriminalDetails.objects.get(cid=g)
                        obj_police.social_media_id=obj.username
                        obj_police.status = "Found"
                        obj_police.save()
                except:
                    pass
                return redirect('profile')
    else:
        form = RegisterForm()
    return render(request,"photogram/signup.html",{'form':form})
def profile(request):
    obj=Register.objects.get(username=us)
    return render(request,"photogram/profile.html",{"obj":obj})
def p_log(request):
    return render(request,"photogram/login.html")
def profo(request):
    email = request.POST.get('email', 'default')
    password= request.POST.get('password', 'default')
    obj = Register.objects.get(email=email)
    if obj.password==password :
        return render(request,"photogram/profile.html",{"obj":obj})
    else:
        return render(request,"photogram/login.html")