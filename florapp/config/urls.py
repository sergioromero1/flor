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
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from orders import views
from users import views as users_views

urlpatterns = [
    path('', views.load_index, name='index'),
    path('about-us/', views.load_aboutus, name='about_us'),
    path('blog/', views.load_blog, name='blog'),
    path('cart/', views.load_cart, name='cart'),
    path('checkout/', views.load_checkout, name='checkout'),
    path('compare/', views.load_compare, name='compare'),
    path('contact-us/', views.load_contactus, name='contact_us'),
    path('error-404/', views.load_error_404, name='error-404'),
    path('FAQ/', views.load_faq, name='faq'),
    path('login/', users_views.LoginView.as_view(), name='login'),
    path("logout/",users_views.LogoutView.as_view(), name="logout"),
    path('my_account/', views.load_myaccount, name='my_account'),
    path('register/', users_views.SignUpView.as_view(), name='register'),
    path("shop/",views.load_shop, name="shop"),
    path('whislist/', views.load_whislist, name='whislist'),
    path('admin/', admin.site.urls),
    path('orders/', include("orders.urls")),
    path('users/', include("users.urls"))

]

handler404 = "orders.views.load_error_404"