from re import search
from django.contrib import admin

from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'flower', 'units', 'status')
    list_display_links = ('id', 'user')
    search_fields = (
        'id',
        'user__username',
        'flower__name',
        'status'
    )

