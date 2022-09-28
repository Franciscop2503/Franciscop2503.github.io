from distutils.command.upload import upload
from itertools import product
from unicodedata import category
import decimal
import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    category = models.ManyToManyField(Category, blank=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

def set_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        slug = slugify(instance.name)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.name, str(uuid.uuid4())[:8])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0,max_digits=8, decimal_places=2)
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    FEE = 0.05

    def __str__(self):
        return self.cart_id

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    def update_subtotal(self):
        self.subtotal = sum([ product.price for product in self.products.all ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())



class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    identificacion = models.TextField(max_length=500, verbose_name='Descripción')
    fecha_naci = models.DateTimeField(verbose_name='fecha de nacimiento')
    


    def __sty__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']


def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_cart_id, sender=Cart)        