from django.shortcuts import render

def hello_everyone(request):
    return render(request, 'templates/home.html',{})

def register(request):
    return render(request,'templates/register.html',{})