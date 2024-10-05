from django.urls import path
from students import views

app_name='student'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('Register/', views.register, name='register'),
    path('Dashboard/', views.dashboard, name='dashboard'),
    path('Details/<int:id>', views.details, name='details'),
    path('Logout/', views.logout_user, name='logout'),
]
