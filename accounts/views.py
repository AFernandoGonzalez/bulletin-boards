from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from .models import CustomUser
from .forms import RegisterForm, UserForm, UserFormForEdit
from django.contrib.auth.models import User


def account_register(request):

    return render(request, 'accounts/registration/registration.html')

def user_register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("accounts:login")
    else:
        form = RegisterForm()

    return render(response, "accounts/registration/ambassador_registration.html", {"form":form})


# ##############
@login_required
def user_profile(request):
   
    return render(request, 'accounts/user_profile.html')

@login_required
def edit_details(request):
    user_form = UserFormForEdit(instance = request.user)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance = request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:user_profile')

    return render(request, 'accounts/edit_details.html', {
        "user_form": user_form,
    })

# # DELETE USER
@login_required
def delete_user(request):
    user = User.objects.get(email=request.user)
    # we are inactivating the user instead of deleting the whole user
    user.is_active = False
    user.save()
    logout(request)
    return redirect('accounts:delete_confirmation')
