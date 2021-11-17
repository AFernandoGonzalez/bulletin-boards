from django.urls import path
from . import views

app_name = 'boardapp'


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('boards/', views.boardlist, name='boards'),
    path('board/1/', views.boarddetail, name='board-detail'),
]