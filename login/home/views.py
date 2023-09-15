from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth #importing user
from django.contrib import messages
from .models import Inventory
from .forms import BookingForm
from .forms import formupdation
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def index(request):
    if 'username' in request.session:
        return render(request,'index.html') 
    return redirect(login)

def about(request):
    if 'username' in request.session:
        return render(request,'about.html')
    return redirect(login)

def register(request): #REGISTER REQUEST
        if request.method == 'POST':
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                 if User.objects.filter(username=username).exists():
                      messages.info(request,'Username not available!')
                      return redirect(register)
                 elif User.objects.filter(email=email).exists():
                      messages.info(request,'email entered has an existing account please login to access!')
                      return redirect(register)
                 else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      user.set_password(password)
                      user.is_staff=True
                      user.save()
                      messages.success(request,'Account created succesfully')
                      return redirect('login')

            else:
             messages.info(request,'Passwords does not match')
             return redirect(register)
        else:
             return render(request,"register.html")
        

@user_passes_test(lambda u:u.is_superuser,login_url='home')
def adminedit(request): #ADMIN ADD USER REQUEST
        if request.method == 'POST':
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            username=request.POST["username"]
            email=request.POST["email"]
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                 if User.objects.filter(username=username).exists():
                      messages.info(request,'Username not available!')
                      return redirect(register)
                 elif User.objects.filter(email=email).exists():
                      messages.info(request,'email entered has an existing account please login to access!')
                      return redirect(register)
                 else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      user.set_password(password)
                      user.is_staff=True
                      user.save()
                      messages.success(request,'Account created succesfully')
                      return redirect('adminpanel')

            else:
             messages.info(request,'Passwords does not match')
             return redirect(register)
        else:
             return render(request,"adminedit.html")
        

             
def login(request):  #LOGIN REQUEST
     if 'username' in request.session:
        return redirect(index)
     elif request.method == 'POST': 
          username =request.POST['username'] 
          password = request.POST['password'] 
          user = auth.authenticate(username=username, password=password)
          if user is not None: 
               request.session['username'] = username 
               auth.login(request, user) 
               return redirect('home')
          else: 
               messages.info(request,'Invalid Username or Password') 
               return redirect('login') 
     else: 
          return render(request, 'login.html')



def inventory(request):
    dict_inv = {
        'inventory' :Inventory.objects.all()
    }
    if 'username' in request.session:
        return render(request,'inventory.html',dict_inv)
    return redirect(login)
    

def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form = BookingForm()
    dict_form ={
        'form':form
    }
    if 'username' in request.session:
        return render(request,'booking.html',dict_form)
    return redirect(login)
    

def contact(request):
    if 'username' in request.session:
        return render(request,'contact.html')
    return redirect(login)

    


def logout(request):  #LOGOUT REQUEST
     if 'username' in request.session:
         request.session.flush()
    
     return redirect('login')


@user_passes_test(lambda u:u.is_superuser,login_url='home')
def adminpanel(request):
    if 'username' in request.session:
        dict_user={
            'userdetails':User.objects.all().order_by('id')
        }
        return render(request,'adminpanel.html',dict_user)
        
    return redirect(login)

def SearchName(request): 
    searched=request.GET['search']
    searchnames=User.objects.filter(username__icontains=searched)
    return render(request,'adminpanel.html',{'userdetails':searchnames})


def updateuser(request,id):
    if request.method =='POST':
        query1= User.objects.get(pk=id)
        query2= formupdation(request.POST,instance=query1)
        if query2.is_valid():
            query2.save()
            messages.info(request,'Edit successful')
            return redirect(adminpanel)
    else:
        query1 = User.objects.get(pk=id)
        query2 = formupdation(instance=query1)
    return render(request,'updateuser.html',{'form':query2})


def deleteuser(request,id):
    if request.method =='POST':
        userdelete=User.objects.get(pk=id)
        userdelete.delete()
    messages.info(request,'Deleted successfully')    
    return redirect('adminpanel')

