# ==========================================================================
# ADPME Congo — management/commands/charger_programmes.py — v1
# Crée ou met à jour les fiches programmes à partir des documents de l'ADPME.
#   py manage.py charger_programmes
# Sans risque si on la relance : chaque programme est retrouvé par son titre
# et mis à jour (pas de doublon). Les images se rajoutent ensuite dans l'admin.
# Sources : appel à candidatures SYB (2026), article FADPME 2e cohorte
# (mars 2026), article « Caravane de l'entrepreneuriat ».
# ==========================================================================
from django.core.management.base import BaseCommand

from adpme.models import Programme

PROGRAMMES = [
    {
        "titre": "Start Your Business (SYB)",
        "ordre": 1,
        "icone": "formation",
        "public_cible": "Jeunes porteurs de projets de 18 à 40 ans",
        "resume": (
            "Programme d'incubation de l'ADPME qui forme et accompagne les jeunes "
            "de 18 à 40 ans, de l'idée au lancement de leur entreprise : formation "
            "à l'entrepreneuriat, formation métier, coaching et kit de démarrage."
        ),
        "contenu": """
<h2>Le programme</h2>
<p><strong>Start Your Business</strong> est le programme d'incubation de l'ADPME. Il donne aux jeunes porteurs d'idées et de projets les compétences nécessaires pour créer et lancer une entreprise viable.</p>
<p>Il repose sur un principe simple : un projet se développe mieux lorsque son promoteur bénéficie d'appuis variés et d'un accompagnement de proximité jusqu'à l'installation de son entreprise, et lorsqu'il échange avec d'autres entrepreneurs. Le programme s'appuie sur la méthodologie <strong>GERME</strong>, pour laquelle l'ADPME est habilitée.</p>

<h2>Ce que comprend l'accompagnement</h2>
<ol>
<li><strong>Une formation à l'entrepreneuriat</strong> : les modules GERME « Trouver votre idée d'entreprise » (TRIE) et « Créer votre entreprise » (CREE), complétés par l'éducation financière, l'éducation à la citoyenneté, le leadership et l'informatique (Word et Excel). Étude de marché, risques financiers, stratégie commerciale, gestion, ressources humaines, financement : les fondamentaux pour lancer son projet et rédiger son plan d'affaires.</li>
<li><strong>Une formation technique</strong> dans la filière choisie, complétée par une <strong>immersion en entreprise</strong> pour se mettre en situation réelle et finaliser son plan d'affaires.</li>
<li><strong>Un suivi et un coaching individuels</strong> de 1 à 3 mois, avec une mise en relation avec des partenaires (financiers, investisseurs, fournisseurs, clients) pour obtenir un financement et lancer concrètement l'activité.</li>
<li><strong>Un kit de démarrage</strong> : intrants, matériels et équipements adaptés au projet, dans la limite d'un plafond fixé par l'ADPME.</li>
</ol>

<h2>Filières de la première cohorte</h2>
<table>
<thead><tr><th>Filière</th><th>Durée (formation et immersion)</th><th>Places</th></tr></thead>
<tbody>
<tr><td>Aviculture (poulets de chair, poules pondeuses, autres volailles)</td><td>3 mois</td><td>25</td></tr>
<tr><td>Porciculture</td><td>3 mois</td><td>25</td></tr>
<tr><td>Pisciculture (tilapia, clarias…)</td><td>3 mois</td><td>25</td></tr>
<tr><td>Fabrication de provende (aliment de bétail)</td><td>2 mois</td><td>25</td></tr>
<tr><td>Production végétale (maïs, fruits et légumes, champignons)</td><td>2 mois</td><td>20</td></tr>
</tbody>
</table>

<h2>Qui peut candidater ?</h2>
<ul>
<li>être de nationalité congolaise et âgé de 18 à 40 ans ;</li>
<li>avoir au moins le niveau BEPC ;</li>
<li>avoir une idée de projet précise dans l'une des filières retenues, et une expérience ou des connaissances dans ce domaine ;</li>
<li>savoir utiliser un ordinateur, notamment Word et Excel ;</li>
<li>être disponible pendant toute la durée de la formation ;</li>
<li>réaliser son projet à Brazzaville ou dans un rayon de 200 km.</li>
</ul>
<p>Une première expérience entrepreneuriale, même non réussie, est un atout.</p>

<h2>Comment les projets sont sélectionnés</h2>
<ul>
<li>l'originalité du projet ;</li>
<li>la capacité à passer rapidement de l'idée à l'action ;</li>
<li>la création d'emplois et la valeur ajoutée (transformation, valorisation des savoir-faire et des ressources locales) ;</li>
<li>la connaissance du cadre légal et technique de l'activité.</li>
</ul>

<h2>Candidater</h2>
<p>Les candidatures sont ouvertes lors des appels publiés par l'ADPME sur ce site et sur sa page Facebook. Pour tout renseignement, rendez-vous à la Direction générale de l'ADPME (à côté de l'hôtel Mickael's, centre-ville de Brazzaville) ou appelez le 22 613 54 32, du lundi au vendredi de 9 h à 16 h.</p>
""",
    },
    {
        "titre": "FADPME — Fonds d'Appui au Développement des TPME",
        "ordre": 2,
        "icone": "monnaie",
        "public_cible": "TPME, artisans et coopératives",
        "resume": (
            "Le Fonds d'Appui au Développement des Très Petites, Petites et Moyennes "
            "Entreprises équipe les entreprises congolaises pour moderniser leur "
            "production, améliorer leurs performances et renforcer leur compétitivité."
        ),
        "contenu": """
<h2>Le fonds</h2>
<p>Le <strong>Fonds d'Appui au Développement des Très Petites, Petites et Moyennes Entreprises (FADPME)</strong> accompagne l'émergence d'entreprises plus solides, plus performantes et mieux préparées aux défis économiques. Il dote les entreprises locales des moyens techniques nécessaires à leur croissance.</p>

<h2>Ce que le fonds apporte</h2>
<p>Les entreprises retenues reçoivent des <strong>équipements</strong> qui leur permettent de :</p>
<ul>
<li>moderniser leurs unités de production ;</li>
<li>améliorer leurs performances opérationnelles ;</li>
<li>renforcer leur compétitivité sur leurs marchés.</li>
</ul>

<h2>La deuxième cohorte en chiffres</h2>
<p>Le 14 mars 2026, au PEFACO Hôtel Maya Maya, le FADPME a remis officiellement des équipements à <strong>101 entreprises</strong> congolaises.</p>
<table>
<thead><tr><th>Répartition</th><th>Entreprises</th><th>Part</th></tr></thead>
<tbody>
<tr><td>Hommes</td><td>62</td><td>61,4 %</td></tr>
<tr><td>Femmes</td><td>39</td><td>38,6 %</td></tr>
<tr><td>Artisans</td><td>61</td><td>60,4 %</td></tr>
<tr><td>Entreprises individuelles et établissements</td><td>21</td><td>20,8 %</td></tr>
</tbody>
</table>
<p>Principaux secteurs représentés : l'<strong>agrobusiness</strong> (35 projets, 34,7 %), le <strong>tourisme et l'artisanat</strong> (20 projets, 19,8 %), le <strong>commerce général</strong> (16 projets, 15,8 %) et les <strong>technologies de l'information et de la communication</strong> (4 projets, 4 %).</p>

<h2>Se renseigner</h2>
<p>Pour connaître les conditions d'accès au fonds et les prochaines sessions, contactez l'ADPME.</p>
""",
    },
    {
        "titre": "Caravane de l'entrepreneuriat",
        "ordre": 3,
        "icone": "lieu",
        "public_cible": "Porteurs de projets et entrepreneurs",
        "resume": (
            "Programme itinérant de l'ADPME qui va à la rencontre des porteurs de "
            "projets et des entrepreneurs dans les départements pour les informer, "
            "les orienter et les conseiller au plus près de chez eux."
        ),
        "contenu": """
<h2>Le programme</h2>
<p>La <strong>Caravane de l'entrepreneuriat</strong> est un programme itinérant de l'ADPME. Elle rapproche l'accompagnement des porteurs de projets et des entrepreneurs déjà en activité, sur l'ensemble du territoire national.</p>
<p>Ses objectifs : renforcer la culture entrepreneuriale, faciliter l'accès à l'information et encourager la formalisation des activités économiques, en tenant compte des réalités de chaque localité.</p>

<h2>Ce que la Caravane propose sur place</h2>
<ul>
<li>des séances de sensibilisation et d'information ;</li>
<li>de l'orientation et des conseils personnalisés ;</li>
<li>l'enrôlement des porteurs de projets et des entrepreneurs dans les dispositifs de l'ADPME ;</li>
<li>l'identification des besoins en formation et en accompagnement, et des opportunités économiques locales.</li>
</ul>

<h2>Les étapes déjà réalisées</h2>
<p><strong>Corridor nord :</strong> Kintélé, Ngo, Djambala, Gamboma, Owando, Ewo, Oyo, Ouesso, Pokola, Impfondo et Epena.</p>
<p><strong>Corridor sud :</strong> Dolisie et Kibangou. Cette phase donne la priorité aux entrepreneurs déjà enrôlés, afin qu'ils bénéficient d'abord des appuis directs prévus par les dispositifs de l'ADPME.</p>

<h2>La suite</h2>
<p>La Caravane va s'étendre progressivement à d'autres localités, tout en poursuivant l'accompagnement des bénéficiaires déjà enrôlés.</p>
""",
    },
]


class Command(BaseCommand):
    help = "Crée ou met à jour les fiches programmes de l'ADPME (SYB, FADPME, Caravane)."

    def handle(self, *args, **options):
        for donnees in PROGRAMMES:
            donnees = dict(donnees)
            titre = donnees.pop("titre")
            donnees["contenu"] = donnees["contenu"].strip()
            programme, cree = Programme.objects.update_or_create(titre=titre, defaults=donnees)
            etat = "créé" if cree else "mis à jour"
            self.stdout.write(self.style.SUCCESS(f"{etat} : {programme.titre}  ->  /programme/{programme.slug}/"))

            