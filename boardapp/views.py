from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.db.models import Sum
from django.db.models import Q

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
    flyers = Flyer.objects.filter(board=boards)
    # flyers = Flyer.objects.all()

    # pagination
    paginator = Paginator(flyers, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'boards' : boards,
        'flyers': flyers,
        'page_obj': page_obj,    
    }
    return render (request, 'boardapp/boarddetails.html', context)

# Flyers
@login_required
def flyerlist(request):
    flyers = Flyer.objects.all()

    paginator = Paginator(flyers, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'flyers' : flyers,
        'page_obj': page_obj,
    }
    return render (request, 'boardapp/flyers/flyers.html', context)


@login_required
def add_flyer(request):
    form = AddFlyerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("boardapp:flyers")
    context = {
        'form': form,
    }
    return render (request, 'boardapp/flyers/add_flyer.html', context)

@login_required
def flyer_detail(request, id):
    flyer = Flyer.objects.get(id=id)
    total_boards = Board.objects.filter(flyer=flyer.id)
    print(total_boards)

    lists = list(total_boards)
    print(lists)

    context = {
        'flyer' : flyer,
        # 'total_boards': total_boards,  
    }

    return render(request, 'boardapp/flyers/flyer_detail.html', context)


@login_required
def editflyer(request, id):
    flyer = Flyer.objects.get(id=id)
    form = AddFlyerForm(request.POST or None, instance=flyer)
    if request.method == 'POST':
        form = AddFlyerForm(request.POST or None, request.FILES or None, instance=flyer)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "I saved it successfully")
            return redirect('boardapp:flyers')
    context = {
        'form' : form, 
    }

    return render(request, 'boardapp/flyers/edit-flyer.html', context)


@login_required
def search(request):
    if 'q' in request.GET and request.GET['q']:
        messages.error(request, 'You searched for: %r' % request.GET['q'])
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q))
        flyer = Flyer.objects.filter(multiple_q)
        context = {
            'flyer': flyer ,
        }
        return render (request, 'boardapp/search.html', context ) 
    else:
        messages.error(request, "Please type something")
    return render (request, 'boardapp/search.html' , )
    
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

