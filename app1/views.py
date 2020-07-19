from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


#create view
def posts_create_view(request):
    form= PostForm(request.POST or None)
    

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/posts/")

    
    
    context= {'form': form,
              }
    
    return render(request, 'posts-create-view.html', context)



#list view
def posts_list_view(request):

    allposts= Post.objects.all()
    
    context= {'allposts': allposts,
              }
    
    return render(request, 'posts-list-view.html', context)


#detail view
def posts_detail_view(request, url=None):

    post= get_object_or_404(Post, url=url)


    
    
    context= {'post': post,
              }
    
    return render(request, 'posts-detail-view.html', context)

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
#def index2(request):
#    return render(request, 'index2.html')


