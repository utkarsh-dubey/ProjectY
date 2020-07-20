
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app1.urls")),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', view = LogoutView.as_view(), name='logout', kwargs={'next_page' : '/'}),
#    auth_views.LogoutView.as_view(template_name = 'logout.html')

]
