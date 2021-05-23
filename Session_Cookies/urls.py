"""Session_Cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cookies.views import setcookie , homepage ,getcookie , delete_cookies , cookie_delete, cookie_session , demo_view, create_session, show_session, delete_session
from cookies.views import user_login, user_logout , welcome
from decorators import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setcookie/', setcookie, name= 'setcookie'),
    path('', homepage, name='homepage'),
    path('showcookie/', getcookie , name= 'showcookie'),
    path('deletecookies/', delete_cookies, name='deletecookies'),

    # Session

    path('testcookie/', cookie_session, name='testcookie'),
    path('deletecookie/', cookie_delete, name='deletecookie'),
    path('demo/', demo_view, name='demo'),
    path('create/', create_session, name='create'),
    path('show/', show_session, name='show'),
    path('delete/',delete_session, name='delete'),

    #Login

    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('welcome/',welcome, name='welcome'),

    #Decorators
    path('index/',views.index, name='index'),
    path('add/',views.add, name='add'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('remove/<int:id>/',views.remove, name='remove'),
    path('transfer/<int:id>/',views.transfer, name='transfer'),





]
