from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pizza.models import PizzaModel
from apps.pizza.serializer import PizzaSerializer


class PizzaListCreateView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        pizzas = PizzaModel.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class PizzaRetrieveUpdateDestroyView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs['pk']
        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response({'details' : 'Not Found'}, status.HTTP_404_NOT_FOUND)

        serializer = PizzaSerializer(pizza)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            pizza = PizzaModel.objects.get(pk=pk)
        except PizzaModel.DoesNotExist:
            return Response({'details' : 'Not Found'}, status.HTTP_404_NOT_FOUND)

        data = self.request.data
        serializer = PizzaSerializer(pizza, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(args, **kwargs):
        pk = kwargs['pk']

        try:
            PizzaModel.objects.get(pk=pk).delete()
        except PizzaModel.DoesNotExist:
            return Response({'details' : 'Not Found'}, status.HTTP_404_NOT_FOUND)

        return Response({'details' : 'Deleted!'}, status.HTTP_204_NO_CONTENT)


