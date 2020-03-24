"""serwisrowerowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients_base import views
from django.contrib.auth import views as auth_views
from accounts.views import login_view, logout_view

urlpatterns = [
    path('login/', auth_views.auth_login, name='login'),
    path('logout/', auth_views.auth_logout, name='logout'),
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('comments/', views.comments, name='comments'),
    path('new_client/', views.new_client, name='new_client'),
    path('new_bike/', views.new_bike, name='new_bike'),
    path('new_servis/', views.new_servis, name='new_servis'),
    path('clients/<int:client_id>', views.client, name='client'),
    path('clients/bike/<int:bike_id>', views.bike, name='bike'),
    path('clients/servis/<int:servis_id>', views.servis, name='servis'),
    path('accounts/login/', login_view, name='login'),
    #path('accounts/register/', register_view),
    path('accounts/logout/', logout_view, name='logout'),
]
