import json
from rest_framework import status
from .forms import NewUserForm, UserSignUpForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact
from django.contrib.auth import authenticate, login
from .serializers import contactSerializer
from django.shortcuts import render,redirect
import requests
from .models import *


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = contactSerializer(contact)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = contactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def get_post_contact(request):
    if request.method == 'GET':
        user = Contact.objects.all()
        serializer = contactSerializer(user, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'mobile': int(request.data.get('mobile')),
            'email': request.data.get('email'),
            'address': request.data.get('address')
        }
        serializer = contactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def get_delete_update_home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'home.html')
@api_view(['GET', 'POST'])
def get_post_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            Contact = form.save()
            return redirect('home.html')
        else:
            print("Form unsaved")


    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form':form})
@api_view(['GET', 'POST'])
def get_database(request):
    users = Contact.objects.all()
    return render(request, "database.html", {'User':users})
@api_view(['GET', 'POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return Response(reverse('home'))
            else:
                print("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            #return render("Invalid login details given")
    else:
        return render(request, 'login.html', {})


@api_view(['GET', 'POST'])
def get_about(request):
    users = Contact.objects.all()
    return render(request, "api/v1/About.html", {'User':users})
