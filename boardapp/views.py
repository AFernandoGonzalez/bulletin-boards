from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

from .models import Board, Flyer, Office

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

# Flyers
@login_required
def flyerlist(request):
    flyers = Flyer.objects.all()
    context = {
        'flyers' : flyers
    }
    return render (request, 'boardapp/flyers/flyers.html', context)


# Flyers
@login_required
def officelist(request):
    offices = Office.objects.all()
    context = {
        'offices' : offices
    }
    return render (request, 'boardapp/offices/offices.html', context)

