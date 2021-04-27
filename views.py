from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    messages.success(request,'This is about')
    return render(request,'home/about.html')
    
def contact(request):
    messages.success(request, 'welcome to contact')
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['content']
        print(name,phone,email,content)
        contact =Contact(name=name,email=email,phone=phone,content=content)
        Contact.save()
    return render(request,'home/contact.html')

def handleSignup(request):
    #get the parameters
    if request.method == 'POST':
        username=request.POST['username']
        fname =request.POST['fname']
        lname=request.POST['lname']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2=request.POST['pass2']
      #check for error inputs

        if len(username)>10:
         messages.error(request, 'username can be 10 characters')
         return redirect('home')
        if not username.isalnum:
          messages.error(request, 'username can be characters')
          return redirect('home')
        if pass1!=pass2:
          messages.error(request, 'passwords do not match')
          return redirect('home')
      #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your icoder  account has been succesfully created")
        return redirect('home')
    else:
        return HttpResponse('404-not found')
def handleLogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'successfully login')
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials please try again')    
            return redirect('home')

       
    
    return HttpResponse('404-not found')
def handleLogout(request):
    if request.method =='POST':
        logout(request)
        messages.success(request, 'succesfully logout')
        return redirect('home')
    

    