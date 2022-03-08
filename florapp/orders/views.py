from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from orders.models import  Flower, Order
from orders.forms import OrderForm



class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = "orders/index.html"
    context_object_name = "latest_orders_list"

    def get_queryset(self):
        """Return the last  published orders"""
        user = self.request.user    
        return Order.objects.filter(user=user)

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Order
    template_name = "orders/detail.html"

    def get_queryset(self):
        user = self.request.user 
        qs = user.order_set
        return Order.objects.filter(user=user)

class CreateOrderView(LoginRequiredMixin, generic.CreateView):
    """Create new Order"""

    form_class = OrderForm
    success_url = reverse_lazy('orders:index')
    template_name = 'orders/new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


