"""
Views for handling admin functionalities within the adminn app.

This module includes views to manage the registration, login, dashboard, and user management 
for admins. Each view is responsible for rendering templates, processing form data, 
and handling redirections based on the request method and the outcome of database operations.

Imports:
    - redirect, render, get_object_or_404: Django shortcuts for redirecting, rendering templates, and fetching objects.
    - Users, Users_profile: Models from students.models to handle user and profile data.
    - authenticate, login, logout: Django auth functions to manage user authentication, login, and logout.

Functions:
    - register_admin(request): Handles admin registration, creating a superuser if valid data is provided.
    - login_admin(request): Authenticates and logs in a user as an admin if the credentials are valid.
    - admin_dashboard(request): Renders the dashboard page, listing all non-superuser students.
    - student_details(request, id): Displays and updates details of a specific student, including setting ID expiration.
    - logout_admin(request): Logs out the current admin user and redirects to the login page.
    - delete_user(request, id): Deletes a user by ID and redirects back to the dashboard.
"""

from django.shortcuts import redirect, render, get_object_or_404
from students.models import Users, Users_profile
from django.contrib.auth import authenticate, login, logout


def register_admin(request):
    """
    Handles the registration of a new admin user.

    If the request method is POST, it collects data from the form, checks if the username 
    already exists or if the passwords match, and either redirects back to the registration 
    page or creates a new superuser and redirects to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the registration template for GET requests or redirects 
        for POST requests based on form validation.
    """
    if request.method == 'POST':
        uname = request.POST.get('uname')
        name = request.POST.get('name')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if Users.objects.filter(mat_number=uname).exists() or password != cpassword:
            print('redirect')
            return redirect('adminn:register')
        else:
            user = Users.objects.create(
                mat_number=uname, name=name, password=password, is_superuser=True, is_staff=True)
            user.set_password(password)
            user.save()
            return redirect('adminn:login')
    return render(request, 'adminn/admin_registration.html')


def login_admin(request):
    """
    Handles the login of an admin user.

    Authenticates the user based on the provided credentials. If the user is a superuser, 
    they are logged in and redirected to the dashboard; otherwise, they are redirected 
    to the student login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the login page for GET requests or redirects based on 
        authentication results for POST requests.
    """
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(mat_number=uname, password=password)
        if user is not None:
            if user.is_superuser:
                print(user.id)
                login(request, user)
                return redirect('adminn:dashboard')
            else:
                return redirect('student:login')
        else:
            print('Login rejected')
            return redirect('adminn:login')
    return render(request, 'adminn/admin_home.html')


def admin_dashboard(request):
    """
    Renders the admin dashboard with a list of students.

    Fetches all users who are not superusers and displays them on the dashboard page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the admin dashboard template with the list of students.
    """
    students = Users.objects.filter(is_superuser=False)
    return render(request, 'adminn/admin_dashboard.html', {'students': students})


def student_details(request, id):
    """
    Displays and updates details of a specific student.

    Fetches the student and their profile picture based on the provided ID. If the request 
    method is POST, updates the student's ID expiration date and saves the changes.

    Args:
        request: The HTTP request object.
        id: The ID of the student.

    Returns:
        HttpResponse: Renders the student details template or redirects to the dashboard 
        after updating the student's information.
    """
    student = Users.objects.get(id=id)
    pic = get_object_or_404(Users_profile, user=student)
    id_expiration = request.POST.get('id_expiration')
    if request.method == 'POST':
        student.id_expires = id_expiration
        student.save()
        return redirect('adminn:dashboard')
    return render(request, 'adminn/student_details.html', {'student': student, 'pic': pic})


def logout_admin(request):
    """
    Logs out the current admin user.

    Calls Django's logout function and redirects the user to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Redirects to the login page after logging out.
    """
    logout(request)
    return redirect('adminn:login')


def delete_user(request, id):
    """
    Deletes a user by their ID and redirects to the admin dashboard.

    Args:
        request: The HTTP request object.
        id: The ID of the user to be deleted.

    Returns:
        HttpResponse: Redirects to the admin dashboard after deleting the user.
    """
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('adminn:dashboard')