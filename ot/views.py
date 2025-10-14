from django.shortcuts import render
from .models import Category, MakeOrder

def myorder(request):
    makeorder=MakeOrder.objects.all()
    return render(request,"ot/listaOrdenes.html",{'makeorder':makeorder})
