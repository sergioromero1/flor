from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = "orders/index.html"
    context_object_name = "latest_orders_list"

    def get_queryset(self):
        """Return the last five published orders"""    
        context = ['Pedido 1', 'Pedido 2', 'Pedido 3']
        return context