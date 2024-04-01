from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Client, Order


# Create your views here.
def index(request):
    return HttpResponse('Wellcome to our store!')


def list_of_products(request, id_client, period):
    lst = []
    client = get_object_or_404(Client, pk=id_client)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period)
    start_date_only = start_date.date()

    if client is not None:
        orders = Order.objects.filter(client=client)
        for order in orders:
            if order.order_date > start_date_only:
                products = order.products.all()
                for prod in products:
                    lst.append(prod)
    context = {'client': client.name,
               'period': period,
               'list_of_products': lst}
    return render(request, 'list_of_products.html', context)
