from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

from .models import Board

def home_view(request):
    return render (request, 'boardapp/home.html')

@login_required
def dashboard(request):
    return render (request, 'boardapp/dashboard.html')

@login_required
def student_dashboard(request):
    return render (request, 'boardapp/dashboard/student-dash.html')

@login_required
def manager_dashboard(request):
    return render (request, 'boardapp/dashboard/manager-dash.html')

# Boards
@login_required
def boardlist(request):
    boards = Board.objects.all()
    context = {
        'boards' : boards
    }
    return render (request, 'boardapp/boardlist.html', context)

@login_required
def boarddetail(request, id):
    boards = Board.objects.get(id=id)
    # count


    context = {
        'boards' : boards
    }
    return render (request, 'boardapp/boarddetails.html', context)