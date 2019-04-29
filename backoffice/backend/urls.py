from backend import views
# from .models import GCAAffaire
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "backend"
router = DefaultRouter()
urlpatterns = [
    path('affaires/', views.GCAAffaireList.as_view(), name='affaires'),
    path('contacts/', views.GCAContactList.as_view(), name='contacts'),
    path('users/', views.GCAUserList.as_view(), name='users'),
    path('affaires/<int:pk>', views.GCAAffaireSingleView.as_view()),
    path('contacts/<int:pk>', views.GCAContactSingleView.as_view()),
    path('users/<int:pk>', views.GCAUserSingleview.as_view()),
    path('rest-auth/login/', views.GCALoginView.as_view(), name='login'),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('rest_framework.urls')),
    path('test/', views.test_request),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view),

]


urlpatterns += router.urls
