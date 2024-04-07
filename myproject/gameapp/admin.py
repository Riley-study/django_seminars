from django.contrib import admin
from .models import Coin

# Register your models here.

class CoinAdmin(admin.ModelAdmin):
    list_display = ('size',)

admin.site.register(Coin, CoinAdmin)

