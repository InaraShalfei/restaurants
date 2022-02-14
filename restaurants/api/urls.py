from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PizzaViewSet, RestaurantViewSet

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet)
router.register('pizzas', PizzaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
