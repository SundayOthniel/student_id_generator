from io import BytesIO
from django.shortcuts import redirect, render, get_object_or_404
from .models import Users, Users_profile
from django.contrib.auth import authenticate, login, logout
from PIL import Image
from django.core.files.base import ContentFile
import os
from django.conf import settings


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        address = request.POST.get('address')
        lga = request.POST.get('lga')
        mat_number = request.POST.get('matric')
        pob = request.POST.get('pob')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        state = request.POST.get('state')
        dpt = request.POST.get('dpt')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = Users.objects.create(name=name, place_of_birth=pob, sex=sex, date_of_birth=dob,
                                        address=address, state=state, city=city, lga=lga, mat_number=mat_number, dpt=dpt, password=password)
            default_img_path = os.path.join(settings.BASE_DIR, 'students', 'static', 'default-avatar.jpg')
            default_img = Image.open(default_img_path)
            buffer = BytesIO()
            default_img.save(buffer, format='JPEG')
            pic_data = ContentFile(buffer.getvalue(), 'default_profile_picture.png')

            # Create the Users_profile for the new user
            Users_profile.objects.create(user=user, profile_picture=pic_data)
            user.set_password(password)
            user.save()
            return redirect('student:login')
        else:
            return redirect('student:register')
    return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        mat_number = request.POST.get('matric')
        password = request.POST.get('password')
        user = authenticate(username=mat_number, password=password)
        if user is not None:
            if not user.is_superuser:
                print(user.id)
                login(request, user)
                return redirect('student:dashboard')
            else:
                return redirect('adminn:login')
        else:
            print('Login not allowed')
            return redirect('student:login')
    return render(request, 'home.html')


def dashboard(request):
    user = request.user
    if user.is_authenticated:
        img = get_object_or_404(Users_profile, user=request.user)
        if request.method == "POST":
            file = request.FILES.get('picture')
            if file:
                crop_img = Image.open(file)
                crop_width = 500
                crop_height = 500
                left = (crop_width - crop_width) / 2
                upper = (crop_height - crop_height) / 2
                right = (crop_width + crop_width) / 2
                lower = (crop_height + crop_height) / 2
                cropped_img = crop_img.crop((left, upper, right, lower))
                buffer = BytesIO()
                cropped_img.save(buffer, format='PNG')
                pic_name = f'{user} profile_picture.png'
                pic_data = ContentFile(buffer.getvalue(), pic_name)
                Users_profile.objects.update_or_create(user=user,  defaults={'profile_picture': pic_data})
                return redirect('student:dashboard') 
    return render(request, 'student_dashboard.html', {'user': user, 'img':img})

def details(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        address = request.POST.get('address')
        lga = request.POST.get('lga')
        mat_number = request.POST.get('matric')
        pob = request.POST.get('pob')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        state = request.POST.get('state')
        dpt = request.POST.get('department')

        # user update
        user.name = name
        user.sex = sex
        user.address = address
        user.lga = lga
        user.mat_number = mat_number
        user.place_of_birth = pob
        user.date_of_birth = dob
        user.city = city
        user.state = state
        user.city = city
        user.dpt = dpt
        user.save()
        return redirect('student:dashboard')
    if request.user.is_authenticated:
        img = get_object_or_404(Users_profile, user=request.user)
    else:
        return redirect('login')
    return render(request, 'student_details.html', {'user': user, 'img':img})

def logout_user(request):
    logout(request)
    return redirect('student:login')

