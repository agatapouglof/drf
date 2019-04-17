from backend import views
from .models import GCAAffaire
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = "backend"
router = DefaultRouter()
urlpatterns = [
    path('affaires/', views.GCAAffaireList.as_view(), name='affaires'),
    path('users/', views.GCAUserList.as_view(), name='users'),
    #path('rest-auth/login/', views.GCALoginView.as_view(), name='login'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),

]


urlpatterns += router.urls