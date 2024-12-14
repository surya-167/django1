from django.shortcuts import render

# Create your views here.


def login(request):
    print("FROM 7")
    return render(request, "login.html")