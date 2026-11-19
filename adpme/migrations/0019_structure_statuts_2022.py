# ==========================================================================
# ADPME Congo — migrations/0019_structure_statuts_2022.py — v1
# Contenu initial de l'organigramme : directions, services et missions,
# repris tels quels des statuts de l'ADPME approuvés par le décret
# n° 2022-96 du 2 mars 2022 (Journal officiel n° 10-2022 du 10 mars 2022,
# pages 246 à 248). Seules les coquilles typographiques du JO sont corrigées.
# Ne s'exécute qu'une fois ; ensuite tout se modifie dans l'admin
# (Organigramme). Si l'organigramme contient déjà des données, rien n'est fait.
# ==========================================================================
from django.db import migrations

TC = "très petites, petites et moyennes entreprises"

DIRECTIONS = [
    {
        "nom": "Direction des analyses, études et documentation",
        "slug": "direction-analyses-etudes-documentation",
        "icone": "graphique",
        "reference": "Statuts, articles 29 et 30",
        "presentation": "La direction des analyses, études et documentation est dirigée et animée par un directeur.",
        "missions": [
            "réaliser les études et analyses globales et sectorielles ;",
            f"collecter et analyser les données relatives aux besoins et performances des {TC} ;",
            f"assurer le suivi d'exécution des programmes d'appui aux {TC} ;",
            "réaliser et faire réaliser les études de faisabilité de projet, des plans d'affaires, ainsi que "
            "les programmes d'appui à l'entrepreneuriat ;",
            "contribuer à la mise en place et au développement des incubateurs, des couveuses, des pépinières "
            "d'entreprises ou tout autre structure similaire ;",
            "concevoir et mettre en œuvre les actions de promotion de l'esprit d'entreprise ;",
            "tenir et publier les statistiques et assurer l'archivage des données et dossiers ;",
            "gérer le fonds documentaire technique ;",
            "gérer, et mettre à disposition des usagers toute information et documentation générales ou "
            "spécifiques relatives aux opportunités d'investissement, à la gestion d'entreprise et à la "
            "vulgarisation des technologies.",
        ],
        "services": [
            "Service des études, analyses et statistiques",
            "Service de la documentation",
        ],
    },
    {
        "nom": "Direction de l'assistance technologique",
        "slug": "direction-assistance-technologique",
        "icone": "ampoule",
        "reference": "Statuts, articles 31 et 32",
        "presentation": "La direction de l'assistance technologique est dirigée et animée par un directeur.",
        "missions": [
            f"identifier les besoins en technologie des {TC} ;",
            "contribuer à la vulgarisation, la promotion et la diffusion des résultats de la recherche, des "
            f"innovations et des technologies adaptées aux besoins des {TC} ;",
            f"conseiller et accompagner les {TC} dans leurs choix des technologies ;",
            "négocier les partenariats et le réseautage avec les centres de recherche, d'essai, de démonstration "
            "et d'appui nationaux et internationaux ;",
            f"accompagner les {TC} dans la valorisation des ressources locales.",
        ],
        "services": [
            "Service de la promotion et mise à niveau technologique",
            "Service de suivi des performances technologiques",
        ],
    },
    {
        "nom": "Direction de l'assistance en gestion",
        "slug": "direction-assistance-gestion",
        "icone": "poignee",
        "reference": "Statuts, articles 33 et 34",
        "presentation": "La direction de l'assistance en gestion est dirigée et animée par un directeur.",
        "missions": [
            f"conseiller, assister et accompagner les porteurs de projets, les créateurs et les dirigeants des {TC} ;",
            f"suivre les {TC} bénéficiaires de l'appui financier des pouvoirs publics ;",
            "définir et mettre en œuvre, en collaboration avec les intervenants compétents, les mécanismes de "
            f"suivi, de prévention, d'alerte et, en cas de difficultés, de redressement des {TC} ;",
            f"certifier et labelliser les structures privées d'appui, d'accompagnement et d'assistance aux {TC} ;",
            f"assister et accompagner les {TC} dans la recherche des financements ;",
            f"contribuer à la recherche et au développement des marchés au profit des {TC} ;",
            f"promouvoir les partenaires et le réseautage des {TC}.",
        ],
        "services": [
            "Service d'appui et conseil",
            "Service de suivi des organismes d'appui privé",
        ],
    },
    {
        "nom": "Direction de l'administration et des ressources humaines",
        "slug": "direction-administration-ressources-humaines",
        "icone": "utilisateurs",
        "reference": "Statuts, articles 35 et 36",
        "presentation": "La direction de l'administration et des ressources humaines est dirigée et animée par un directeur.",
        "missions": [
            "gérer les ressources financières ;",
            "organiser et coordonner l'ensemble des activités administratives ;",
            "assurer le traitement et le suivi des dossiers juridiques ;",
            "veiller aux bonnes relations professionnelles et les promouvoir ;",
            "participer à l'élaboration et veiller à la bonne mise en œuvre des contrats, conventions, "
            "protocoles, mémorandums d'entente ;",
            "participer à l'élaboration des dossiers d'appels d'offres, à la négociation et à l'exécution des "
            "accords de coopération et de partenariat ;",
            "représenter l'agence dans ses relations avec les tribunaux, les organismes et établissements de "
            "l'emploi et de sécurité sociale ainsi qu'avec les autres commissions spécialisées.",
        ],
        "services": [
            "Service administratif et juridique",
            "Service des ressources humaines",
        ],
    },
    {
        "nom": "Direction des finances et de la comptabilité",
        "slug": "direction-finances-comptabilite",
        "icone": "monnaie",
        "reference": "Statuts, articles 37 et 38",
        "presentation": "La direction des finances et de la comptabilité est dirigée et animée par un directeur.",
        "missions": [
            "assurer l'approvisionnement en moyens généraux ;",
            "procéder au recouvrement des différentes ressources financières appartenant ou allouées à l'agence ;",
            "gérer le patrimoine ;",
            "tenir la comptabilité et arrêter les comptes ;",
            "établir les bilans, les états financiers et comptables ainsi que les états de synthèse ;",
            "élaborer et exécuter les budgets annuels et les plans pluriannuels de financement ;",
            "gérer la trésorerie et les finances ;",
            "représenter l'agence dans ses relations avec le trésor public, les établissements bancaires et de "
            "crédit ainsi que les partenaires financiers ;",
            "participer à l'élaboration des dossiers d'appels d'offres ainsi qu'à la négociation et l'exécution "
            "des accords financiers.",
        ],
        "services": [
            "Service des finances",
            "Service de la comptabilité",
        ],
    },
]

