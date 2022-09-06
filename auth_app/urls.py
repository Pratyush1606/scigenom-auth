from django.urls import path
from auth_app import views

app_name = 'auth_app'
urlpatterns = [
    path("hello", views.Hello.as_view(), name="hello"),
]