from django.views import generic
from django.urls import reverse_lazy
from orders.models import  Order
from orders.forms import OrderForm


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

class CreateOrderView(generic.CreateView):
    """Create new Order"""

    form_class = OrderForm
    success_url = reverse_lazy('orders:index')
    template_name = 'orders/new.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

