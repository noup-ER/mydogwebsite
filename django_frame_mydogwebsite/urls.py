"""django_frame_mydogwebsite URL Configuration

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
from django.urls import path
from django.shortcuts import HttpResponse
from methods import getmysql
from methods import getnews
import json

def getuserdate(request):
    sql = "select * from userdata"
    res = getmysql.getsql("localhost","root",3306,"test",sql,"search")
    data = {}
    res = json.loads(res)
    for i in res:
        data[i[0]] = i[1]
    return HttpResponse(json.dumps(data))

def adduserdata(request):
    account = request.GET['account']
    pw = request.GET['pw']
    email = request.GET['email']
    qq = request.GET['qq']
    mobile = request.GET['mobile']
    sql = "insert into userdata values (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(account,pw,email,qq,mobile)
    getmysql.getsql("localhost", "root", 3306, "test", sql,"add")
    return HttpResponse("ok")

def getwbtitlenews(request):
    return HttpResponse(json.dumps(getnews.getweibonews()))

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'getuserdate/', getuserdate),
    path(r'adduserdata/',adduserdata),
    path(r'gwtn/',getwbtitlenews)
]
