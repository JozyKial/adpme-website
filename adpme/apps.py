# ==========================================================================
# ADPME Congo — apps.py — v2
# Configuration de l'application : synchronisation des textes après migrate.
# ==========================================================================
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AdpmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adpme'
    verbose_name = 'Site ADPME'

    def ready(self):
        # Après chaque migrate : textes du site et listes créés automatiquement
        from .synchronisation import synchroniser
        post_migrate.connect(synchroniser, sender=self)
        