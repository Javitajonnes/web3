from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,
                          verbose_name="Nombre Categoria")
    created=models.DateTimeField(auto_now_add=True,
                                 verbose_name="F.creacion")
    updated=models.DateTimeField(auto_now=True,
                                 verbose_name="F.Actualizacion")
    class Meta():
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.name  
    
class MakeOrder(models.Model):
    header=models.CharField(max_length=30, verbose_name="Titulo")
    detail=models.TextField(verbose_name="Detalle")
    published=models.DateTimeField(default=now,
                                   verbose_name="F.Orden")
    image=models.ImageField(upload_to="ordenIMG",
                            null=True,blank=True,
                            verbose_name="Imagen")
    author=models.ForeignKey(User,on_delete=models.CASCADE,
                             verbose_name="Autor")
    categories=models.ManyToManyField(Category, verbose_name="Categorias")
    created=models.DateTimeField(auto_now_add=True,
                                 verbose_name="F.creacion")
    updated=models.DateTimeField(auto_now=True,
                                 verbose_name="F.Actualizacion")
    class Meta():
        verbose_name="Orden"
        verbose_name_plural="Ordenes"

    def __str__(self):
        return self.header




