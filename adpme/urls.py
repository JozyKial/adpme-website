from django.urls import path, include
from django.conf.urls.static import static
from . import views 

from adpme_project import settings

urlpatterns = [
    #path('admin/',admin.site.urls),
    # Accueil & Infos
    path('',views.AccueilView, name="accueil"),
    path('a-propos/', views.AproposView, name='a_propos'),
    path('programme', views.ProgrammeView, name="programme"),
    path('actualite', views.ActualiteView,name="actualite"),
    path('contact', views.ContactView,name="contact"),
    path('conseil', views.ConseilView, name="conseil"),
    path('information', views.Info_orientationView, name="information"),
    path('accompagnement', views.AccompagnementView, name="accompagnement"),
    path('formation', views.FormationView, name="formation"),
    path('actualite/<str:slug>', views.Blog_detail, name="actu_detail"),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
