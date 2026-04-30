import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import FileResponse, Http404, HttpResponse
from django.db.models import F
from .models import (
    BlogActualite,
    Category,
    FAQ,
)

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

from django.core.paginator import Paginator

def AccueilView(request):
    post        = BlogActualite.objects.order_by('-id')
    main_post   = BlogActualite.objects.order_by('-id').filter(Main_post = True)[0:1] 
    recent      = BlogActualite.objects.filter(section = 'Recent').order_by('-id')[:5]
    categorie   = Category.objects.all()

    context = {
        'post':post,
        'main_post':main_post,
        'recent':recent,
        'categorie':categorie
    }

    return render(request,"adpme/accueil.html", context)


def Categorie(request, slug):
    cat = Category.objects.all()
    blog_cat    = Category.objects.filter(slug = slug)
    
    context = {
        'cat' : cat,
        'active_category' : slug,
        'blog_cat' : blog_cat
    }

    return render(request,"adpme/categorie.html", context)


def Blog_detail(request, slug):
    post        = get_object_or_404(BlogActualite, blog_slug=slug)
    posts       = BlogActualite.objects.filter(published=True).exclude(id=post.id).order_by('-created_on')[:5]
    category    = Category.objects.all()

    context = {
        'posts' : posts,
        'category' : category,
        'post' : post
    }

    return render(request, "adpme/detail_actualite.html", context)


def ActualiteView(request):
    posts_list = BlogActualite.objects.filter(published=True).order_by('-created_on')
    cat        = Category.objects.all()

    paginator   = Paginator(posts_list, 6)
    page        = request.GET.get('page', 1)
    posts       = paginator.get_page(page)   

    context = {
        'cat'   : cat,
        'posts' : posts,
    }

    return render(request,"adpme/actualite.html", context)


def AproposView(request):
    return render(request,"adpme/apropos.html")

def Info_orientationView(request):
    return render(request,"adpme/information.html")

def FormationView(request):
    return render(request,"adpme/formation.html")

def AccompagnementView(request):
    return render(request,"adpme/accompagnement.html")

def ConseilView(request):
    return render(request,"adpme/conseil.html")


def ProgrammeView(request):
    return render(request,"adpme/programme.html")    


def BlogActualiteView(request):
    return render(request,"adpme/BlogActualite.html")

logger = logging.getLogger(__name__)
def ContactView(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom             = form.cleaned_data['nom']
            email           = form.cleaned_data['email']
            sujet           = form.cleaned_data['sujet']
            message_text    = form.cleaned_data['message']

            try:
                send_mail(
                    subject         = f"[ADPME Contact] {sujet}",
                    message         = f"Message de : {nom} <{email}>\n\n{message_text}",
                    from_email      = settings.DEFAULT_FROM_EMAIL,
                    recipient_list  = [settings.CONTACT_EMAIL],
                    fail_silently   = False,
                )
                messages.success(request, "votre message a bien été envoyé. Nous répondrons dans les plus brefs délais.")
                form = ContactForm()
            except Exception as e:
                logger.error(f"Erreur envoi email contact : {e}")
                messages.error(request, "Une erreur est survenue lors de l'envoi. Veuillez réessayer ou nous contacter directement par téléphone.")

    return render(request, "adpme/contact.html",{'form':form})


def FaqView(request):
    faqs = FAQ.objects.filter(active=True)
    return render(request, "adpme/faq.html", {'faqs':faqs})

