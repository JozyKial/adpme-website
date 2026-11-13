# ==========================================================================
# ADPME Congo — management/commands/corriger_textes.py — v1
# Corrige dans la base les textes déjà chargés (pages, blocs d'accueil,
# parcours) selon les règles éditoriales de l'ADPME :
#   - l'ADPME ne crée pas d'entreprises : elle accompagne leur formalisation ;
#   - le diagnostic porte sur l'entreprise, pas sur le projet ;
#   - cible prioritaire : porteurs d'idées et de projets, dirigeants d'entreprises.
# Remplacements ciblés, phrase par phrase : le reste du texte (et vos
# modifications faites dans l'admin) n'est pas touché. Sans risque si relancée.
#   py manage.py corriger_textes            -> applique les corrections
#   py manage.py corriger_textes --simuler  -> affiche ce qui serait modifié
# ==========================================================================
from django.core.management.base import BaseCommand

from adpme.models import BlocAccueil, Page, Parcours

REMPLACEMENTS = [
    # Création -> formalisation
    ("pour soutenir leur création, leur formalisation et leur développement.",
     "pour soutenir leur formalisation et leur développement."),
    ("visant à favoriser la <strong>création et le développement des entreprises</strong>",
     "visant à favoriser la <strong>formalisation et le développement des entreprises</strong>"),
    ("les procédures de création et de formalisation d'entreprises",
     "les procédures de formalisation des entreprises"),
    ("depuis la création jusqu'au développement et à la consolidation des activités.",
     "depuis la formalisation jusqu'au développement et à la consolidation des activités."),
    ("Suivi et accompagnement post-création", "Suivi et accompagnement de l'entreprise"),
    ("Après la création ou le renforcement de l'entreprise,", "Après la formalisation ou le renforcement de l'entreprise,"),
    ("nécessaires à la création, à la gestion et au développement durable",
     "nécessaires à la formalisation, à la gestion et au développement durable"),
    ("Favoriser la création et le développement des très petites,",
     "Favoriser la formalisation et le développement des très petites,"),
    ("de la création de l'entreprise à sa formalisation et à son développement.",
     "de la formalisation de l'entreprise à son développement."),
    ("Vous souhaitez créer votre activité.", "Vous avez une idée ou un projet d'entreprise."),
    # Diagnostic : l'entreprise, pas le projet
    ("Diagnostic du projet ou de l'entreprise", "Diagnostic de l'entreprise"),
    ("évaluer la maturité du projet ou de l'entreprise", "évaluer la maturité de l'entreprise"),
    # Cible prioritaire
    ("Elle accompagne les porteurs de projets, les entrepreneurs et les artisans grâce à une "
     "offre intégrée d'orientation, de renforcement des capacités et d'appui au financement,",
     "Elle accompagne les porteurs d'idées et de projets ainsi que les dirigeants d'entreprises "
     "grâce à une offre intégrée d'orientation, de renforcement des capacités et d'appui au financement,"),
]

CHAMPS = [
    (Page, ["titre", "intro", "contenu", "meta_description"]),
    (BlocAccueil, ["surtitre", "titre", "texte", "points"]),
    (Parcours, ["titre", "description"]),
]


class Command(BaseCommand):
    help = "Corrige les textes déjà enregistrés (création -> formalisation, diagnostic, cible)."

    def add_arguments(self, parser):
        parser.add_argument("--simuler", action="store_true", help="N'enregistre rien, affiche seulement.")

    def handle(self, *args, **options):
        total = 0
        for modele, champs in CHAMPS:
            for objet in modele.objects.all():
                modifies = []
                for champ in champs:
                    valeur = getattr(objet, champ) or ""
                    nouvelle = valeur
                    for ancien, nouveau in REMPLACEMENTS:
                        nouvelle = nouvelle.replace(ancien, nouveau)
                    if nouvelle != valeur:
                        setattr(objet, champ, nouvelle)
                        modifies.append(champ)
                if modifies:
                    total += 1
                    if not options["simuler"]:
                        objet.save(update_fields=modifies)
                    self.stdout.write(self.style.SUCCESS(
                        f"{'à corriger' if options['simuler'] else 'corrigé'} : "
                        f"{modele._meta.verbose_name} « {objet} » ({', '.join(modifies)})"))
        if not total:
            self.stdout.write("Aucun texte à corriger.")


            