from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import FileResponse, Http404, HttpResponse
from django.db.models import F
from .models import (
    BlogActualite,
    Category,
)


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
    cat    = Category.objects.all()
    context = {
        'cat' : cat
    }
    return render(request,"adpme/actualite.html", context)


def AproposView(request):
    return render(request,"adpme/apropos.html")


def ProgrammeView(request):
    return render(request,"adpme/programme.html")    


def BlogActualiteView(request):
    return render(request,"adpme/BlogActualite.html")


def ContactView(request):
    return render(request,"adpme/contact.html")



