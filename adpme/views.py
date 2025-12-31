from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    RedirectView
)
from django.urls import reverse
from django.http import FileResponse, Http404, HttpResponse
from django.db.models import F
from .models import (
    AgenceInfo,
    MembreEquipe,
    CategorieActualite,
    CategorieDocument,
    Actualite,
    Document,
    MessageContact,
    PageStatique,
    Partenaire
)
from .forms import ContactForm
# Create your views here.

class AccueilView(TemplateView):
    template_name = "adpme/accueil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 1 info de l'agence
        try:
            context['agence_info'] = AgenceInfo.objects.get()
        except AgenceInfo.DoesNotExist:
            context['agence_info'] = None # gérer le cas où aucune info n'existe
        
        # 2. Équipe (les 5 premiers par ordre d'affichage)
        context['membres_equipe'] = MembreEquipe.objects.all()[:3]

        # 3 actualités publiées récentes (les 3 dernières)
        context['actualites_recentes'] = Actualite.objects.filter(
            est_publie=True
        ).select_related('categorie')[:3]

        # 4 Partenaires
        context['partenaires'] = Partenaire.objects.all()
        
        return context

class InfoAgenceView(DetailView):
    # Comme il n'y a qu'une seule instance attendue, on utilise AgenceInfo comme modèle
    model = AgenceInfo 
    template_name = "adpme/agence/detail_agence.html"
    
    # Surcharge de get_object pour toujours récupérer la seule instance
    def get_object(self, queryset=None):
        try:
            return AgenceInfo.objects.get()
        except AgenceInfo.DoesNotExist:
            raise Http404("Aucune information d'agence n'est configurée.")


class ListeEquipeView(ListView):
    model = MembreEquipe
    template_name = "adpme/equipe/liste_equipe.html"
    context_object_name = "membres"
    # L'ordering est déjà défini dans la classe Meta du modèle, mais peut être spécifié ici aussi
    # ordering = ['ordre_affichage'] 
    paginate_by = 10


class ListeActualitesView(ListView):
    model = Actualite
    template_name = "adpme/actualites/liste_actualites.html"
    context_object_name = "actualites"
    paginate_by = 10

    def get_queryset(self):
        queryset = Actualite.objects.filter(est_publie=True)
        # Filtrage par catégorie si un slug est passé dans l'URL (via urls.py)
        self.categorie_slug = self.kwargs.get('categorie_slug')
        if self.categorie_slug:
            # S'assure que la catégorie existe et filtre
            self.categorie = get_object_or_404(
                CategorieActualite, slug=self.categorie_slug
            )
            queryset = queryset.filter(categorie=self.categorie)
        return queryset.select_related('categorie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter toutes les catégories pour un menu de filtrage
        context['categories'] = CategorieActualite.objects.all()
        # Ajouter la catégorie courante pour l'affichage du titre
        if hasattr(self, 'categorie'):
            context['categorie_actuelle'] = self.categorie
        return context


class DetailActualiteView(DetailView):
    model = Actualite
    template_name = "adpme/actualites/detail_actualite.html"
    context_object_name = "actualite"
    slug_field = 'slug'  # Utilise le champ 'slug' pour la recherche dans l'URL

    def get_queryset(self):
        # S'assurer que seules les actualités publiées sont visibles publiquement
        return Actualite.objects.filter(est_publie=True).prefetch_related('autres_images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupère les autres images associées à cette actualité
        context['galerie_images'] = self.object.autres_images.all()
        return context


class ListeDocumentsView(ListView):
    model = Document
    template_name = "adpme/documents/liste_documents.html"
    context_object_name = "documents"
    paginate_by = 20

    def get_queryset(self):
        queryset = Document.objects.filter(est_public=True)
        # Filtrage par catégorie si un slug est passé dans l'URL
        self.categorie_slug = self.kwargs.get('categorie_slug')
        if self.categorie_slug:
            self.categorie = get_object_or_404(
                CategorieDocument, slug=self.categorie_slug
            )
            queryset = queryset.filter(categorie=self.categorie)
        return queryset.select_related('categorie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategorieDocument.objects.all()
        if hasattr(self, 'categorie'):
            context['categorie_actuelle'] = self.categorie
        return context


class PageStatiqueView(DetailView):
    model = PageStatique
    template_name = "adpme/page_statique/detail_page.html"
    context_object_name = "page"
    slug_field = 'slug'

    def get_object(self, queryset=None):
        # Récupère l'objet PageStatique en utilisant le slug fourni dans l'URL
        return get_object_or_404(
            PageStatique, 
            slug=self.kwargs.get(self.slug_url_kwarg)
        )

class AProposView(TemplateView):
    # Assurez-vous que ce chemin est correct
    template_name = "adpme/apropos.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Optionnel: Si vous avez besoin d'infos de l'agence pour le footer, etc.
        try:
            context['agence_info'] = AgenceInfo.objects.get()
        except AgenceInfo.DoesNotExist:
            context['agence_info'] = None
        return context


def ProgrammeView(request):
    return render(request,'adpme/programme.html')    

def ActualiteView(request):
    return render(request,"adpme/actualite.html")

# Nécessite un MessageContactForm dans votre fichier forms.py
class ContactCreateView(CreateView):
    model = MessageContact
    # Assurez-vous d'avoir créé le formulaire MessageContactForm dans forms.py
    form_class = ContactForm 
    template_name = 'adpme/contact/contact_form.html'
    
    def get_success_url(self):
        # Rediriger vers la page de contact après succès (avec un message Flash)
        return reverse('contact_success') 
    
    def form_valid(self, form):
        # Optionnel: Ajouter un message flash avant de rediriger
        # from django.contrib import messages
        # messages.success(self.request, "Votre message a été envoyé avec succès!")
        return super().form_valid(form)

# Vue pour le succès de l'envoi du message de contact
class ContactSuccessView(TemplateView):
    template_name = "adpme/contact/contact_success.html"


class PageStatiqueView(DetailView):
    model = PageStatique
    template_name = "adpme/page_statique/detail_page.html"
    context_object_name = "page"
    slug_field = 'slug'

    def get_object(self, queryset=None):
        # Récupère l'objet PageStatique en utilisant le slug fourni dans l'URL
        return get_object_or_404(
            PageStatique, 
            slug=self.kwargs.get(self.slug_url_kwarg)
        )

