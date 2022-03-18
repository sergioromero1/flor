from multiprocessing import context
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from orders.models import Order
from orders.forms import OrderForm
from django.shortcuts import render



class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = "orders/index.html"
    context_object_name = "context"

    def get_queryset(self):
        """Return the last  published orders"""
        user = self.request.user
        context = {}
        context['latest_orders_list'] = Order.objects.filter(user=user)
        if 'status' in self.kwargs:
            status = self.kwargs['status']
            context[f'{status}'] = status
            context['latest_orders_list'] =Order.objects.filter(user=user).filter(status=status)
            return context
        context['todas'] = 'todas'
        return context

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Order
    template_name = "orders/detail.html"

    def get_queryset(self):
        user = self.request.user 
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

def prueba(request):
    return render(request,"orders/prueba.html")

def prueba2(request):
    return render(request,"orders/prueba2.html")
