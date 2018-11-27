from django.conf.urls import include, url
from .views import RegistrationAPIView, LoginAPIView

app_name = 'users'

urlpatterns = [
    url(r'^create/?$', RegistrationAPIView.as_view()),
    url(r'^login/?$', LoginAPIView.as_view()),
]