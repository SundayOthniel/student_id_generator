"""
URL configuration for student_id project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for the project.

This module defines the URL patterns for the entire Django project, directing 
requests to the appropriate application views and handling the serving of static 
and media files.

- Includes URL patterns for the 'students' app and the 'adminn' app.
- Serves static files (CSS, JavaScript, images) during development using 
  Django's static files configuration.
- Serves media files (user-uploaded content) during development.

Attributes:
    urlpatterns (list): A list of URL patterns that map URLs to views.
"""

urlpatterns = [
    # Maps the root URL to the 'students' application URLs.
    path('', include('students.urls')),

    # Maps the 'admin/' URL to the 'adminn' application URLs.
    path('admin/', include('adminn.urls')),
]

# Serve static files during development.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
