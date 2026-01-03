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
    CategorieActu,
    Actualite,
)
#from .forms import ContactForm
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
                CategorieActu, slug=self.categorie_slug
            )
            queryset = queryset.filter(categorie=self.categorie)
        return queryset.select_related('categorie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter toutes les catégories pour un menu de filtrage
        context['categories'] = CategorieActu.objects.all()
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

def ContactView(request):
    return render(request,"adpme/contact.html")



