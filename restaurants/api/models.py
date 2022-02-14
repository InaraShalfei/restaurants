from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=128, blank=False)
    address = models.CharField(max_length=128, blank=False)

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=128, blank=False)
    cheese = models.CharField(max_length=128, blank=True)
    pastry = models.CharField(max_length=128, blank=True)
    secret_ingredient = models.CharField(max_length=128, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='pizzas')

    class Meta:
        verbose_name = 'pizza'
        verbose_name_plural = 'pizzas'

    def __str__(self):
        return f'{self.name} с секретным ингредиентом {self.secret_ingredient}'
