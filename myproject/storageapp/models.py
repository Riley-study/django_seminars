from django.db import models
# Поля модели «Клиент»:
# — имя клиента # — электронная почта клиента
# — номер телефона клиента # — адрес клиента # — дата регистрации клиента

# Поля модели «Товар»:
# — название товара # — описание товара # — цена товара
# — количество товара # — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа # — дата оформления заказа

# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, default='89505555555')
    address = models.CharField(max_length=150)
    date_of_registry = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="New product")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.quantity} {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.client} {self.total_amount} {self.order_date}'

