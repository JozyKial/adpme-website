from django.urls import path
from . import views 


urlpatterns = [
    # Accueil & Infos
    path('',views.AccueilView.as_view(), name="accueil"),
    path('a-propos/', views.AProposView.as_view(), name='a_propos'),
    path('programme', views.ProgrammeView, name="programme"),
    path('actualite', views.ActualiteView,name="actualite"),

    #Actualités
    path('actualites/', views.ListeActualitesView.as_view(), name='liste_actualites'),
    path('actualites/categorie/<slug:categorie_slug>/', views.ListeActualitesView.as_view(), name='liste_actualites_par_categorie'),
    path('actualites/<slug:slug>/', views.DetailActualiteView.as_view(), name='detail_actualite'),



    
]