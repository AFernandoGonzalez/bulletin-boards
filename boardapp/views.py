from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.db.models import Sum

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Board, Flyer, Office
from .forms import AddOfficeForm, FlyerPostedForm, AddFlyerForm

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
    flyers = Flyer.objects.filter(board=boards.id)

    context = {
        'boards' : boards,
        'flyers': flyers,   
    }
    return render (request, 'boardapp/boarddetails.html', context)

# Flyers
@login_required
def flyerlist(request):
    flyers = Flyer.objects.all()

    paginator = Paginator(flyers, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        searched = request.POST['searched']
        flyer = Flyer.objects.filter(name__contains=searched)

        context = {
            'flyer': flyer,
            'searched': searched, 
        }
        return render (request, 'boardapp/flyers/flyers.html', context)

    form = AddFlyerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("boardapp:flyers")

    context = {
        'form': form,
        'flyers' : flyers,
        # 'flyer' : flyer,
        'page_obj': page_obj,
    }
    return render (request, 'boardapp/flyers/flyers.html', context)

def editflyer(request, id):
    flyer = get_object_or_404(Flyer, id = id)
    form = AddFlyerForm(request.POST or None, instance = flyer)
    if form.is_valid():
        form.save()
        return redirect("boardapp:flyers")
 
    context= {
        'form': form
    }
    return render(request, "boardapp/flyers/edit-flyer.html", context)

# def search(request):
    
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         flyer = Flyer.objects.filter(name__contains=searched)
    
#         context = {
#             'flyer': flyer,
#             'searched': searched, 
#         }
#         return render (request, 'boardapp/search.html', context)
#     else:
#         return render (request, 'boardapp/search.html')

# Flyers
@login_required
def officelist(request):
    offices = Office.objects.all()

    form = AddOfficeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("boardapp:offices")

    context = {
        'form': form,
        'offices' : offices
    }
    return render (request, 'boardapp/offices/offices.html', context)

