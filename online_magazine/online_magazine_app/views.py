from django.shortcuts import render

def hello_everyone(request):
    return render(request, 'templates/hello.html',{})