from django.shortcuts import render, HttpResponse, redirect
from .models import Password
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
import string 
import uuid 
import random

# Create your views here.
def home(request):
    return redirect('all_passwords')

@login_required
def update(request, id):
    update_pass = Password.objects.get(id=id)
    
    if update_pass.u_name == request.user:
        params = {'update_pass': update_pass}
        # return render(request, 'update.html', params)

    else:
        return redirect('all_passwords')

    if request.method == "POST":
        update_pass.u_name = request.user
        update_pass.site = request.POST['site']
        update_pass.site_name = request.POST['sitename']
        update_pass.uname_site = request.POST['uname_site']
        update_pass.pass_site = request.POST['pass_site']
        
        update_pass.save()

        messages.success(request, "Password Updated Successfully")
        return redirect('all_passwords')

    return render(request, 'update.html', params)

def signup(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['signupemail']
        password = request.POST['signuppassword1']
        password2 = request.POST['signuppassword2']

        # Checks for creating User
        if len(uname) < 3:
            messages.error(request, 'Username should be greater then 3')

        create_newuser = User.objects.create_user(uname, email, password2)
        create_newuser.first_name = fname
        create_newuser.last_name = lname
        create_newuser.save()
        messages.success(request, f'User {uname} created successfully, Go ahead and Login to your Account')

    return redirect('/')


def handle_login(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']    

        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f'Successfully Logged in as - {user}')
            return redirect('/')
        else:
            messages.error(request, 'No Such User exists')
            return redirect('/')
    else:
        messages.error(request, f'{user} Details dont Match the Database Please Try Agians')
        return redirect('/')

@login_required
def handle_logout(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    messages.success(request, f' Successfully Logged Out')
    return redirect('/')

@login_required
def all_passwords(request):

    if request.user.is_authenticated:
        user_pass = Password.objects.filter(u_name=request.user)
        params = {'user_pass': user_pass}

        return render(request, 'all_password.html', params)
    else:
        return redirect('/home#SignupModal')

@login_required
def add_password(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            u_name = request.user
            site = request.POST['site']
            sitename = request.POST['sitename']
            uname_site = request.POST['uname_site']
            pass_site = request.POST['pass_site']
            

            pass_object = Password.objects.create(u_name=u_name, site_name=sitename, site=site, uname_site=uname_site, pass_site=pass_site)
            pass_object.save()

            messages.success(request, "Password Successfully Created")
            
        return render(request, 'add_password.html')

    else:
        return redirect('/home')

@login_required
def delete(request, id):
    delete_pass = Password.objects.get(id=id)
    
    if delete_pass.u_name == request.user:
        delete_pass.delete()
    
    return redirect('all_passwords')