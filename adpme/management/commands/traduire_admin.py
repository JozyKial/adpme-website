# ==========================================================================
# ADPME Congo — management/commands/traduire_admin.py — v1
# Génère la traduction française de l'administration (adpme/traductions_admin.py).
# Usage : py manage.py traduire_admin   (fait aussi automatiquement par migrate)
# ==========================================================================
from django.core.management.base import BaseCommand

from adpme.traductions_admin import TRADUCTIONS, generer_catalogue


class Command(BaseCommand):
    help = "Génère la traduction française de l'administration (thème Unfold)."

    def handle(self, *args, **options):
        chemin = generer_catalogue()
        if chemin is None:
            self.stderr.write(self.style.ERROR("LOCALE_PATHS n'est pas défini dans settings.py."))
            return
        self.stdout.write(self.style.SUCCESS(
            f"{len(TRADUCTIONS)} traductions écrites dans {chemin}. Redémarrez le serveur pour les voir."))

        