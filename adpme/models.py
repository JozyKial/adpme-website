from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

class AgenceInfo(models.Model):
    nom_agence      = models.CharField(max_length=200, default="ADPME")
    slogan          = models.CharField(max_length=255, blank=True, null=True)
    mission         = models.TextField(help_text="La mission de l'agence")
    vision          = models.TextField(blank=True, null=True, help_text="La vision à long terme")
    valeurs         = models.TextField(blank=True, null=True, help_text="Les valeurs fondamentales de l'agence")
    adresse         = models.CharField(max_length=100, blank=True, null=True)
    phone           = models.CharField(max_length=50, blank=True, null=True)
    email_contact   = models.EmailField(blank=True, null=True)
    whatsapp        = models.CharField(max_length=30, blank=True, null=True,help_text="Numéro WhatsApp au format international, ex. +242 06 000 00 00. Laisser vide pour masquer le bouton WhatsApp.")
    horaires        = models.CharField(max_length=120, blank=True, null=True,help_text="Ex. : Lundi – vendredi, 8h – 16h. Laisser vide pour ne rien afficher.")
    liens_sociaux   = models.JSONField(blank=True, null=True, help_text="Ex: {'facebook':'url','linkedin':'url'}")
    carte_embed_url = models.URLField(blank=True, null=True, help_text="URL d'intégration Google Maps")

    class Meta:
        verbose_name    = "Information de l'agence"
        verbose_name_plural     = "Informations de l'agence"
    
    def __str__(self):
        return self.nom_agence

class Category(models.Model):
    name   = models.CharField(max_length=100, verbose_name="Categorie")
    slug   = AutoSlugField(populate_from = "name", unique=True, null=True, default=None)

    class Meta:
        verbose_name = "Categorie"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name

class BlogActualite(models.Model):
    
    STATUS = (
        ('0','DRAFT'),
        ('1','PUBLISH')
    )

    SECTION = (
        ('Recent', 'Recent'),
        ('Publish', 'Publish'),
        ('Trending', 'Trending')
    )

    title       = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    author      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image       = models.ImageField(upload_to="actualite_img", blank=True, null=True, verbose_name="Image d'entête")
    content     = RichTextUploadingField()
    category    = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, verbose_name="Catégorie")
    blog_slug   = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    created_on  = models.DateField(auto_now_add=True)
    published   = models.BooleanField(default=False, verbose_name="Publié")
    Main_post   = models.BooleanField(default=False)
    status      = models.CharField(choices=STATUS, max_length=1, default='0')
    section     = models.CharField(choices=SECTION, max_length=100)
    date_publication    = models.DateField(default=timezone.now, verbose_name="Date de publication effective")
    last_update         = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Actualite"
    
    def __str__(self):
        return f"{self.title} ({self.category})"
     
class ActualiteEnImage(models.Model):
    actualite   = models.ForeignKey(BlogActualite, related_name='galerie', on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='actualite_galerie/')
    caption     = models.CharField(max_length=255, blank=True,help_text="Description facultative de l'image")

    def __str__(self):
        return f"Image - {self.actualite.title}" 

class FAQ(models.Model):
    question    = models.CharField(max_length=300, verbose_name="Question")
    reponse     = models.TextField(verbose_name="Réponse")
    ordre       = models.PositiveSmallIntegerField(default=0, verbose_name="Ordre d'affichage")
    active      = models.BooleanField(default=True, verbose_name="Visible sur le site")

    class Meta:
        ordering        = ['ordre']
        verbose_name    = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question

class Discours(models.Model):
    TYPE_CHOICES = (
        ('dg', 'Directeur Général'),
        ('ministre', 'Ministre'),
    )

    type_discours   = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True, verbose_name="Type de discours")
    nom_auteur      = models.CharField(max_length=200, verbose_name="Nom de l'auteur")
    fonction        = models.CharField(max_length=200, verbose_name="Fonction")
    photo           = models.ImageField(upload_to="discours/", blank=True, null=True, verbose_name="Photo")
    extrait         = models.TextField(verbose_name="Extrait (citation courte pour l'accueil)", help_text="2-3 phrases maximum, affichées sur la page d'accueil")
    contenu_complet = RichTextUploadingField(verbose_name="Discours complet")
    date_maj        = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Discours"
        verbose_name_plural = "Discours"

    def __str__(self):
        return f"Discours — {self.get_type_discours_display()}"




# ==========================================================================
# Refonte v3 — Phase 3 : contenus de la page d'accueil (tous gérés dans l'admin)
# ==========================================================================

def choix_icones():
    """Liste des icônes disponibles (adpme/templatetags/ui.py)."""
    from .templatetags.ui import ICONES
    return [(nom, nom) for nom in sorted(ICONES)]


def choix_pages():
    """Pages internes du site qu'on peut viser depuis l'admin (nom de route)."""
    from .navigation import MENU_PRINCIPAL
    pages = []
    for rubrique in MENU_PRINCIPAL:
        for lien in rubrique.get("liens", [rubrique]):
            pages.append((lien["url"], lien["titre"]))
    pages += [("contact", "Contact"), ("recherche", "Recherche")]
    return pages


