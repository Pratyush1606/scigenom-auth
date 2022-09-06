from django.urls import path
from auth_app import views

app_name = "auth_app"
urlpatterns = [
    path("signup", views.Signup.as_view(), name="signup"),
]
