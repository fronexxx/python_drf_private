from apps.pizza_shop.models import PizzaShopModel
from core.models import BaseModel
from django.db import models

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    size = models.IntegerField()
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
