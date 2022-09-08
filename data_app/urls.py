from django.urls import path
from data_app import views

app_name = "data_app"
urlpatterns = [
    path(
        "add_usr_prof",
        views.AddData.as_view(data_id="user_profile"),
        name="add_usr_prof",
    ),
    path(
        "get_usr_prof",
        views.GetData.as_view(data_id="user_profile"),
        name="get_usr_prof",
    ),
    path(
        "add_usr_address",
        views.AddData.as_view(data_id="user_address"),
        name="add_usr_address",
    ),
    path(
        "get_usr_address",
        views.GetData.as_view(data_id="user_address"),
        name="get_usr_address",
    ),
]
