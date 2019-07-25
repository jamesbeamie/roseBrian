from django.urls import path

from .views import (RegistrationAPIView, UserRetrieveUpdateAPIView,
    VerifyAPIView, LoginAPIView
)

app_name = "auth"

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('users/', RegistrationAPIView.as_view(), name="register"),
    path('users/verify/<token>', VerifyAPIView.as_view(), name='email-verify'),
    path('users/login/', LoginAPIView.as_view(), name="login"),
]