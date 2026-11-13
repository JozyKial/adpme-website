# ==========================================================================
# ADPME Congo — models.py — v5
# Modèles. Lot 2 : TexteSite (textes du site) et Element (listes modifiables).
# Phase 4c : Offre (appels d'offres, emplois et stages, appels à candidatures)
# et Abonne (lettre d'information).
# ==========================================================================
import uuid

from django.core.validators import FileExtensionValidator
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
    whatsapp        = models.CharField(
        max_length=30, blank=True, null=True,
        help_text="Numéro WhatsApp au format international, ex. +242 06 000 00 00. Laisser vide pour masquer le bouton WhatsApp.")
    horaires        = models.CharField(
        max_length=120, blank=True, null=True,
        help_text="Ex. : Lundi – vendredi, 8h – 16h. Laisser vide pour ne rien afficher.")
    liens_sociaux   = models.JSONField(blank=True, null=True, help_text="Ex: {'facebook':'url','linkedin':'url'}")
    carte_embed_url = models.URLField(blank=True, null=True, help_text="URL d'intégration Google Maps")

    class Meta:
        verbose_name    = "Information de l'agence"
        verbose_name_plural     = "Informations de l'agence"
    
    def __str__(self):
        return self.nom_agence

class Category(models.Model):
    name   = models.CharField(max_length=100, verbose_name="Nom")
    slug   = AutoSlugField(populate_from = "name", unique=True, null=True, default=None)

    class Meta:
        verbose_name        = "Catégorie"
        verbose_name_plural = "Catégories"

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
    author      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
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
        verbose_name        = "Actualité"
        verbose_name_plural = "Actualités"
    
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


# ==========================================================================
# Refonte v3 — Phase 4b : antennes et documents téléchargeables
# ==========================================================================

class Antenne(models.Model):
    nom         = models.CharField(max_length=150, verbose_name="Nom", help_text="Ex. : Antenne de Pointe-Noire")
    ville       = models.CharField(max_length=100, verbose_name="Ville ou département")
    adresse     = models.CharField(max_length=255, blank=True, verbose_name="Adresse")
    telephone   = models.CharField(max_length=40, blank=True, verbose_name="Téléphone")
    email       = models.EmailField(blank=True, verbose_name="E-mail")
    horaires    = models.CharField(max_length=120, blank=True, verbose_name="Horaires")
    lien_carte  = models.URLField(blank=True, verbose_name="Lien Google Maps",
                                  help_text="Lien « Partager » de Google Maps (ouvre l'itinéraire).")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affichée")

    class Meta:
        ordering            = ["ordre", "nom"]
        verbose_name        = "Antenne"
        verbose_name_plural = "Antennes"

    def __str__(self):
        return self.nom


