from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
#from app1.forms import SignUpForm
from .forms import PostForm, UserForm
from django.http import HttpResponseRedirect
from django.utils import timezone
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


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form' : form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts' : posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)



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

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')

    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

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


def basketball_view(request):

    allposts= Post.objects.all()

    context= {'allposts': allposts,
              }

    return render(request, 'basketball.html', context)

def pubg_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="pubg":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'pubg.html', context)

def cod_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="cod":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'callofduty.html', context)

def cricket_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="cricket":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'cricket.html', context)

def football_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="football":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'football.html', context)

def fifa_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="fifa":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'fifa.html', context)

def nba_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="nba":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'nba.html', context)

def skribbl_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="skribbl":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'skribbl.html', context)

def ludo_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="ludo":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'ludo.html', context)

def fortnite_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="fortnite":
            display.append(post)

    context= {"fortnite": display,
              }

    return render(request, 'fortnite.html', context)

def uno_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="uno":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'uno.html', context)

def others_view(request):

    display = []
    allposts= Post.objects.all()
    for post in allposts:
        if post.category=="cricket":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'cricket.html', context)
#detail view

#def sign_up(request):
 #   if request.method == 'POST':
  #      form = SignUpForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
     #       user.refresh_from_db()  # load the profile instance created by the signal
      #      user.profile.email = form.cleaned_data.get('email')
       #     user.profile.first_name = form.cleaned_data.get('first_name')
        #    user.profile.last_name = form.cleaned_data.get('last_name')
         #   user.save()
          #  raw_password = form.cleaned_data.get('password1')
           # user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            #return render(request, 'index2.html')
   # else:
    #    form = SignUpForm()
    #return render(request, 'registration/signup.html', {'form': form})
#@login_required
#def index2(request):
#    return render(request, 'index2.html')


