from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.conf.urls import url, include
from .views import( posts_detail_view,
    posts_list_view, posts_create_view)


urlpatterns = [
    path('',views.index,name="home"),
    path('accounts/signup/',views.sign_up,name="sign-up"),
	url(r'^index2/$', views.index2, name='loggedin'),
	url(r'^login/$',views.login_view,name="login"),
	url(r'^posts/$', posts_list_view, name='posts_list_view'),
    url(r'^posts/(?P<url>\S+)/$', posts_detail_view, name='posts_detail_view'),
    url(r'^create/$', posts_create_view, name='posts_create_view'),

]
