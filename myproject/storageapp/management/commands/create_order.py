from django.core.management.base import BaseCommand
from storageapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create clients, products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='create order')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client.objects.get(id=i)
            product1 = Product.objects.get(id=i)
            product2 = Product.objects.get(id=i + 1)
            total_amount = product1.price + product2.price
            order = Order.objects.create(client=client, total_amount=total_amount)
            order.products.set([product1, product2])
            order.save()
