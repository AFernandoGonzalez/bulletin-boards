from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404


from django.db.models import Sum
from django.db.models import Q

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
    try:
        f = Flyer.objects.get(id=id)
    except Flyer.DoesNotExist:    
        f = None
    
    flyers = Flyer.objects.filter(board=boards).filter(removed=False)   

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

def history(request):
    return render (request, 'boardapp/flyers/history.html')

# Flyers
# @login_required
def flyerlist(request):
    flyers = Flyer.objects.all().filter(removed=False)
    # total_boards = Board.objects.filter(flyers=flyers).count()

    paginator = Paginator(flyers, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'flyers' : flyers,
        'page_obj': page_obj,
        # 'total_boards': total_boards,
    }
    return render (request, 'boardapp/flyers/flyers.html', context)


@login_required
def add_flyer(request):
    if request.method == 'POST':
        current_user = Flyer(added_by=request.user)
        form = AddFlyerForm(request.POST or None, request.FILES or None, instance=current_user)
        
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user  # User posting the form
            new_form.save()
            
        return redirect("boardapp:flyers")
    else:
        form = AddFlyerForm()
        context = {
            'form': form,
        }
    return render (request, 'boardapp/flyers/add_flyer.html', context)

# @login_required
def flyer_detail(request, id):
    flyer = Flyer.objects.get(id=id)
    print(flyer)
    total_boards = Board.objects.filter(flyer=flyer.id).count()


    context = {
        'flyer' : flyer,
        'total_boards': total_boards,  
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


# Removed Flyers

def removed(request):
    flyers = Flyer.objects.filter(removed=True)
    

    paginator = Paginator(flyers, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'flyers' : flyers,
        'page_obj': page_obj,
        
    }
    return render (request, 'boardapp/flyers/removed.html', context)





# Search Flyers

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
        messages.error(request, "Please type your flyer name")

    return render (request, 'boardapp/search.html' , )




# Offies
@login_required
def officelist(request):
    offices = Office.objects.all()

    paginator = Paginator(offices, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'form': form,
        'offices' : offices,
        'page_obj':page_obj,
    }
    return render (request, 'boardapp/offices/offices.html', context)



# form = AddOfficeForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect("boardapp:offices")










# handling errors
def custom_page_not_found_view(request, exception):
    return render(request, "boardapp/error/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "boardapp/error/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "boardapp/error/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "boardapp/error/400.html", {})