# Structures rattachées à la Direction générale (statuts, articles 25 à 28)
RATTACHES = [
    ("Secrétariat de direction", "secretariat-direction", "document", "Statuts, article 26"),
    ("Service de la communication et des relations publiques", "service-communication-relations-publiques",
     "message", "Statuts, article 27"),
    ("Service du système d'information", "service-systeme-information", "ordinateur", "Statuts, article 28"),
]

# Directions départementales (organigramme de l'agence ; statuts, article 40)
DEPARTEMENTALES = [
    "Kouilou – Pointe-Noire",
    "Niari",
    "Bouenza – Lékoumou",
    "Djoué-Léfini",
    "Cuvette – Cuvette-Ouest",
    "Plateaux",
    "Congo-Oubangui",
    "Pool – Brazzaville",
    "Sangha – Likouala",
]


def charger(apps, schema_editor):
    Structure = apps.get_model("adpme", "Structure")
    if Structure.objects.exists():
        return

    Structure.objects.create(type_structure="comite", nom="Comité de direction", slug="comite-direction",
                             icone="utilisateurs", ordre=1)
    Structure.objects.create(type_structure="dg", nom="Direction générale", slug="direction-generale",
                             icone="batiment", reference="Statuts, article 25", ordre=2)

    for i, (nom, slug, icone, reference) in enumerate(RATTACHES, start=1):
        Structure.objects.create(type_structure="rattache", nom=nom, slug=slug, icone=icone,
                                 reference=reference, ordre=i)

    for i, d in enumerate(DIRECTIONS, start=1):
        direction = Structure.objects.create(
            type_structure="direction", nom=d["nom"], slug=d["slug"], icone=d["icone"],
            reference=d["reference"], presentation=d["presentation"],
            missions="\n".join(d["missions"]), ordre=i * 10,
        )
        for j, service in enumerate(d["services"], start=1):
            Structure.objects.create(type_structure="service", nom=service, parent=direction,
                                     slug=f"{d['slug']}-service-{j}", ordre=i * 10 + j)

    Structure.objects.create(
        type_structure="comptable", nom="Agence comptable", slug="agence-comptable", icone="document",
        reference="Statuts, article 39",
        presentation="L'agence comptable est régie par des textes spécifiques.", ordre=60,
    )

    for i, nom in enumerate(DEPARTEMENTALES, start=1):
        Structure.objects.create(type_structure="departementale", nom=nom,
                                 slug=f"direction-departementale-{i}", icone="lieu", ordre=100 + i)


def vider(apps, schema_editor):
    apps.get_model("adpme", "Structure").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("adpme", "0018_structure"),
    ]

    operations = [
        migrations.RunPython(charger, vider),
    ]

    