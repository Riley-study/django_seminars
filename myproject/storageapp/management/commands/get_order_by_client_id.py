from django.core.management.base import BaseCommand
from storageapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Get all orders by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            orders = Order.objects.filter(client=client)
            products_list =[]
            for order in orders:
                prod = str(order.products)
                products_list.append(prod)
            intro = f'All orders of {client}\n'
            all_orders = '\n'.join(str(prod for prod in products_list) for order in orders)
            self.stdout.write(f'{intro}{all_orders}')
