import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import json
# Create your views here.
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        res = json.loads(request.body.decode('UTF-8'))
        print(res)
        username = res['email']
        password = res['password']
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return JsonResponse({"resp":"success"},status=200)
        else:
            print("Not Found")
            messages.success(request,"There was error while logging in...")
            return JsonResponse({"resp":"failure"},status=200)
    return render(request,'user/login.html',{
        "messages":messages
    })

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        res = json.loads(request.body.decode('UTF-8'))
        username = res['username']
        email = res['email']
        password = res['password']
        user = authenticate(request,username=email,password=password)
        if user is None:
            newuser = User.objects.create_user(email,email,password)
            newuser.first_name = username
            newuser.save()
            return JsonResponse({"resp":"success"},status=200)
        else:
            print("failure")
            return JsonResponse({"resp":"failure"},status=200)
    return render(request,'user/register.html')