from django.urls import path
from .views import EmailObtainTokenPairView

urlpatterns = [
    path("login", EmailObtainTokenPairView.as_view(), name="login"),
]
