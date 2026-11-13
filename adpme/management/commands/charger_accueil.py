# ==========================================================================
# ADPME Congo — management/commands/charger_accueil.py — v1
# Crée les 4 blocs éditoriaux de la page d'accueil (modèle BlocAccueil).
#   py manage.py charger_accueil            -> crée les blocs manquants
#   py manage.py charger_accueil --ecraser  -> remplace aussi les blocs existants
# Textes rédigés à partir du contenu officiel de l'ADPME (page Présentation,
# services, programme SYB). Les images s'ajoutent ensuite dans l'admin.
# ==========================================================================
from django.core.management.base import BaseCommand

from adpme.models import BlocAccueil

BLOCS = [
    {
        "cle": "presentation",
        "surtitre": "Qui sommes-nous ?",
        "titre": "L'agence au service des TPME congolaises",
        "texte": (
            "L'Agence de Développement des Très Petites, Petites et Moyennes Entreprises (ADPME) "
            "coordonne et harmonise les actions publiques en faveur des TPME en République du Congo. "
            "Elle accompagne les porteurs de projets, les entrepreneurs et les artisans grâce à une "
            "offre intégrée d'orientation, de renforcement des capacités et d'appui au financement, "
            "de la création de l'entreprise à sa formalisation et à son développement."
        ),
        "points": "",
        "bouton_texte": "Découvrir l'agence",
        "bouton_lien": "/a-propos/",
    },
    {
        "cle": "missions",
        "surtitre": "Missions de l'ADPME",
        "titre": "Quelles sont nos missions ?",
        "texte": (
            "Favoriser la création et le développement des très petites, petites et moyennes "
            "entreprises du Congo grâce à une offre intégrée de services non financiers. "
            "À ce titre, l'ADPME est chargée de :"
        ),
        "points": "\n".join([
            "Coordonner et harmoniser les interventions de soutien aux TPME",
            "Faire connaître les opportunités d'investissement et d'affaires, y compris la reprise d'entreprises",
            "Aider à la formalisation et au démarrage des entreprises, notamment par l'élaboration du plan d'affaires",
            "Accompagner les TPME dans la recherche de financement",
            "Former les porteurs de projets, les dirigeants et les employés des TPME",
            "Diffuser les technologies performantes et les résultats de la recherche utiles aux TPME",
            "Prévenir les difficultés des entreprises accompagnées par des mécanismes d'alerte, de suivi et de redressement",
            "Labelliser les bénéficiaires et certifier les partenaires de l'accompagnement",
        ]),
        "bouton_texte": "En savoir plus sur l'agence",
        "bouton_lien": "/a-propos/",
    },
    {
        "cle": "priorites",
        "surtitre": "Nos priorités",
        "titre": "Quelles sont nos priorités ?",
        "texte": "",
        "points": "\n".join([
            "Stimuler l'esprit d'entreprise et l'innovation",
            "Faciliter l'accès des TPME au financement",
            "Accroître la productivité et la compétitivité des entreprises",
            "Renforcer les capacités managériales des dirigeants de TPME",
        ]),
        "bouton_texte": "",
        "bouton_lien": "",
    },
    {
        "cle": "competences",
        "surtitre": "Renforcement des capacités",
        "titre": "Développez vos compétences",
        "texte": (
            "Ateliers pratiques, séminaires, formations de proximité et coaching : l'ADPME renforce "
            "les compétences des porteurs de projets et des dirigeants de TPME, au plus près des "
            "réalités économiques locales."
        ),
        "points": "\n".join([
            "Culture entrepreneuriale et gestion d'entreprise",
            "Élaboration du plan d'affaires et formalisation",
            "Accès au financement, productivité et compétitivité",
            "Méthodologie GERME et coaching individuel avec le programme SYB",
        ]),
        "badge_image": "Programme SYB",
        "legende": "Incubation des jeunes porteurs de projets",
        "bouton_texte": "Voir les dispositifs d'accompagnement",
        "bouton_lien": "/dispositifs-accompagnement/",
    },
]


class Command(BaseCommand):
    help = "Crée les blocs éditoriaux de la page d'accueil (présentation, missions, priorités, compétences)."

    def add_arguments(self, parser):
        parser.add_argument("--ecraser", action="store_true",
                            help="Remplace aussi les blocs déjà présents dans l'admin (les images sont conservées).")

    def handle(self, *args, **options):
        for donnees in BLOCS:
            donnees = dict(donnees)
            cle = donnees.pop("cle")
            existe = BlocAccueil.objects.filter(cle=cle).exists()
            if existe and not options["ecraser"]:
                self.stdout.write(f"déjà présent (non modifié) : {cle}")
                continue
            BlocAccueil.objects.update_or_create(cle=cle, defaults=donnees)
            self.stdout.write(self.style.SUCCESS(f"{'remplacé' if existe else 'créé'} : {cle}"))

