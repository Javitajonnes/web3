from django.db import models

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
