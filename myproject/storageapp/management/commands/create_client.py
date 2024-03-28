from django.core.management.base import BaseCommand
from storageapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com', address='street 1')
        client.save()
        self.stdout.write(f'{client}')
