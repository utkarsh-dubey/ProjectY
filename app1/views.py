from django.shortcuts import render

def index(request):
    a=0
    return render(request,"index.html")
