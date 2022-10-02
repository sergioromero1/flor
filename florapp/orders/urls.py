from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("status/<str:status>/",views.IndexView.as_view(), name="index"),
    path("<int:pk>/",views.DetailView.as_view(), name="detail"),
    path("new/",views.CreateOrderView.as_view(), name="new"),
    path("prueba/",views.prueba, name="prueba"),
    path("product/",views.load_product, name="product")
]
