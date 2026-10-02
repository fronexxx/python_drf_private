from django.urls import path

from apps.pizza_shop.views import PizzaShopListCreateView, PizzaShopAddPizza

urlpatterns = [
    path('', PizzaShopListCreateView.as_view()),
    path('/<int:pk>/pizza', PizzaShopAddPizza.as_view())

]