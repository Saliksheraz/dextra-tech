from django.contrib.auth.decorators import permission_required, login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile


@permission_required('auth.add_user')
def register(request):
    all_permission = Permission.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            firstName = form.cleaned_data.get('firstName')
            secondName = form.cleaned_data.get('secondName')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('mobile')
            website = form.cleaned_data.get('website')
            insta = form.cleaned_data.get('insta')
            facebook = form.cleaned_data.get('facebook')

            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            gender = form.cleaned_data.get('gender')
            picture = form.cleaned_data.get('picture')

            user = form.save()
            user.is_active = False
            user.save()
            for eachPermission in all_permission:
                user.user_permissions.add(eachPermission)
            Profile.objects.create(user=user, phone=phone, address=address, gender=gender, picture=picture,
                                   firstName=firstName, secondName=secondName, email=email,
                                   mobile=mobile, website=website, insta=insta, facebook=facebook)
            messages.success(request,
                             f'Your Account is successfully created!!!, Please wait till you are authorized to LogIn')
            return redirect('homePage')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    userObj = request.user
    context = {'userObj': userObj}
    return render(request, 'users/profile.html', context)
