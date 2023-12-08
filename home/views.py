from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
# use @login here
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/login")
# Create your views here.
# def index(request):
# 	context = {
# 		"variable1" : "dev",
# 		"variable2" : "roy",
# 	}
# 	return render(request, 'index.html', context)
	#return HttpResponse("this is home page")
def about(request):
	return render(request, 'about.html')
	#return HttpResponse("this is about page")

def slippers(request):
	return render(request, 'slippers.html')
	#return HttpResponse("this is services page")
def sneakers(request):
	return render(request, 'sneakers.html')
	#return HttpResponse("this is services page")
def jordan(request):
	return render(request, 'jordan.html')
	#return HttpResponse("this is services page")
def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		desc = request.POST.get('desc')
		contact = Contact(name = name, phone = phone, email = email, desc = desc, date = datetime.today())
		contact.save()
		messages.success(request, "Profile details updated.")
	return render(request, 'contact.html')