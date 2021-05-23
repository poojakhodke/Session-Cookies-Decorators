from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def setcookie(request):
    response = render(request, "cookies.html")
    if request.COOKIES.get('visits'):
        response.set_cookie('data', 'welcome back')
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the First time"
        response.set_cookie('visits', value)
        response.set_cookie('data', text)
    return response

def homepage(request):
    return render(request, "homepage.html")

def getcookie(request):
    # nm =request.COOKIE.get('name')
    # ag = request.COOKIE.get('age')
    return render(request, "showcookie.html")

def delete_cookies(request):
    response = redirect('homepage')
    response.delete_cookie('name')
    response.delete_cookie('age') 
    return response


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Welcome to Django Session</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        print("In delete cookie")
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

def demo_view(request):
    print(request.session.__dict__)
    return HttpResponse("In Demo View")


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    request.session['age'] = 25
    request.session['city'] = 'pune'
    print(request.session.__dict__)
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")

def show_session(request):
    return render(request, 'session.html')

def delete_session(request):
    del request.session['name']
    del request.session['password']
    del request.session['age']
    return render(request, 'session.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pword = request.POST.get("pswd")
        user_obj= authenticate(username = uname, password= pword)
        if user_obj:
            request.session["Dialogue"]= "You are Auth User"
            login(request, user_obj)
            #print(user_obj.__dict__, "User Objects")
            return redirect("welcome")
        else:
            return HttpResponse("Invalid Credentials...!")

    return render(request, 'login.html')
    # print(request.user)S
    # return HttpResponse("user Login")

# @login_required(login_url='login')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
    
@login_required
def welcome(request):
    return render(request, 'home.html')