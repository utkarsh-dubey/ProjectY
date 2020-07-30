from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from app1.forms import SignUpForm
from .forms import PostForm,CommentForm,Goingform,UserUpdateForm,ProfileUpdateForm
from django.http import HttpResponseRedirect
from .filters import PostFilter
from django.contrib import messages
from .forms import ContactForm, NameForm
#create view
@login_required(login_url='/accounts/login/')
def posts_create_view(request):

    form= PostForm(request.POST or None,initial={'user':request.user.username })


    if request.method == "POST":
        if form.is_valid():

            form.save()
        return HttpResponseRedirect("/posts/")



    context= {'form': form,
              }

    return render(request, 'posts-create-view.html', context)



@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts' : posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)



#list view
@login_required(login_url='/accounts/login/')
def posts_list_view(request):

    allposts= Post.objects.all()
    myFilter = PostFilter(request.GET, queryset=allposts )
    allposts = myFilter.qs

    context= {'allposts': allposts,'myFilter': myFilter
              }

    return render(request, 'posts-list-view.html', context)

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
        if post.category=="others":
            display.append(post)

    context= {"allposts": display,
              }

    return render(request, 'others.html', context)
#detail view
def posts_detail_view(request, url=None):

    post= get_object_or_404(Post, url=url)
    goings= post.goings.filter(active=True)
    impcheck=True
    for i in goings:

        if i.name==request.user.username:

            impcheck=False
            break

    new_goings=None
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)
        if impcheck:

            going_form = Goingform(data=request.POST)
            if going_form.is_valid():
                if request.POST.get('going',False)!='False':

                    new_goings=going_form.save(commit=False)
                    new_goings.post=post
                    new_goings.save()
                else:
                    pass
        else:

            going_form=[]
            new_goings=True


        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
        if not impcheck:
            new_goings=True
            going_form=[]
        else:
            going_form=Goingform()


    context= {'post': post,
              }

    return render(request, 'posts-detail-view.html', {'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form,'goings':goings,'new_goings':new_goings,'going_form':going_form})

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
            return render(request, 'index.html')
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
            return render(request,'index.html')

        else:
            form=AuthenticationForm()
    else:
        form=AuthenticationForm()


    return render(request,'registration/login.html',{'form':form})


@login_required
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = NameForm(request.POST)
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !')
    else:
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        form = NameForm(request.POST)

    context= { 'u_form':u_form,
                'p_form':p_form,
                'user':user,
                'form':form
            }
    return render(request, 'accounts/profile.html', context)

def home_view(request):

    display = []
    allposts= Post.objects.all()

    myFilter = PostFilter(request.GET, queryset=allposts )
    allposts = myFilter.qs

    for post in allposts:
        if post.location=="online" or post.location == request.user.profile.location:
            display.append(post)

    context= {'allposts': display,'myFilter': myFilter,
              }

    return render(request, 'posts2.html', context)
