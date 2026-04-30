from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=100,
        label="Nom complet",
        widget=forms.TextInput(attrs={
            'placeholder': 'Votre nom complet',
        })
    )
    email = forms.EmailField(
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Votre adresse e-mail',
        })
    )
    sujet = forms.CharField(
        max_length=200,
        label="Sujet",
        widget=forms.TextInput(attrs={
            'placeholder': 'Sujet de votre message',
        })
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Votre message...',
            'rows': 6
        })
    )

