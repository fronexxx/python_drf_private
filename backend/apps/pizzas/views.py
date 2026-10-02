from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.pizzas.models import PizzaModel
from apps.pizzas.serializer import PizzaSerializer


class PizzaListCreateView(ListCreateAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer


class PizzaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer


