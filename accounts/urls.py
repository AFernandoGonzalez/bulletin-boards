from django.urls import path
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

from . import views
from .forms import UserLoginForm

app_name = 'accounts'

urlpatterns = [

    # auth
    path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html', redirect_authenticated_user=True, form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/registration/logout.html'), name='logout'),
    # registration
    path('register/', views.account_register, name='register'),
    path('register/owner/', views.owner_register, name='register-owner'),
    
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/',  views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="accounts/delete_confirm.html"), name='delete_confirmation'),

]