class Document(models.Model):
    CATEGORIES = [
        ("textes", "Textes juridiques et réglementaires"),
        ("guides", "Guides pratiques"),
        ("formulaires", "Formulaires"),
        ("rapports", "Rapports et études"),
        ("autres", "Autres documents"),
    ]

    titre       = models.CharField(max_length=255, verbose_name="Titre")
    description = models.CharField(max_length=300, blank=True, verbose_name="Description courte")
    categorie   = models.CharField(max_length=20, choices=CATEGORIES, default="autres", verbose_name="Catégorie")
    fichier     = models.FileField(
        upload_to="documents/%Y/", verbose_name="Fichier",
        validators=[FileExtensionValidator(["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "ods", "zip"])],
        help_text="PDF conseillé. Formats acceptés : PDF, Word, Excel, PowerPoint, OpenDocument, ZIP.")
    date_publication = models.DateField(default=timezone.now, verbose_name="Date de publication")
    actif       = models.BooleanField(default=True, verbose_name="Publié")

    class Meta:
        ordering            = ["-date_publication", "titre"]
        verbose_name        = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.titre

    @property
    def extension(self):
        return self.fichier.name.rsplit(".", 1)[-1].upper() if "." in self.fichier.name else ""

    @property
    def taille(self):
        """Taille lisible (ex. « 1,2 Mo ») ; vide si le fichier est introuvable."""
        try:
            octets = self.fichier.size
        except (OSError, ValueError):
            return ""
        for unite in ("o", "Ko", "Mo", "Go"):
            if octets < 1024 or unite == "Go":
                return f"{octets:.0f} {unite}" if unite == "o" else f"{octets:.1f} {unite}".replace(".", ",")
            octets /= 1024


# ==========================================================================
# Refonte v3 — Blocs éditoriaux de la page d'accueil
# ==========================================================================

class BlocAccueil(models.Model):
    CLES = [
        ("presentation", "Qui sommes-nous ? (texte + image)"),
        ("missions", "Nos missions (liste + image)"),
        ("priorites", "Nos priorités (bandeau pleine largeur)"),
        ("competences", "Développez vos compétences (image + liste + bouton)"),
    ]

    cle         = models.CharField(max_length=30, choices=CLES, unique=True, verbose_name="Bloc")
    surtitre    = models.CharField(max_length=80, blank=True, verbose_name="Surtitre",
                                   help_text="Petit texte au-dessus du titre (ex. : Qui sommes-nous ?)")
    titre       = models.CharField(max_length=150, verbose_name="Titre")
    texte       = models.TextField(blank=True, verbose_name="Texte")
    points      = models.TextField(blank=True, verbose_name="Liste à puces",
                                   help_text="Un point par ligne.")
    image       = models.ImageField(upload_to="accueil/", blank=True, null=True, verbose_name="Image",
                                    help_text="Photo de l'ADPME, format paysage conseillé (1200×900).")
    badge_image = models.CharField(max_length=40, blank=True, verbose_name="Badge sur l'image",
                                   help_text="Bloc « compétences » uniquement (ex. : Programme SYB).")
    legende     = models.CharField(max_length=120, blank=True, verbose_name="Légende sur l'image",
                                   help_text="Bloc « compétences » uniquement.")
    bouton_texte = models.CharField(max_length=60, blank=True, verbose_name="Texte du bouton")
    bouton_lien = models.CharField(max_length=300, blank=True, verbose_name="Lien du bouton",
                                   help_text="Chemin du site (ex. : /a-propos/) ou adresse complète.")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["cle"]
        verbose_name        = "Bloc de la page d'accueil"
        verbose_name_plural = "Blocs de la page d'accueil"

    def __str__(self):
        return f"{self.get_cle_display()} — {self.titre}"

    @property
    def liste_points(self):
        return [ligne.strip(" -•\t") for ligne in self.points.splitlines() if ligne.strip(" -•\t")]


# ==========================================================================
# Refonte v3 — Lot 2 : textes et listes modifiables dans l'admin
# ==========================================================================

def choix_pages_textes():
    from .textes import PAGES
    return PAGES


class TexteSite(models.Model):
    cle         = models.CharField(max_length=100, unique=True, verbose_name="Identifiant")
    page        = models.CharField(max_length=30, choices=choix_pages_textes, verbose_name="Page")
    libelle     = models.CharField(max_length=200, verbose_name="Emplacement")
    valeur      = models.TextField(blank=True, verbose_name="Texte",
                                   help_text="Laisser vide pour revenir au texte d'origine.")
    date_maj    = models.DateTimeField(auto_now=True, verbose_name="Modifié le")

    class Meta:
        ordering            = ["page", "cle"]
        verbose_name        = "Texte du site"
        verbose_name_plural = "Textes du site"

    def __str__(self):
        return self.libelle


class Element(models.Model):
    LISTES = [
        ("acces", "Accueil — Accès rapides « Que souhaitez-vous faire ? »"),
        ("service", "Dispositifs — Offre de services"),
        ("etape", "Dispositifs — Étapes du parcours d'accompagnement"),
    ]

    liste       = models.CharField(max_length=20, choices=LISTES, verbose_name="Liste")
    titre       = models.CharField(max_length=120, verbose_name="Titre")
    texte       = models.CharField(max_length=300, blank=True, verbose_name="Texte court")
    points      = models.TextField(blank=True, verbose_name="Points clés",
                                   help_text="Offre de services uniquement. Un point par ligne.")
    page        = models.CharField(max_length=60, choices=choix_pages, blank=True, verbose_name="Page visée",
                                   help_text="Page ouverte au clic (accès rapides et services).")
    icone       = models.CharField(max_length=40, choices=choix_icones, blank=True, verbose_name="Icône")
    ordre       = models.PositiveIntegerField(default=0, verbose_name="Ordre")
    actif       = models.BooleanField(default=True, verbose_name="Affiché")

    class Meta:
        ordering            = ["liste", "ordre", "id"]
        verbose_name        = "Élément de liste"
        verbose_name_plural = "Listes (accès rapides, services, étapes)"

    def __str__(self):
        return self.titre

    @property
    def liste_points(self):
        return [ligne.strip(" -•\t") for ligne in self.points.splitlines() if ligne.strip(" -•\t")]


# ==========================================================================
# Refonte v3 — Phase 4c : opportunités et lettre d'information
# ==========================================================================

class Offre(models.Model):
    TYPES = [
        ("appel_offres", "Appel d'offres"),
        ("emploi", "Emploi ou stage"),
        ("candidature", "Appel à candidatures (programme, concours, financement…)"),
    ]
    # Adresse de chaque rubrique sur le site : /opportunites/<slug>/
    SLUGS_TYPES = {"appel_offres": "appels-offres", "emploi": "emplois-stages", "candidature": "appels-candidatures"}

    type_offre  = models.CharField(max_length=20, choices=TYPES, verbose_name="Type")
    titre       = models.CharField(max_length=255, verbose_name="Titre")
    slug        = AutoSlugField(populate_from="titre", unique=True)
    reference   = models.CharField(max_length=80, blank=True, verbose_name="Référence",
                                   help_text="Ex. : AO-2026-001. Facultatif.")
    resume      = models.TextField(max_length=300, verbose_name="Résumé (affiché dans la liste)")
    contenu     = RichTextUploadingField(verbose_name="Description complète")
    modalites   = RichTextUploadingField(blank=True, verbose_name="Comment postuler ou soumissionner",
                                         help_text="Pièces à fournir, lieu et mode de dépôt…")
    lieu        = models.CharField(max_length=150, blank=True, verbose_name="Lieu",
                                   help_text="Ex. : Brazzaville, ou « Tout le territoire ».")
    date_publication = models.DateField(default=timezone.now, verbose_name="Date de publication")
    date_limite = models.DateField(blank=True, null=True, verbose_name="Date limite",
                                   help_text="Après cette date, l'offre passe automatiquement dans « Clôturées ». "
                                             "Vide : pas de date limite.")
    fichier     = models.FileField(
        upload_to="opportunites/%Y/", blank=True, verbose_name="Dossier à télécharger",
        validators=[FileExtensionValidator(["pdf", "doc", "docx", "xls", "xlsx", "odt", "zip"])],
        help_text="TDR, dossier d'appel d'offres, fiche de poste… PDF conseillé.")
    lien_externe = models.URLField(blank=True, verbose_name="Lien externe",
                                   help_text="Formulaire en ligne ou annonce publiée ailleurs. Facultatif.")
    email_contact = models.EmailField(blank=True, verbose_name="E-mail de contact ou de dépôt")
    actif       = models.BooleanField(default=True, verbose_name="Publiée")

    class Meta:
        ordering            = ["-date_publication", "-id"]
        verbose_name        = "Opportunité"
        verbose_name_plural = "Opportunités (offres, emplois, appels)"

    def __str__(self):
        return self.titre

    @property
    def est_ouverte(self):
        return self.date_limite is None or self.date_limite >= timezone.localdate()

    @property
    def slug_type(self):
        return self.SLUGS_TYPES.get(self.type_offre, "")

    @property
    def extension(self):
        return self.fichier.name.rsplit(".", 1)[-1].upper() if self.fichier and "." in self.fichier.name else ""


class Abonne(models.Model):
    email       = models.EmailField(unique=True, verbose_name="Adresse e-mail")
    actif       = models.BooleanField(default=True, verbose_name="Inscrit",
                                      help_text="Décoché : la personne s'est désinscrite.")
    origine     = models.CharField(max_length=200, blank=True, verbose_name="Page d'inscription")
    jeton       = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,
                                   verbose_name="Jeton de désinscription")
    date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Inscrit le")
    date_maj    = models.DateTimeField(auto_now=True, verbose_name="Modifié le")

    class Meta:
        ordering            = ["-date_inscription"]
        verbose_name        = "Abonné à la lettre d'information"
        verbose_name_plural = "Abonnés à la lettre d'information"

    def __str__(self):
        return self.email

    