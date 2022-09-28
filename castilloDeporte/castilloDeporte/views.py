import imp
from logging import PlaceHolder
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
#from django.contrib.auth.models import User
from users.models import User
from .forms import RegisterForm
from core.models import Product
from core.utils import get_or_create_cart



def index(request):

    return render(request, 'index.html', {
        
    })



def login_view(request):
    # if request.user.is_autenticated:
    #     return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

    

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(email=email, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, 'Bienvenido {}'.format(user.email))
#             return redirect('index')
#         else: 
#             messages.error(request, 'Usuario o contraseña incorrectos')
#     return render(request, 'login.html',{

#     })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

def register(request):
    # if request.user.is_autenticated:
    #     return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'registro.html', {
        'form': form
    })

# def cart(request):
#     return render(request, 'cart.html', {

#     })
    
def products(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'Productos.html', {
        'message': 'Listado de productos',
        'name': 'Productos',
        'core': products,
    })

def categoryM(request):
    return render(request, 'CategoriaHombres.html', {
        #context
    })

def categoryC(request):
    return render(request, 'CategoriaNiños.html', {
        #context
    })
    
def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)

    return render(request, 'Productos.html', {
        'product' : product
    })

# def starts(request):
#     return render(request, 'login.html', {
#         #context
#     })

#dashboards

#dashboards cliente

#dashboards cliente agregar

def aggdirec(request):
    return render(request, 'dashboardClienteAgregarDireccion.html', {
        #context
    })

def aggmetod(request):
    return render(request, 'dashboardClienteAgregarMetodo.html', {
        #context
    })

#dashboards cliente editar

def editdirec(request):
    return render(request, 'dashboardClienteEditarDireccion.html', {
        #context
    })

def editmetod(request):
    return render(request, 'dashboardClienteEditarMetodo.html', {
        #context
    })

def editprofi(request):
    return render(request, 'dashboardClienteEditarPerfil.html', {
        #context
    })

#dashboards cliente inhabilitar cuenta

def inhabili(request):
    return render(request, 'dashboardClienteInhablitar.html', {
        #context
    })

#dashboards cliente metodos de pago

def metods(request):
    return render(request, 'dashboardClienteMetodosPago.html', {
        #context
    })

#dashboards cliente compras

def buys(request):
    return render(request, 'dashboardClienteMisCompras.html', {
        #context
    })

#dashboards cliente direcciones

def adress(request):
    return render(request, 'dashboardClienteMisDirecciones.html', {
        #context
    })

#dashboards cliente principal

def clientprinc(request):
    return render(request, 'dashboardClientePrincipal.html', {
        #context
    })



