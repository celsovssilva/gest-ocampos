from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm as UserRegistrationForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def home(request):
    return render(request, 'campo/home.html', {})

def paginagestor(request):
    return render(request, 'campo/paginagestor.html', {})


def register(request):
   return render(request, 'campo/register.html')

def login(request):
 
 if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('campo:user'))
        else:
            return render(request, 'campo/login.html', {'error': 'Credenciais inválidas'})
        
def user(request):
    if request.user.is_authenticated:
        return render(request, 'campo/user.html', {'user': request.user})
    else:
        return redirect(reverse('campo:login'))
    
         