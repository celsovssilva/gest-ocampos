from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'campo/home.html', {})

def manager_dashboard(request):
    return render(request, 'campo/manager_dashboard.html', {})