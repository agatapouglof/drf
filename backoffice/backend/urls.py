from backend import views
from .models import GCAAffaire
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = "backend"
router = DefaultRouter()
urlpatterns = [
    path('affaires/', views.GCAAffaireList.as_view(), name='affaires'),
]


urlpatterns += router.urls