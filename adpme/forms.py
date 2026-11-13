# ==========================================================================
# ADPME Congo — forms.py — v3
# Formulaire de contact et inscription à la lettre d'information.
# Libellés et exemples modifiables dans admin > Textes du site.
# ==========================================================================
from django import forms

from .textes import texte_admin


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    sujet = forms.CharField(max_length=200, widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Libellé et texte d'exemple de chaque champ : admin > Textes du site
        for nom, champ in self.fields.items():
            champ.label = texte_admin(f"contact.champ_{nom}")
            champ.widget.attrs['placeholder'] = texte_admin(f"contact.champ_{nom}_exemple")


class NewsletterForm(forms.Form):
    email = forms.EmailField(max_length=254)
    # Piège à robots : champ invisible pour les humains, il doit rester vide.
    site_web = forms.CharField(required=False)

    