from django.shortcuts import render, redirect
from .forms import UserForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer 

def show_home(request):
    if request.user.is_authenticated:
        return redirect('/welcome')

    msg = 'Welcome back!'

    if request.POST:
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('/welcome')
        else:
            msg = 'Invalid User Name'

    return render(request, 'index.html', {'status': msg})

def show_signup(request):
    if request.POST:
        obj = UserForm(request.POST)
        if obj.is_valid:
            obj.save()
            return redirect('/')
        else:
            return render(request,'signup.html',{'myform':obj})
    else:
        obj=UserForm()
        return render(request, 'signup.html', {'myform':obj})

@login_required(login_url='/')
def show_welcome(request):
    rows = Customer.objects.all()  
    return render(request, 'welcome.html', {'values': rows})

def logout_me(request):
    logout(request)
    return redirect('/')

def customer_new(request):
    if request.POST:
        frm = CustomerForm(request.POST, request.FILES)
        if frm.is_valid:
            frm.save()
            return redirect('/welcome')
    else:
        return render(request, 'customer.html', {'myform': frm})
    frm = CustomerForm()
    return render(request, 'customer.html', {'myform': frm})


