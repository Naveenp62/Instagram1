from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from insta.models import post
# Create your views here.
def loginV(request):
    if request.user.is_authenticated:
        messages.warning(request,"Ochinav bro already!")
        return redirect('homepage')
    #logout(request)
    if request.method=="POST":
        a=request.POST.get('ip1')
        b=request.POST.get('ip2')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            print(a,b,type(result))
            login(request,result)
            messages.success(request,"Namasthe mawa !")
            return redirect('homepage')
        else:
            messages.error(request,"Bokal iruguthay bidda ! password chusko")
            return redirect('loginpage')
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
@login_required(login_url="/admin")
def create(request):
    if request.method=="POST":
        image=request.FILES['image']
        capt=request.POST.get('cap')
        obj=post(user=request.user,photo=image,caption=capt)
        obj.save()
    return render(request,'create.html')
def home(request):
    objs=post.objects.all()
    if request.method=="POST":
        a=request.POST.get('search')
        results=post.objects.filter(caption__icontains=a)
        return render(request,'index.html',{'posts':results})
    return render(request,'index.html',{'posts':objs})
@login_required(login_url='loginpage')
def profile(request):
    if request.user.is_superuser:
        print(request.user.username)
        return redirect('/admin')

    return render(request,'profile.html')
def register(request):
    if request.user.is_authenticated:
        messages.warning(request,"Man you already have an account !")
        return redirect('homepage')
        
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        print(fname,lname,passw,cpass,email,uname)

        #validation username
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists !")
            return redirect('loginpage')
        #validation for password
        if len(passw)<8:
            messages.error(request,"Password must be 8 chars")
            return redirect('registerpage')
        #validation for cpass
        if (cpass!=passw):
            messages.error(request,"Passwords doest match")
            return redirect('registerpage')
        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=passw)
        obj.save()
        messages.success(request,"Hey your account is ready, Login now")
        return redirect('loginpage')

    return render(request,'register.html')
def logoutV(request):
    logout(request)
    messages.success(request,"Ochinav bro already!")
    return redirect('loginpage')