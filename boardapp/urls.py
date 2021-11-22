from django.urls import path
from . import views

app_name = 'boardapp'


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('boards/', views.boardlist, name='boards'),
    path('board/<str:id>', views.boarddetail, name='board-detail'),
    # all flyers
    path('flyers/', views.flyerlist, name='flyers'),
    path('flyers/update/<int:id>/', views.editflyer, name='edit-flyer'),
    path('flyers/search/', views.search, name='search-flyer'),
    # all offices
    path('offices/', views.officelist, name='offices'),

    # Dashboard
    path('student_dashboard/', views.student_dashboard, name='student-dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager-dashboard'),
]