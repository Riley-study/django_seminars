from django.core.management.base import BaseCommand
from storageapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create clients, products and orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Create clients and products')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Client{i}', email=f'cl{i}@mail.com', address=f'street {i}')
            product = Product(name=f'prod{i}', description=f'very good prod {i}', price=50 + i, quantity=i)
            client.save()
            product.save()
            #
            # for j in range(1, count + 1):
            #     set_of_products = set(product,)
            #     order = Order(client=client, products=set_of_products, total_amount=50 + i)
            #     order.save()
