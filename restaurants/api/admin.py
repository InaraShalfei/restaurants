from django.contrib import admin

from .models import Restaurant, Pizza


class RestaurantAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class PizzaAdmin(admin.ModelAdmin):
    list_filter = ('name', 'restaurant', 'secret_ingredient')
    empty_value_display = '-пусто-'


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Pizza, PizzaAdmin)
