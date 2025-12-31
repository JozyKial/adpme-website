from django.contrib import admin
from .models import (
    AgenceInfo,
    MembreEquipe,
    CategorieActualite,
    Actualite,
    CategorieDocument,
    Document,
    MessageContact,
    PageStatique,
    Partenaire,
    ImageActualite,
)


class ImageActualiteInline(admin.TabularInline): # Ou admin.StackedInline pour un affichage différent
    model = ImageActualite
    extra = 1 # Nombre de formulaires vides à afficher par défaut pour ajouter de nouvelles images

@admin.register(CategorieActualite)
class CategorieActualiteAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(CategorieDocument)
class CategorieDocumentAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(AgenceInfo)
class AgenceInfoAdmin(admin.ModelAdmin):
    list_display = ('nom_agence','slogan','adresse','phone')


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display        = ('titre', 'date_publication', 'est_publie')
    list_filter         = ('categorie','est_publie','date_publication')
    prepopulated_fields = {'slug' : ('titre',)}
    search_fields       = ('titre','contenu')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display    = ('titre','categorie','date_publication')
    list_filter     = ('categorie',)


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display    = ('nom','email','sujet','date_envoi','lu')
    list_filter     = ('lu',)
    search_fields   = ('nom','email','sujet')


@admin.register(PageStatique)
class PageStatiqueAdmin(admin.ModelAdmin):
    list_display        = ('titre',)
    prepopulated_fields = {'slug':('titre',)}


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nomPartenanire',)


@admin.register(MembreEquipe)
class MembreEquipeAdmin(admin.ModelAdmin):
    list_display    = ('nom', 'fonction')

