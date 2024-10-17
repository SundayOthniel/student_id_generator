"""
URL configuration for the adminn app.

This module defines the URL patterns for the admin-related views, such as login, registration, 
dashboard access, and user management. It maps URL paths to their corresponding view functions.

Imports:
    - path: A function from django.urls used to define URL patterns.
    - * (all views): Imports all views from the current app's views module.

Available routes:
    - '' : Login view for admins (name='login')
    - 'Register' : Registration view for admins (name='register')
    - 'Dashboard' : Dashboard view for admins (name='dashboard')
    - 'Logout/' : Logout view for admins (name='logout')
    - 'StudentDetails/<int:id>' : View to display details of a student by ID (name='student_details')
    - 'DeleteUser/<int:id>' : View to delete a user by ID (name='delete_user')

app_name: Specifies the app namespace as 'adminn' for URL namespacing.
"""

from django.urls import path
from .views import *

app_name = 'adminn'
urlpatterns = [
    path('', login_admin, name='login'),
    path('Register', register_admin, name='register'),
    path('Dashboard', admin_dashboard, name='dashboard'),
    path('Logout/', logout_admin, name='logout'),
    path('StudentDetails/<int:id>', student_details, name='student_details'),
    path('DeleteUser/<int:id>', delete_user, name='delete_user'),
]