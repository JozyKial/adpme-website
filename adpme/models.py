from django.db import models

from django.template.defaultfilters import slugify
from django.utils import timezone

class AgenceInfo(models.Model):
    nom_agence      = models.CharField(max_length=200, default="ADPME")
    slogan          = models.CharField(max_length=255, blank=True, null=True)
    mission         = models.TextField(help_text="La mission de l'agence")
    vision          = models.TextField(blank=True, null=True, help_text="La vision à long terme")
    valeurs         = models.TextField(blank=True, null=True, help_text="Les valeurs fondamentales de l'agence")
    adresse         = models.CharField(max_length=100, blank=True, null=True)
    phone           = models.CharField(max_length=50, blank=True, null=True)
    email_contact   = models.EmailField(blank=True, null=True)
    liens_sociaux   = models.JSONField(blank=True, null=True, help_text="Ex: {'facebook':'url','linkedin':'url'}")
    carte_embed_url = models.URLField(blank=True, null=True, help_text="URL d'intégration Google Maps")

    class Meta:
        verbose_name    = "Information de l'agence"
        verbose_name_plural     = "Informations de l'agence"
    
    def __str__(self):
        return self.nom_agence


class MembreEquipe(models.Model):
    nom         = models.CharField(max_length=100)
    prenom      = models.CharField(max_length=100)
    fonction    = models.CharField(max_length=100)
    photo       = models.ImageField(upload_to='equipes/', blank=True, null=True)
    ordre_affichage = models.IntegerField(default=0, help_text="Ordre d'affichage sur la page de l'équipe")

    class Meta:
        verbose_name        = "Membre d'équipe"
        verbose_name_plural = "Membres d'équipe"
        ordering            = ['ordre_affichage']

    def __str__(self):
        return f"{self.nom} - ({self.fonction})"


class CategorieActualite(models.Model):
    """
    Catégories pour organiser les actualités (ex: "Événement", "Annonce", "Rapport").
    """
    nom     = models.CharField(max_length=100, unique=True)
    slug    = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name        = "Catégorie d'actualité"
        verbose_name_plural = "Catégorie d'actualités"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom


class Actualite(models.Model):
    """
    Modèle pour les articles d'actualité et les annonces.
    """
    titre       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)
    categorie   = models.ForeignKey(
        CategorieActualite,
        on_delete=models.SET_NULL, # si une catégoei est supprimé, les actualités ne le sont pas
        blank=True,
        null=True,
        related_name='actualites'
    )
    image_principale = models.ImageField(
        upload_to='actualites_images/',
        blank=True,
        null=True,
        help_text="Image d'illustration de l'actualité"
    )
    resume  = models.TextField(
        help_text="Un court résumé visible sur la liste des actualités",
        blank=True, 
        null=True
    )
    contenu             = models.TextField()
    date_publication    = models.DateTimeField(default=timezone.now)
    mis_a_jour_le       = models.DateTimeField(auto_now=True)
    est_publie          = models.BooleanField(default=True, help_text="Cochez pour publier l'actualité sur le site")

    class Meta:
        verbose_name        = "Actualité"
        verbose_name_plural = "Actualités"
        ordering            = ['-date_publication'] # les plus récentes en premier

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titre


class ImageActualite(models.Model):
    """
    Modèle pour les images supplémentaires d'une actualité.
    """
    actualite = models.ForeignKey(
        Actualite,
        on_delete=models.CASCADE, # Si l'actualité est supprimée, ses images le sont aussi
        related_name='autres_images' # Nom pour accéder aux images depuis une actualité (e.g., actualite.autres_images.all())
    )
    image = models.ImageField(
        upload_to='actualites_images/supplementaires/', # Dossier pour les images supplémentaires
        help_text="Image supplémentaire pour l'actualité"
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Description ou légende de l'image"
    )
    ordre_affichage = models.IntegerField(
        default=0,
        help_text="Ordre d'affichage de l'image dans la galerie"
    )

    class Meta:
        verbose_name = "Image d'Actualité Supplémentaire"
        verbose_name_plural = "Images d'Actualité Supplémentaires"
        ordering = ['ordre_affichage'] # Pour afficher les images dans un ordre défini

    def __str__(self):
        return f"Image pour '{self.actualite.titre}' - {self.description or 'Sans description'}"


class CategorieDocument(models.Model):
    nom     = models.CharField(max_length=100, unique=True)
    slug    = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name    = "Catégorie de document"
        verbose_name_plural = "Catégories de documents"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom


class Document(models.Model):
    titre       = models.CharField(max_length=225)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    categorie   = models.ForeignKey(
        CategorieDocument,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='documents'
    )
    description = models.TextField(blank=True, null=True, help_text="Brève description du document")
    fichier     = models.FileField(
        upload_to='documents_telechargement/',
        help_text="Le fichier à télécharger (PDF, Word, Excel, etc.)"
    )
    date_publication        = models.DateTimeField(default=timezone.now)
    est_public              = models.BooleanField(default=True, help_text="Cochez pour rendre public le téléchargement")
    nombre_telechargements  = models.IntegerField(default=0, editable=False) # compter le nombre de téléchargement du fichier

    class Meta:
        verbose_name    = "Document"
        verbose_name_plural     = "Documents"
        ordering = ['-date_publication']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
    
    def increment_downloads(self):
        """ Méthode pour incrémenter le compteur de téléchargements """
        self.nombre_telechargements+=1
        self.save()


class MessageContact(models.Model):
    nom         = models.CharField(max_length=100)
    email       = models.EmailField()
    sujet       = models.CharField(max_length=150)
    message     = models.TextField()
    date_envoi  = models.DateTimeField(auto_now_add=True)
    lu          = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"


class PageStatique(models.Model):
    TITRES_PAGES = [
        ('a_propos', 'A propos'),
        ('document', 'Lois et textes'),
        ('contact', 'Contact'),
    ]

    titre    = models.CharField(max_length=100, choices=TITRES_PAGES, unique=True)
    contenu  = models.TextField()
    slug     = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.get_titre_display())
            super().save(*args, **kwargs)
    
    def __str__(self):
        return self.get_titre_display()


class Partenaire(models.Model):
    nomPartenanire  = models.CharField(max_length=150)
    logo            = models.ImageField(upload_to='partenaires_logo/', blank=True, null=True)
    lien            = models.URLField(blank=True)

    def __str__(self):
        return self.nomPartenanire



    







    