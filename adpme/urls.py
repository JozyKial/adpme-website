from django.urls import path
from . import views 


urlpatterns = [
    # Accueil & Infos
    path('',views.AccueilView.as_view(), name="accueil"),
    path('a-propos/', views.AProposView.as_view(), name='a_propos'),
    path('programme', views.ProgrammeView, name="programme"),
    path('actualite', views.ActualiteView,name="actualite"),
    path('contact', views.ContactView,name="contact"),


    
]