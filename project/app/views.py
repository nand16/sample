from django.shortcuts import render
from app.forms import user_data_form, user_info_form
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,"app/index.html")

def register(request):
    r = False
    u = user_data_form()
    i = user_info_form()
    if request.method == 'POST':
        u = user_data_form(request.POST)
        i = user_info_form(request.POST)
        if u.is_valid() and i.is_valid():
            u1 = u.save()
            u1.set_password(u1.password)
            u1.save()
            print("u1 done")
            p1 = i.save(commit=False)
            p1.user_data = u1
            if 'profile_pic' in request.FILES:
                print("found an image")
                p1.profile_pic = request.FILES['profile_pic']
            p1.save()
            print("p1 is also ddone")
            r = True
        else:
            # print("errorrsssssssssss-------------------------")
            print(u.errors,i.errors)

    return render(request,"app/register.html",context={'user_d':u,'user_i':i,'r':r})

@login_required
def user_logout(request):
    logout(request)
    print("to log out !")
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        user = authenticate(request,username=u_name,password=p_word)
        print("finish authenticated")
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Not a active user")
        else:
            return HttpResponse("Not correct credentials !!!")
    else:
        return render(request,"app/login.html",{})
