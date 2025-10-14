from django.contrib import admin
from .models import Category,MakeOrder

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class MakeOrderAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('header','published','author')
    ordering=('published','author')
    search_fields=('header','author__username')

admin.site.register(Category,CategoryAdmin)
admin.site.register(MakeOrder,MakeOrderAdmin)