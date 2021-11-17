from django.urls import path
from . import views

app_name = 'boardapp'


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('boards/', views.boardlist, name='boards'),
    path('board/1/', views.boarddetail, name='board-detail'),

    # Dashboard
    path('student_dashboard/', views.student_dashboard, name='student-dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager-dashboard'),
]