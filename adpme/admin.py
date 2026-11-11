from django.contrib import admin
from .models import (
    AgenceInfo,
    BlogActualite,
    Category,
    ActualiteEnImage,
    FAQ, Discours
)

@admin.register(AgenceInfo)
class AgenceInfoAdmin(admin.ModelAdmin):
    list_display = ('nom_agence', 'email_contact', 'phone', 'adresse')
    fieldsets = (
        ('Identité', {
            'fields': ('nom_agence', 'slogan')
        }),
        ('Contenu institutionnel', {
            'fields': ('mission', 'vision', 'valeurs')
        }),
        ('Coordonnées', {
            'fields': ('adresse', 'phone', 'whatsapp', 'email_contact', 'horaires', 'carte_embed_url')
        }),
        ('Réseaux sociaux', {
            'description': 'Format JSON : {"facebook": "https://...", "linkedin": "https://..."}',
            'fields': ('liens_sociaux',)
        }),
    )

    def has_add_permission(self, request):
        # Une seule entrée autorisée
        return not AgenceInfo.objects.exists()


class ActualiteEnImageInline(admin.TabularInline):
    model                   = ActualiteEnImage
    extra                   = 1
    can_delete              = True
    verbose_name            = "Image associée"
    verbose_name_plural     = "Image associées"
    show_change_link        = True

@admin.register(BlogActualite)
class BlogActualiteAdmin(admin.ModelAdmin):
    list_display        = ('title', 'published','created_on','date_publication','author','category')
    list_editable       = ('date_publication',)
    search_fields       = ('title',)
    inlines             = [ActualiteEnImageInline]

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display        = ('ordre', 'question', 'active')
    list_editable       = ('ordre', 'active')
    list_display_links  = ('question',)
    ordering            = ('ordre',)

@admin.register(Discours)
class DiscoursAdmin(admin.ModelAdmin):
    list_display    = ('get_type_discours_display', 'nom_auteur', 'fonction', 'date_maj')
    fieldsets = (
        ('Identité', {
            'fields': ('type_discours', 'nom_auteur', 'fonction', 'photo')
        }),
        ('Contenu', {
            'fields': ('extrait', 'contenu_complet')
        }),
    )

    def get_type_discours_display(self, obj):
        return obj.get_type_discours_display()
    get_type_discours_display.short_description = "Type"


