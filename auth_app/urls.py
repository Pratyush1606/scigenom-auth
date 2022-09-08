from django.urls import path
from auth_app import views
from rest_framework_simplejwt import views as jwt_views

app_name = "auth_app"
urlpatterns = [
    # JWT Authentication APIs
    path(
        "api/token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token-verify", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path("signup", views.Signup.as_view(), name="signup"),
]
