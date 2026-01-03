from django.contrib import admin
from .models import (
    CategorieActu,
    AgenceInfo,
    Actualite,
    ImageActualite,
)


class ImageActualiteInline(admin.TabularInline): # Ou admin.StackedInline pour un affichage différent
    model = ImageActualite
    extra = 1 # Nombre de formulaires vides à afficher par défaut pour ajouter de nouvelles images

@admin.register(CategorieActu)
class CategorieActuAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(AgenceInfo)
class AgenceInfoAdmin(admin.ModelAdmin):
    list_display = ('nom_agence','slogan','adresse','phone')


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display        = ('titre', 'date_publication','status','section')
    list_filter         = ('categorie','date_publication')
    search_fields       = ('titre','contenu')

