from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Defines custom models for user management, extending Django's built-in user model 
and providing a model for storing user profile pictures.

Classes:
    Users: Extends AbstractUser to include additional fields such as name, place of birth, 
           and other user-specific information.
    Users_profile: Stores profile pictures for each user, linked through a OneToOne relationship.
"""

class Users(AbstractUser):
    """
    Represents a custom user model extending Django's AbstractUser.

    Attributes:
        name (str): The full name of the user.
        place_of_birth (str): The place where the user was born.
        sex (str): The gender of the user (e.g., 'Male' or 'Female').
        date_of_birth (date): The user's date of birth.
        address (str): The address of the user.
        city (str): The city where the user resides.
        lga (str): The local government area of the user.
        state (str): The state where the user resides.
        mat_number (str): The unique matriculation number of the user, used as the username.
        dpt (str): The department of the user.
        username (str): Username for the user, not used as the login identifier.
        id_expires (date): The expiration date of the user's ID.
        
    Meta:
        db_table (str): The name of the database table for this model ('users').
        
    Methods:
        __str__(): Returns a string representation of the user, displaying their email.
    """
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
        """
        Returns a string representation of the user.
        
        Returns:
            str: The email address of the user.
        """
        return self.email


class Users_profile(models.Model):
    """
    Represents a user's profile picture, linked to a Users object through a OneToOne relationship.

    Attributes:
        user (ForeignKey): A OneToOneField linking to a Users object, using the 'mat_number' field.
        profile_picture (ImageField): Stores the profile picture of the user.
        
    Meta:
        db_table (str): The name of the database table for this model ('profile_picture').
        
    Methods:
        __str__(): Returns a string representation of the user profile.
    """
    user = models.OneToOneField("Users", on_delete=models.CASCADE, to_field='mat_number', null=True)
    profile_picture = models.ImageField(blank=True)

    class Meta:
        db_table = 'profile_picture'

    def __str__(self):
        """
        Returns a string representation of the user profile.
        
        Returns:
            str: The matriculation number of the user.
        """
        return self.user
