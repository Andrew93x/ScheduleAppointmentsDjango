from django.http import request
from django.shortcuts import redirect, render
from list_appointments.models import CustomSettings, RolesUsers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render (request, 'index.html',{})

@login_required
def list_patients(request):
    #Query que devuelve los datos
    rol_users = RolesUsers.objects.all()
    return render(request, 'list.html', {'r_users':rol_users})


def login_view(request):
    if request.method == 'POST':
        username_ = request.POST['username']
        password_ = request.POST['password']
        user = authenticate(request, username = username_, password = password_)
        if user:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})
    
    return render(request, 'login.html',{})


def logout_view(request):
    logout(request)
    return redirect('login')

def get_list(request, _id):
    if request.method == 'GET':
        try:
            role_user = RolesUsers.objects.get(id = _id)
            response = json.dumps([{
                'Usuario': role_user.users.first_name, 
                'Rol': role_user.rol}])
        except:
            response = json.dumps([{
                'Error': 'Id usuario no esxiste'
            }])
        return HttpResponse(response, content_type = 'text/jason')

#Metodo para crear un usuario
def register(request):
    #Toma las varibales de register.hml y las almacena en la db
    return render(request, 'register.html')


def list_cs(request):
    custom_settings = CustomSettings.objects.all()
    return render(request, 'list.html', {'custom_settings':custom_settings})