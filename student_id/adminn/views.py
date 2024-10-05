from django.shortcuts import redirect, render, get_object_or_404
from students.models import Users, Users_profile
from django.contrib.auth import authenticate, login, logout


def register_admin(request):
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
    students = Users.objects.filter(is_superuser=False)
    return render(request, 'adminn/admin_dashboard.html', {'students': students})


def student_details(request, id):
    student = Users.objects.get(id=id)
    pic = get_object_or_404(Users_profile, user=student)
    id_expiration = request.POST.get('id_expiration')
    if request.method == 'POST':
        student.id_expires = id_expiration
        student.save()
        return redirect('adminn:dashboard')
    return render(request, 'adminn/student_details.html', {'student': student, 'pic':pic})


def logout_admin(request):
    logout(request)
    return redirect('adminn:login')
def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('adminn:dashboard')