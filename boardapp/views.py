from django.shortcuts import render

def home_view(request):
    return render (request, 'boardapp/home.html')

def dashboard(request):
    return render (request, 'boardapp/dashboard.html')

def boardlist(request):
    return render (request, 'boardapp/boardlist.html')

def boarddetail(request):
    return render (request, 'boardapp/boarddetails.html')