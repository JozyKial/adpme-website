# ==========================================================================
# ADPME Congo — admin.py — v3
# Interface d'administration (thème Unfold aux couleurs de l'ADPME).
# Toutes les classes héritent de unfold.admin.ModelAdmin pour profiter du
# nouveau design. Le menu latéral se règle dans settings.py (UNFOLD).
# ==========================================================================
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import (
    AgenceInfo,
    BlogActualite,
    Category,
    ActualiteEnImage,
    FAQ, Discours,
    Slide, Programme, Parcours, ParcoursLien, ChiffreCle, Partenaire,
    Page, Antenne, Document, BlocAccueil,
    TexteSite, Element,
)
from .textes import defaut


def apercu_image(champ, hauteur=48):
    """Petite vignette dans la liste de l'admin."""
    def apercu(self, obj):
        image = getattr(obj, champ)
        if image:
            return format_html('<img src="{}" style="height:{}px;width:auto;border-radius:6px;">', image.url, hauteur)
        return "—"
    apercu.short_description = "Aperçu"
    return apercu


# ==========================================================================
# Utilisateurs et groupes (formulaires au style Unfold)
# ==========================================================================
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UtilisateurAdmin(BaseUserAdmin, ModelAdmin):
    form                 = UserChangeForm
    add_form             = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupeAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# ==========================================================================
# L'agence
# ==========================================================================
@admin.register(AgenceInfo)
class AgenceInfoAdmin(ModelAdmin):
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


@admin.register(Discours)
class DiscoursAdmin(ModelAdmin):
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


@admin.register(Antenne)
class AntenneAdmin(ModelAdmin):
    list_display  = ("nom", "ville", "telephone", "ordre", "actif")
    list_editable = ("ordre", "actif")


# ==========================================================================
# Actualités
# ==========================================================================
class ActualiteEnImageInline(TabularInline):
    model                   = ActualiteEnImage
    extra                   = 1
    can_delete              = True
    verbose_name            = "Image associée"
    verbose_name_plural     = "Images associées"
    show_change_link        = True


@admin.register(BlogActualite)
class BlogActualiteAdmin(ModelAdmin):
    list_display        = ('title', 'statut', 'apercu', 'date_publication', 'category', 'author')
    list_filter         = ('published', 'category')
    search_fields       = ('title', 'content')
    date_hierarchy      = 'date_publication'
    inlines             = [ActualiteEnImageInline]
    apercu              = apercu_image("image", 40)
    warn_unsaved_form   = True

    @display(description="Statut", label={"Publié": "success", "Brouillon": "warning"})
    def statut(self, obj):
        return "Publié" if obj.published else "Brouillon"

    def save_model(self, request, obj, form, change):
        # L'auteur est renseigné automatiquement à la création
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)


# ==========================================================================
# Page d'accueil
# ==========================================================================
@admin.register(BlocAccueil)
class BlocAccueilAdmin(ModelAdmin):
    list_display  = ("get_cle_display", "titre", "apercu", "actif")
    list_editable = ("actif",)
    apercu        = apercu_image("image")
    fieldsets = (
        (None, {"fields": ("cle", "surtitre", "titre", "texte", "points")}),
        ("Image", {"fields": ("image", "badge_image", "legende")}),
        ("Bouton", {"fields": ("bouton_texte", "bouton_lien")}),
        ("Affichage", {"fields": ("actif",)}),
    )


@admin.register(Slide)
class SlideAdmin(ModelAdmin):
    list_display  = ("titre", "apercu", "ordre", "actif")
    list_editable = ("ordre", "actif")
    apercu        = apercu_image("image")


class ParcoursLienInline(TabularInline):
    model = ParcoursLien
    extra = 1


@admin.register(Parcours)
class ParcoursAdmin(ModelAdmin):
    list_display  = ("titre", "description", "ordre", "actif")
    list_editable = ("ordre", "actif")
    inlines       = [ParcoursLienInline]


@admin.register(ChiffreCle)
class ChiffreCleAdmin(ModelAdmin):
    list_display  = ("valeur", "libelle", "source", "ordre", "actif")
    list_editable = ("ordre", "actif")


@admin.register(Partenaire)
class PartenaireAdmin(ModelAdmin):
    list_display  = ("nom", "apercu", "site_web", "ordre", "actif")
    list_editable = ("ordre", "actif")
    apercu        = apercu_image("logo", 36)


# ==========================================================================
# Pages, programmes et ressources
# ==========================================================================
@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display  = ("titre", "cle", "date_maj")
    search_fields = ("titre", "contenu")
    fields        = ("titre", "intro", "contenu", "image", "meta_description", "cle")
    warn_unsaved_form = True

    def get_readonly_fields(self, request, obj=None):
        # L'identifiant est figé une fois la page créée : le site s'en sert pour la retrouver.
        return ("cle",) if obj else ()


@admin.register(Programme)
class ProgrammeAdmin(ModelAdmin):
    list_display  = ("titre", "public_cible", "sur_accueil", "ordre", "actif")
    list_editable = ("sur_accueil", "ordre", "actif")
    search_fields = ("titre", "resume")
    warn_unsaved_form = True
    fieldsets = (
        (None, {"fields": ("titre", "resume", "public_cible", "icone", "image")}),
        ("Page détaillée", {"fields": ("contenu", "site_web")}),
        ("Affichage", {"fields": ("sur_accueil", "ordre", "actif")}),
    )


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display  = ("titre", "categorie", "date_publication", "actif")
    list_editable = ("actif",)
    list_filter   = ("categorie", "actif")
    search_fields = ("titre", "description")
    date_hierarchy = "date_publication"


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display        = ('ordre', 'question', 'active')
    list_editable       = ('ordre', 'active')
    list_display_links  = ('question',)
    ordering            = ('ordre',)
    search_fields       = ('question', 'reponse')



# ==========================================================================
# Textes du site et listes (lot 2)
# ==========================================================================
@admin.register(TexteSite)
class TexteSiteAdmin(ModelAdmin):
    list_display    = ("libelle", "apercu_texte", "page", "date_maj")
    list_filter     = ("page",)
    search_fields   = ("libelle", "valeur", "cle")
    list_per_page   = 50
    fields          = ("page", "libelle", "valeur", "texte_origine", "cle")
    readonly_fields = ("page", "libelle", "texte_origine", "cle")
    warn_unsaved_form = True

    @display(description="Texte actuel")
    def apercu_texte(self, obj):
        texte = obj.valeur or defaut(obj.cle)
        return texte if len(texte) <= 90 else texte[:90] + "…"

    @display(description="Texte d'origine")
    def texte_origine(self, obj):
        return defaut(obj.cle)

    # Les textes sont créés automatiquement (migrate) : pas d'ajout ni de suppression manuels
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Element)
class ElementAdmin(ModelAdmin):
    list_display  = ("titre", "liste", "page", "ordre", "actif")
    list_editable = ("ordre", "actif")
    list_filter   = ("liste", "actif")
    search_fields = ("titre", "texte")
    fields        = ("liste", "titre", "texte", "points", "page", "icone", "ordre", "actif")

    