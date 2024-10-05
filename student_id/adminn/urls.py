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
