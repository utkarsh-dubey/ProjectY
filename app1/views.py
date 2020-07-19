from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'index2.html')
    context['form']=form
    return render(request,'registration/signup.html',context)
#@login_required
#def index(request):
#    return render(request, 'index2.html')


