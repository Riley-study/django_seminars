from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    # Настройка полей, которые будет видно в полном списке
    list_display = ('name', 'email', 'phone_number',)
    # Настройка полей, по которым можно фильтровать значения
    list_filter = ('name', 'email', 'phone_number')
    # Настройка полей, по которым можно будет искать значения
    search_fields = ('name', 'email', 'phone_number')
    # Настройка полей с разбивкой на подразделы
    fieldsets = [
        (
            None,
            {
                'fields': ['name'],
            },
        ),
        (
            'Контактные данные клиента',
            {
                'fields': ['email', 'phone_number', 'address'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_added',)
    list_filter = ('name', 'price', 'quantity', 'date_added',)
    search_fields = ('name', 'price', 'quantity', 'date_added',)
    fieldsets = [
        (
            None,
            {
                'fields': ['name'],
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description'],
            },
        ),
        (
            'На складе',
            {
                'fields': ['price', 'quantity', 'date_added'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date',)
    list_filter = ('client', 'total_amount', 'order_date',)
    search_fields = ('client', 'total_amount', 'order_date',)
    fields = ['client', 'products', 'total_amount', 'order_date', ]
    readonly_fields = ['order_date', ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
