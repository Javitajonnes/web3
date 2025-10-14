from django.contrib import admin 
from django.urls import path
from ot import views as views_ot

urlpatterns = [
    path('list/',views_ot.myorder,
         name="list"),
    path('admin/', admin.site.urls),
]
