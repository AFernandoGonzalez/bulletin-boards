from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required


# from .models import CustomUser
from .forms import UserForm, UserFormForEdit
from django.contrib.auth.models import User


def account_register(request):
    return render(request, 'accounts/registration/registration.html')

def owner_register(request):
    user_form = UserForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user = user_form.save(commit=False)
            new_user.user = new_user
            new_user.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect('accounts:login')

    return render(request, "accounts/registration/owner_registration.html", {
        "user_form": user_form,
    })

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
