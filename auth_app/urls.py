from django.urls import path
from auth_app import views

app_name = "auth_app"
urlpatterns = [
    path("signup", views.SignUp.as_view(), name="signup"),
]
