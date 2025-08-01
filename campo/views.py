from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm as UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'campo/home.html', {})

def manager_dashboard(request):
    return render(request, 'campo/manager_dashboard.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(reverse('campo:login'))
    else:
        form = UserRegistrationForm()
        
    return render(request, 'campo/register.html', {'form': form})

def paginagestor(request):
    return render(request, 'campo/paginagestor.html', {})

def login(request):
    return render(request, 'campo/login.html', {})