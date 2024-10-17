from django.urls import path
from students import views

"""
Defines URL patterns for the 'student' application, mapping various routes to view functions.

Each path in this list is linked to a corresponding view that handles a specific aspect 
of the user experience, such as registration, login, accessing the dashboard, 
viewing or updating user details, and logging out.

Attributes:
    app_name (str): A namespace for the student app's URLs, used for namespacing.
    urlpatterns (list): A list of URL patterns that maps URLs to view functions.
"""

app_name = 'student'

urlpatterns = [
    path('', views.login_user, name='login'),
    """
    Maps the root URL ('') to the 'login_user' view.
    
    URL: '/'
    View: login_user
    Name: 'login'
    Description: Handles the login functionality for users.
    """,
    
    path('Register/', views.register, name='register'),
    """
    Maps the 'Register/' URL to the 'register' view.
    
    URL: '/Register/'
    View: register
    Name: 'register'
    Description: Handles user registration and displays the registration form.
    """,
    
    path('Dashboard/', views.dashboard, name='dashboard'),
    """
    Maps the 'Dashboard/' URL to the 'dashboard' view.
    
    URL: '/Dashboard/'
    View: dashboard
    Name: 'dashboard'
    Description: Displays the user's dashboard and handles profile picture updates.
    """,
    
    path('Details/<int:id>', views.details, name='details'),
    """
    Maps the 'Details/<int:id>' URL to the 'details' view, allowing for dynamic user ID.
    
    URL: '/Details/<int:id>'
    View: details
    Name: 'details'
    Description: Displays and updates user details for the given user ID.
    """,
    
    path('Logout/', views.logout_user, name='logout'),
    """
    Maps the 'Logout/' URL to the 'logout_user' view.
    
    URL: '/Logout/'
    View: logout_user
    Name: 'logout'
    Description: Logs out the user and redirects them to the login page.
    """
]