class Slide(models.Model):
    titre       = models.CharField(max_length=150, verbose_name="Titre")
    texte       = models.TextField(max_length=300, blank=True, verbose_name="Texte court")
    image       = models.ImageField(upload_to="slides/", verbose_name="Image (format paysage, 1920×800 conseillé)")
    bouton_texte = models.CharField(max_length=60, blank=True, verbose_name="Texte du bouton")
    bouton_lien = models.CharField(max_length=300, blank=True, verbose_name="Lien du bouton",
                                   help_text="Adresse complète (https://…) ou chemin du site (/contact/).")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["ordre", "id"]
        verbose_name        = "Slide (bandeau d'accueil)"
        verbose_name_plural = "Slides (bandeau d'accueil)"

    def __str__(self):
        return self.titre


class Programme(models.Model):
    titre       = models.CharField(max_length=200, verbose_name="Titre")
    slug        = AutoSlugField(populate_from="titre", unique=True)
    resume      = models.TextField(max_length=300, verbose_name="Résumé (affiché sur les cartes)")
    public_cible = models.CharField(max_length=150, blank=True, verbose_name="Public cible",
                                    help_text="Ex. : Jeunes porteurs de projets")
    icone       = models.CharField(max_length=40, choices=choix_icones, default="drapeau", verbose_name="Icône")
    image       = models.ImageField(upload_to="programmes/", blank=True, null=True, verbose_name="Image")
    contenu     = RichTextUploadingField(blank=True, verbose_name="Présentation détaillée")
    site_web    = models.URLField(blank=True, verbose_name="Site ou page externe du programme")
    sur_accueil = models.BooleanField(default=True, verbose_name="Afficher sur l'accueil")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Publié")

    class Meta:
        ordering            = ["ordre", "titre"]
        verbose_name        = "Programme"
        verbose_name_plural = "Programmes"

    def __str__(self):
        return self.titre


class Parcours(models.Model):
    titre       = models.CharField(max_length=100, verbose_name="Profil", help_text="Ex. : Porteur de projet")
    description = models.CharField(max_length=200, blank=True, verbose_name="Description courte")
    icone       = models.CharField(max_length=40, choices=choix_icones, default="utilisateur", verbose_name="Icône")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["ordre", "id"]
        verbose_name        = "Parcours « Vous êtes… »"
        verbose_name_plural = "Parcours « Vous êtes… »"

    def __str__(self):
        return self.titre


class ParcoursLien(models.Model):
    parcours    = models.ForeignKey(Parcours, related_name="liens", on_delete=models.CASCADE)
    libelle     = models.CharField(max_length=100, verbose_name="Libellé", help_text="Ex. : M'informer et m'orienter")
    page        = models.CharField(max_length=60, choices=choix_pages, verbose_name="Page visée")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")

    class Meta:
        ordering            = ["ordre", "id"]
        verbose_name        = "Lien du parcours"
        verbose_name_plural = "Liens du parcours"

    def __str__(self):
        return self.libelle


class ChiffreCle(models.Model):
    valeur      = models.CharField(max_length=30, verbose_name="Valeur", help_text="Ex. : 1 250 ou 85 %")
    libelle     = models.CharField(max_length=150, verbose_name="Libellé", help_text="Ex. : entrepreneurs formés")
    source      = models.CharField(max_length=200, blank=True, verbose_name="Source",
                                   help_text="Ex. : Rapport d'activité 2025. Fortement conseillé.")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["ordre", "id"]
        verbose_name        = "Chiffre clé"
        verbose_name_plural = "Chiffres clés"

    def __str__(self):
        return f"{self.valeur} {self.libelle}"


class Partenaire(models.Model):
    nom         = models.CharField(max_length=150, verbose_name="Nom")
    logo        = models.ImageField(upload_to="partenaires/", verbose_name="Logo (PNG fond transparent conseillé)")
    site_web    = models.URLField(blank=True, verbose_name="Site web")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["ordre", "nom"]
        verbose_name        = "Partenaire"
        verbose_name_plural = "Partenaires"

    def __str__(self):
        return self.nom
    



# ==========================================================================
# Refonte v3 — Phase 4 : pages de contenu (L'Agence, services)
# ==========================================================================

class Page(models.Model):
    cle         = models.SlugField(max_length=60, unique=True, verbose_name="Identifiant",
                                   help_text="Identifiant technique utilisé par le site (ex. : information). Ne pas modifier.")
    titre       = models.CharField(max_length=200, verbose_name="Titre")
    intro       = models.CharField(max_length=300, blank=True, verbose_name="Introduction",
                                   help_text="Une ou deux phrases affichées sous le titre.")
    contenu     = RichTextUploadingField(verbose_name="Contenu")
    image       = models.ImageField(upload_to="pages/", blank=True, null=True, verbose_name="Image d'illustration")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="Description pour Google",
                                        help_text="160 caractères maximum. Vide : l'introduction est utilisée.")
    date_maj    = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        ordering            = ["titre"]
        verbose_name        = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.titre

    
