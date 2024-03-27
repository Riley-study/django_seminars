from django.core.management.base import BaseCommand
from myproject.storageapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create clients, products and orders."


# def handle(self, *args, **kwargs):
#     for i in range(5):
#         for j in range(10):
#             client = Client(name=f'Client{i}', email=f'client{i}@example.com', address=f'street{i}, home{i + 5}')
#             product = Product()
#
#             client.save()
#
#             self.stdout.write(f'{client}')
