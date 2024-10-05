from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
  name = models.CharField(max_length=255)
  place_of_birth = models.CharField(max_length=255)
  sex = models.CharField(max_length=6)
  date_of_birth = models.DateField(auto_now_add=True, blank=True, null=True)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  lga = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  mat_number = models.CharField(max_length=255, unique=True)
  dpt = models.CharField(max_length=255)
  username = models.CharField(unique=False, max_length=255)
  id_expires = models.DateField(blank=True, null=True)
  
  USERNAME_FIELD = 'mat_number'
  REQUIRED_FIELDS = []

  class Meta:
        db_table = 'users'

  def __str__(self):
        return self.email
  
class Users_profile(models.Model):
    user = models.OneToOneField("Users", on_delete=models.CASCADE, to_field='mat_number', null=True)
    profile_picture = models.ImageField(blank=True)
    class Meta:
        db_table = 'profile_picture'

    def __str__(self):
        return self.user