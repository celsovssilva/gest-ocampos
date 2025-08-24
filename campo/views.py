from email.headerregistry import Group
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm as UserRegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


def home(request):
    return render(request, 'campo/home.html', {})

def paginagestor(request):
    return render(request, 'campo/paginagestor.html', {})


def register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password_confirm')
        tipo = request.POST.get('tipo') 

       
        if password != password2:
            
            return render(request, 'campo/register.html', {'error': 'As senhas não coincidem'})
            
        try:
            
            user = User.objects.create_user(username=username, email=email, password=password)
            
          
            if tipo == 'gestor':
                gestor_group = Group.objects.get(name='Gestores')
                user.groups.add(gestor_group)
            elif tipo == 'usuario':
                usuario_group = Group.objects.get(name='Usuarios')
                user.groups.add(usuario_group)
            
          
            return redirect(reverse('login')) 
            
        except Exception as e:
            
            return render(request, 'campo/register.html', {'error': str(e)})

    
    return render(request, 'campo/register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        if user.groups.filter(name='Gestores').exists():
                return redirect(reverse('campo/paginagestor'))
        elif user.groups.filter(name='Usuarios').exists():
                return redirect(reverse('campo/user'))
  
    return render(request, 'campo/login.html')
        
def user(request):
    if request.user.is_authenticated:
        return render(request, 'campo/user.html', {'user': request.user})
    else:
        return redirect(reverse('campo:login'))
    
         