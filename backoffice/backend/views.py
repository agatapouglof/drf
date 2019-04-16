from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from .models import GCAAffaire
from .serialier import GCAAffaireSerializer


class GCAAffaireList(generics.ListAPIView):
    queryset = GCAAffaire.objects.all()
    serializer_class = GCAAffaireSerializer
