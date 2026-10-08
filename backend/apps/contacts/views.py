from rest_framework import generics, status
from rest_framework.response import Response

from apps.contacts.models import ContactModel
from apps.contacts.serializer import ContactSerializer


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

    def delete(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except ContactModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'details' : 'user has been deleted'}, status=status.HTTP_204_NO_CONTENT)
