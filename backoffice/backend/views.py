from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response
from rest_auth.views import LoginView



from .models import GCAAffaire, GCAUser
from .serializer import GCAAffaireSerializer, GCAUserSerializer


class GCAAffaireList(generics.ListAPIView):

    queryset = GCAAffaire.objects.all()
    serializer_class = GCAAffaireSerializer


class GCAUserList(generics.ListAPIView):

    queryset = GCAUser.objects.all()
    serializer_class = GCAUserSerializer

# class GCALoginView(LoginView):
#
#     def get_response(self):
#         orginal_response = super().get_response()
#         mydata = {"status": "success"}
#         orginal_response.data.update(mydata)
#         return orginal_response


