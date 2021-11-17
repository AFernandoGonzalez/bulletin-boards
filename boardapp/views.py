from django.shortcuts import render

def home_view(request):
    return render (request, 'boardapp/home.html')

def dashboard(request):
    return render (request, 'boardapp/dashboard.html')

def student_dashboard(request):
    return render (request, 'boardapp/dashboard/student-dash.html')

def manager_dashboard(request):
    return render (request, 'boardapp/dashboard/manager-dash.html')

def boardlist(request):
    return render (request, 'boardapp/boardlist.html')

def boarddetail(request):
    return render (request, 'boardapp/boarddetails.html')