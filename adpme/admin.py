from django.contrib import admin
from .models import (
    BlogActualite,
    Category,
    ActualiteEnImage
)

class ActualiteEnImageInline(admin.TabularInline):
    model                   = ActualiteEnImage
    extra                   = 1
    can_delete              = True
    verbose_name            = "Image associée"
    verbose_name_plural     = "Image associées"
    show_change_link        = True

@admin.register(BlogActualite)
class BlogActualiteAdmin(admin.ModelAdmin):
    list_display        = ('title', 'published','created_on','date_publication','author')
    list_editable       = ('date_publication',)
    search_fields       = ('title',)
    inlines             = [ActualiteEnImageInline]

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)

