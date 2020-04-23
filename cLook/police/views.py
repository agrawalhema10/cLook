from django.shortcuts import render,redirect
# Create your views here.
from .forms import *
def police_login(request):
    return render(request,"police/login.html")
def police_home(request):
    if request.method=="POST":
        u_n = request.POST.get('phone', 'default')
        password = request.POST.get('password', 'default')
        if u_n != None and password != None:
            if u_n == '8103831751' and password == '2590':
                obj = CriminalDetails.objects.all()
                count=len(obj)
                context={'obj':obj,'count':count}
                return render(request,"police/home.html",context)
    else:
        redirect("police_login")
def add_criminal(request):
    if request.method == 'POST':
        n=request.POST
        criminal_id=n["cid"]
        criminal_name=n["name"]
        print(criminal_id,criminal_name)
        form = AddCriminalForm(n, request.FILES)
        if form.is_valid():
            form.save()
            obj = CriminalDetails.objects.all()
            count = len(obj)
            context = {'obj': obj, 'count': count,'form':form}
            return redirect('add')
    else:
        form = AddCriminalForm()
        obj = CriminalDetails.objects.all()
        count = len(obj)
        context = {'obj': obj, 'count': count, 'form': form}
    return render(request,"police/criminal.html",context)
def add(request):
    return render(request,"police/add.html")
def new_home(request):
    obj = CriminalDetails.objects.all()
    count = len(obj)
    context = {'obj': obj, 'count': count}
    return render(request,"police/new_home.html",context)
def search(request):
    return render(request,"police/search.html")
def search_criminal(request):
    S_Cid = request.POST.get('S_Cid', 'default')
    print(S_Cid)
    obj=CriminalDetails.objects.get(cid=S_Cid)
    print(obj.cid)
    # m,n= code.init("C:\\Users\\Hp\\PycharmProjects\\cLook\\cLook\\media\\" + str(obj.photo))
    # obj.status=m
    # obj.social_media_id=n
    # obj.save()
    # print(m,n)
    context={'obj':obj}
    return render(request,"police/search_criminal.html",context)