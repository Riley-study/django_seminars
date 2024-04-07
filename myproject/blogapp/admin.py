from django.contrib import admin
from .models import Author


# Register your models here.
@admin.action(description='Rename')
def action_admin_rename(modeladmin, request, queryset):
    queryset.update(first_name='New name!!')


class AuthorAdmin(admin.ModelAdmin):
    # Настройка полей, которые будет видно в полном списке эксземпляров
    list_display = ('first_name', 'second_name', 'birthday',)
    # Настройка полей, по которым можно фильтровать значения
    list_filter = ('first_name',)
    # Настройка полей, по которым можно будет искать значения
    search_fields = ('first_name', 'second_name',)
    # Настройка полей, которые будет видно, когда проваливаемся в экземпляр класса
    # fields = ['first_name', 'second_name', 'birthday']
    # Настройка полей, которые нельзя менять
    # readonly_fields = ['second_name']

    # Настройка полей с разбивкой на подразделы (список списков/кортежей
    # [название подаздела, словарь {что редактируем (поле): как редактируем (какие поля входят)}])
    fieldsets = [
        (
            'ФИО автора',
            {
                'fields': ['first_name', 'second_name'],
            },
        ),
        (
            'Биография',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['biography'],
            },
        ),
        (
            'День рождения',
            {
                'fields': ['birthday'],
            }
        ),
    ]
    # Добавить action переименовать по имени
    actions = [action_admin_rename]

admin.site.register(Author, AuthorAdmin)
