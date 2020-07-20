from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from app1.forms import SignUpForm
from .forms import PostForm
from django.http import HttpResponseRedirect


#create view
@login_required(login_url='/accounts/login/')
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
@login_required(login_url='/accounts/login/')
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'index2.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
#@login_required
#def index2(request):
#    return render(request, 'index2.html')


def login_view(request):

    if(request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=form.get_user()
            login(request,user)
            return render(request,'index2.html')

        else:
            form=AuthenticationForm()
    else:
        form=AuthenticationForm()


    return render(request,'registration/login.html',{'form':form})

@login_required(login_url='/accounts/login/')
def index2(request):

    return render(request,'index2.html')
