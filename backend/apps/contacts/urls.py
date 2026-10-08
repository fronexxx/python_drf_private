from django.urls import path

from apps.contacts.views import ContactListCreateView, ContactRetrieveUpdateDestroyView

urlpatterns = [
    path('', ContactListCreateView.as_view()),
    path('/<int:pk>', ContactRetrieveUpdateDestroyView.as_view()),
]