from django.db import models
from auth_app.models import User

# Create your models here.
class UserProfile(models.Model):
    user_id = models.OneToOneField(
        to=User, related_name="user_profile", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class UserAddress(models.Model):
    user_id = models.ForeignKey(
        to=User, related_name="user_address", on_delete=models.CASCADE
    )
    address = models.CharField(max_length=100)
