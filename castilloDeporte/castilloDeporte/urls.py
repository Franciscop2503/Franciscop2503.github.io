"""castilloDeporte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from core.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registro', views.register, name='register'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    #path('carrito/', views.cart, name='carrito'),
    path('products/', ProductListView.as_view(), name='products'),
    path('productos/', include('core.urls')),
    path('categoryC/', views.categoryC, name='categoryC'),
    path('categoryM/', views.categoryM, name='categoryM'),
    # path('productos/', include('core.urls')),
    #path('carrito/', views.cart, name='cart'),
    path('carrito/', include('core.urls')),
    path('agregar', views.add, name='add'),

    
    #dashboards cliente

    #dashboards cliente agregar

    path('aggdirec/', views.aggdirec, name='aggdirec'),
    path('aggmetod/', views.aggmetod, name='aggmetod'),

    #dashboards cliente editar

    path('editdirec/', views.editdirec, name='editdirec'),
    path('editmetod/', views.editmetod, name='editmetod'),
    path('editprofi/', views.editprofi, name='editprofi'),
   
   #dashboards cliente inhabilitar cuenta

    path('inhabili/', views.inhabili, name='inhabili'),

    #dashboards cliente metodos de pago

    path('metods/', views.metods, name='metods'),

    #dashboards cliente compras

    path('buys/', views.buys, name='buys'),

    #dashboards cliente direcciones

    path('adress/', views.adress, name='adress'),

    #dashboards cliente principal

    path('clientprinc/', views.clientprinc, name='clientprinc'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)