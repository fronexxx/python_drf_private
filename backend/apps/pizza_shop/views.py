from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.pizza.serializer import PizzaSerializer
from apps.pizza_shop.models import PizzaShopModel
from apps.pizza_shop.serializer import PizzaShopSerializer


class PizzaShopListCreateView(generics.ListCreateAPIView):
    queryset = PizzaShopModel.objects.all()
    serializer_class = PizzaShopSerializer

class PizzaShopAddPizzaView(generics.GenericAPIView):
    queryset = PizzaShopModel.objects.all()

    def post(self, *args, **kwargs):
        pizza_shop = self.get_object()
        print(pizza_shop, '?????????????????????????????')
        request: Request = self.request
        data = request.data
        print(data, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        serializer = PizzaSerializer(data=data)
        print(serializer, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)
        print(serializer, '))))))))))))))))))))))))))))))')
        shop_serializer = PizzaShopSerializer(pizza_shop)
        print(shop_serializer, '###########################')
        return Response(shop_serializer.data, status=status.HTTP_201_CREATED)



