"""florapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from orders import views

urlpatterns = [
    path('', views.load_index, name='index'),
    path('about-us/', views.load_aboutus, name='about_us'),
    path('contact-us/', views.load_contactus, name='contact_us'),
    path('blog/', views.load_blog, name='blog'),
    path('FAQ/', views.load_faq, name='faq'),
    path('login/', views.load_login, name='login'),
    path('register/', views.load_register, name='register'),
    path('my_account/', views.load_myaccount, name='my_account'),
    path('admin/', admin.site.urls),
    path('orders/', include("orders.urls")),
    path('users/', include("users.urls"))

]
