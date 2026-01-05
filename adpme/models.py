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
    category    = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug   = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    last_update = models.DateTimeField(auto_now=True)
    created_on  = models.DateField(auto_now_add=True)
    published   = models.BooleanField(default=False, verbose_name="Publié")
    Main_post   = models.BooleanField(default=False)
    status      = models.CharField(choices=STATUS, max_length=1, default='0')
    section     = models.CharField(choices=SECTION, max_length=100)


    class Meta:
        ordering = ['-created_on']
        verbose_name = "Actualite"
    
    def __str__(self):
        return f"{self.title} ({self.category})"
    
  







    