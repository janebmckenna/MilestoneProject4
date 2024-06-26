from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'house_number', 'street', 'town_or_city',
              'county', 'country', 'postcode', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name', 'email',
                    'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
