from django.contrib import admin
from .models import (
    BlogActualite,
    Category,
)



@admin.register(BlogActualite)
class BlogActualiteAdmin(admin.ModelAdmin):
    list_display        = ('title', 'published','created_on','author')
    list_editable       = ('published',)
    search_fields       = ('title','content')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
