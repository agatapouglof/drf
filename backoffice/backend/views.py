from rest_auth.views import LoginView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GCAAffaire, GCAUser, GCAContact
from .serializer import GCAAffaireSerializer, GCAUserSerializer, GCAContactSerializer

from rest_auth.registration.views import RegisterView


class GCAAffaireList(generics.ListCreateAPIView):

    queryset = GCAAffaire.objects.all()
    serializer_class = GCAAffaireSerializer

class GCAAffaireSingleView(generics.RetrieveUpdateDestroyAPIView):

    queryset = GCAAffaire.objects.all()
    serializer_class = GCAAffaireSerializer


class GCAContactList(generics.ListCreateAPIView):
    queryset = GCAContact.objects.all()
    serializer_class = GCAContactSerializer

class GCAContactSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GCAContact.objects.all()
    serializer_class = GCAContactSerializer


class GCAUserList(generics.ListCreateAPIView):

    queryset = GCAUser.objects.all()
    serializer_class = GCAUserSerializer

class GCAUserSingleview(generics.RetrieveUpdateDestroyAPIView):
    queryset = GCAUser.objects.all()
    serializer_class = GCAUserSerializer


@api_view(['GET','POST'])
def test_request(request, fornat=None):
    print("get the data in test daniel")
    return Response('test')

# class GCALoginView(LoginView):
#
#     def get_response(self):
#         orginal_response = super().get_response()
#         mydata = {"status": "success"}
#         orginal_response.data.update(mydata)
#         return orginal_response


class CustomRegisterView(RegisterView):
    queryset = GCAUser.objects.all()
