from django.views import generic
from .models import  Order


# Create your views here.
class IndexView(generic.ListView):
    template_name = "orders/index.html"
    context_object_name = "latest_orders_list"

    def get_queryset(self):
        """Return the last  published orders"""    
        return Order.objects.all()

class DetailView(generic.DetailView):
    model = Order
    template_name = "orders/detail.html"

    def get_queryset(self):
        return Order.objects.all()