from django.db import models
from autoslug import AutoSlugField
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


class CategorieActu(models.Model):
    """
    Catégories pour organiser les actualités (ex: "Événement", "Annonce", "Rapport").
    """
    nom     = models.CharField(max_length=100)
    slug    = AutoSlugField(populate_from = "name", unique=True, blank=True, default=None)

    class Meta:
        verbose_name        = "Catégorie d'actualité"
        verbose_name_plural = "Catégorie d'actualités"
    
    def __str__(self):
        return self.nom




class Actualite(models.Model):
    """
    Modèle pour les articles d'actualité et les annonces.
    """
    STATUTS = (
        ('0','DRAFT'),
        ('1','PUBLISH')
    )

    SECTION = (
        ('Recent','Recent'),
        ('Publish','Publish'),
        ('Trending','Trending')
    )

    titre       = models.CharField(max_length=200)
    actu_slug   = AutoSlugField(populate_from="titre", unique=True, blank=True, default=None)
    categorie   = models.ForeignKey(
        CategorieActu,
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
    # est_publie          = models.BooleanField(default=True, help_text="Cochez pour publier l'actualité sur le site")
    status              = models.CharField(choices=STATUTS, max_length=1, default='0')
    section             = models.CharField(choices=SECTION, max_length=100, default='Recent')


    class Meta:
        verbose_name        = "Actualité"
        verbose_name_plural = "Actualités"
        ordering            = ['-date_publication'] # les plus récentes en premier
    
    def __str__(self):
        return f"{self.titre} ({self.categorie})"




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



    







    