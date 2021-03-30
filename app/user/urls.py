
from os import name
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import UserCreationAPIView, UserListView


class JwtTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['email'] = self.user.email
        data['username'] = self.user.username
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = JwtTokenObtainPairSerializer


urlpatterns = [
    path('user/', include('allauth.urls')),
    path('api/v1/user/sign-up/', UserCreationAPIView.as_view(), name='create_user'),
    path('api/v1/user/list-users/', UserListView.as_view(), name='user-list'),
    # jwt
    path('api/v1/token/', JwtTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += format_suffix_patterns(urlpatterns)
