# ==========================================================================
# ADPME Congo — management/commands/charger_pages.py — v1
# Transfère dans l'admin (modèle Page) le contenu des pages « À propos »,
# « Information et orientation », « Conseil », « Accompagnement » et
# « Formation », repris des anciens gabarits du site (texte de l'ADPME).
#   py manage.py charger_pages            -> crée les pages manquantes
#   py manage.py charger_pages --ecraser  -> remplace aussi les pages existantes
# Par défaut, une page déjà modifiée dans l'admin n'est JAMAIS écrasée.
# ==========================================================================
from django.core.management.base import BaseCommand

from adpme.models import Page

PAGES = [
    {
        "cle": "a-propos",
        "titre": "Présentation de l'ADPME",
        "intro": "L'Agence de Développement des Très Petites, Petites et Moyennes Entreprises du Congo : "
                 "notre mission, notre vision et nos valeurs.",
        "meta_description": "L'ADPME est l'Agence de Développement des Très Petites, Petites et Moyennes "
                            "Entreprises du Congo. Découvrez notre mission, notre vision et nos valeurs.",
        "contenu": """
<h2>Qui sommes-nous ?</h2>
<p>L'Agence de Développement des Très Petites, Petites et Moyennes Entreprises (ADPME) du Congo a pour mission de coordonner et d'harmoniser l'ensemble des actions publiques en faveur des TPME, en offrant un accompagnement intégré alliant <strong>orientation, renforcement de capacités et appui au financement</strong> pour soutenir leur création, leur formalisation et leur développement.</p>

<h2>Notre vision</h2>
<p>À l'horizon 2030, les très petites, petites et moyennes entreprises congolaises sont compétitives, innovantes et constituent des moteurs essentiels de la diversification et de la transformation de l'économie nationale, contribuant durablement à la prospérité du Congo.</p>

<h2>Notre mission</h2>
<p>L'ADPME assure une mission d'encadrement visant à favoriser la <strong>création et le développement des entreprises</strong>. Pour répondre aux besoins de renforcement des capacités des entrepreneurs, elle propose une offre intégrée de <strong>services non financiers</strong>, complémentaires et adaptés aux différentes étapes de vie de l'entreprise ainsi qu'aux divers niveaux de développement des compétences entrepreneuriales.</p>
<p>L'ADPME a pour principales missions de :</p>
<ul>
<li><strong>coordonner et harmoniser les interventions</strong> de soutien et d'accompagnement en faveur des TPME ;</li>
<li><strong>vulgariser les opportunités d'investissement et d'affaires</strong>, y compris la reprise d'entreprises, à partir d'études et d'analyses sectorielles ;</li>
<li><strong>aider à la formalisation et au démarrage des entreprises</strong>, notamment en appuyant l'élaboration des plans d'affaires et autres documents essentiels ;</li>
<li><strong>accompagner les TPME dans la recherche de financement</strong> pour lancer ou développer leurs activités ;</li>
<li><strong>contribuer à la formation</strong> des porteurs de projets, des dirigeants et des employés des TPME ;</li>
<li><strong>vulgariser les technologies performantes</strong> et les résultats de recherche adaptés aux besoins des TPME ;</li>
<li><strong>mettre en œuvre des mécanismes d'alerte, de suivi, de prévention et de redressement</strong> pour les entreprises accompagnées, en coopération avec les acteurs spécialisés ;</li>
<li><strong>mettre en place des dispositifs de labellisation</strong> des bénéficiaires et de certification des partenaires impliqués dans les actions d'accompagnement.</li>
</ul>

<h2>Nos valeurs</h2>
<ul>
<li>Entrepreneuriat et créativité</li>
<li>Accompagnement durable</li>
<li>Professionnalisme</li>
<li>Inclusion sociale et économique</li>
<li>Innovation au service des entreprises</li>
</ul>

<h2>Nos priorités</h2>
<ul>
<li>Stimuler l'esprit d'entreprise et encourager l'innovation</li>
<li>Accroître la productivité et renforcer la compétitivité des entreprises</li>
<li>Améliorer l'accès des MPME aux mécanismes de financement</li>
<li>Développer les capacités managériales et opérationnelles des dirigeants de MPME</li>
</ul>
""",
    },
    {
        "cle": "information",
        "titre": "Information et orientation",
        "intro": "Faciliter l'accès des entrepreneurs aux dispositifs publics et privés d'appui à l'entrepreneuriat.",
        "contenu": """
<p>L'ADPME assure une mission d'<strong>information et d'orientation</strong> afin de faciliter l'accès des entrepreneurs aux dispositifs publics et privés d'appui à l'entrepreneuriat.</p>
<p>Elle met à disposition des informations fiables et actualisées sur :</p>
<ul>
<li>les opportunités économiques ;</li>
<li>les procédures de création et de formalisation d'entreprises ;</li>
<li>les mécanismes de financement ;</li>
<li>les programmes de formation et d'accompagnement existants.</li>
</ul>
<p>Grâce à cette action, l'ADPME oriente les porteurs de projets et les entrepreneurs vers les structures, partenaires et dispositifs les mieux adaptés à leurs besoins, contribuant ainsi à une meilleure lisibilité de l'écosystème entrepreneurial et à une utilisation optimale des ressources disponibles.</p>
""",
    },
    {
        "cle": "conseil",
        "titre": "Conseil",
        "intro": "Des conseils personnalisés pour structurer, améliorer et pérenniser votre activité.",
        "contenu": """
<p>L'ADPME met à la disposition des porteurs de projets et des entrepreneurs des services de <strong>conseil personnalisés</strong>, destinés à les aider à structurer, améliorer et pérenniser leurs activités.</p>
<p>À travers des échanges individualisés, l'agence accompagne les entrepreneurs dans :</p>
<ul>
<li>la clarification de leurs idées ;</li>
<li>l'analyse de la viabilité de leurs projets ;</li>
<li>l'amélioration de leur organisation interne ;</li>
<li>la prise de décisions stratégiques adaptées à leur contexte.</li>
</ul>
<p>Le conseil offert par l'ADPME vise à renforcer la qualité des projets entrepreneuriaux, à réduire les risques liés au lancement ou au développement des entreprises et à favoriser une gestion plus efficace et durable des très petites, petites et moyennes entreprises.</p>
""",
    },
    {
        "cle": "accompagnement",
        "titre": "Accompagnement",
        "intro": "Un processus structuré et progressif, de l'idée d'entreprise à la consolidation des activités.",
        "contenu": """
<p>L'accompagnement constitue un pilier central de l'action de l'ADPME. Il s'agit d'un processus structuré et progressif qui soutient les entrepreneurs à chaque étape de la vie de leur entreprise, depuis la création jusqu'au développement et à la consolidation des activités.</p>
<p>Cet accompagnement comprend le renforcement des capacités entrepreneuriales, le suivi technique, l'appui à la formalisation, l'amélioration des performances économiques et l'accès aux mécanismes de financement et d'appui matériel.</p>
<p>À travers une approche de proximité, l'ADPME œuvre à transformer les porteurs de projets et les entreprises accompagnées en acteurs économiques compétitifs, capables de contribuer durablement à la diversification et au développement de l'économie nationale.</p>

<h2>Le processus d'accompagnement</h2>
<p>L'accompagnement s'adapte aux besoins des porteurs de projets et des entrepreneurs, depuis l'idée d'entreprise jusqu'à la consolidation des activités.</p>

<h3>1. Accueil, information et orientation</h3>
<p>Le processus débute par l'accueil des porteurs de projets et des entrepreneurs. À cette étape, l'ADPME fournit des informations générales sur l'entrepreneuriat, identifie les besoins exprimés et oriente les bénéficiaires vers les dispositifs et services d'appui les plus adaptés à leur situation.</p>

<h3>2. Diagnostic du projet ou de l'entreprise</h3>
<p>L'ADPME réalise un diagnostic afin d'évaluer la maturité du projet ou de l'entreprise, les capacités techniques et managériales de l'entrepreneur, ainsi que les forces, faiblesses et opportunités de développement. Cette analyse permet de définir un parcours d'accompagnement personnalisé.</p>

<h3>3. Conseil et structuration</h3>
<p>Sur la base du diagnostic, l'ADPME apporte un appui en matière de conseil pour la structuration du projet ou de l'entreprise : élaboration ou amélioration du plan d'affaires, organisation de l'activité, clarification du modèle économique et préparation à la formalisation.</p>

<h3>4. Formation et renforcement des capacités</h3>
<p>Les bénéficiaires participent à des actions de formation ciblées visant à renforcer leurs compétences entrepreneuriales, techniques et managériales. Ces formations répondent aux besoins identifiés et améliorent la performance et la durabilité des entreprises.</p>

<h3>5. Appui à la formalisation et à l'accès aux dispositifs</h3>
<p>L'ADPME accompagne les entrepreneurs dans les démarches de formalisation de leurs activités et facilite leur accès aux dispositifs publics et privés d'appui, notamment les mécanismes de financement et les programmes de soutien au développement des entreprises.</p>

<h3>6. Suivi et accompagnement post-création</h3>
<p>Après la création ou le renforcement de l'entreprise, l'ADPME assure un suivi technique et un accompagnement continu. Cette étape permet d'évaluer les progrès réalisés, d'anticiper les difficultés et d'apporter des solutions adaptées pour consolider les activités.</p>

<h3>7. Appui à la croissance et à la pérennisation</h3>
<p>L'ADPME soutient les entreprises dans leur phase de développement à travers des actions ciblées : amélioration de la productivité, innovation, accès aux marchés et montée en compétitivité, afin de favoriser leur pérennisation et leur contribution à l'économie nationale.</p>
""",
    },
    {
        "cle": "formation",
        "titre": "Formation et animation entrepreneuriale",
        "intro": "Renforcer les compétences des porteurs de projets et des entrepreneurs, au plus près des réalités économiques locales.",
        "contenu": """
<p>L'ADPME œuvre au renforcement des capacités des porteurs de projets et des entrepreneurs à travers des actions de <strong>formation et d'animation entrepreneuriale</strong> adaptées aux réalités économiques locales.</p>
<p>Ces actions visent à développer les compétences techniques, managériales et organisationnelles nécessaires à la création, à la gestion et au développement durable des très petites, petites et moyennes entreprises.</p>

<h2>Les thèmes de formation</h2>
<ul>
<li>la culture entrepreneuriale ;</li>
<li>la gestion d'entreprise ;</li>
<li>l'élaboration de plans d'affaires ;</li>
<li>la formalisation ;</li>
<li>l'accès au financement ;</li>
<li>l'amélioration de la productivité et de la compétitivité des entreprises.</li>
</ul>
<p>Elles sont organisées sous forme d'ateliers pratiques, de sessions de sensibilisation, de séminaires et de formations de proximité, favorisant l'apprentissage par l'échange et l'expérience.</p>

<h2>L'animation entrepreneuriale</h2>
<p>À travers l'animation entrepreneuriale, l'ADPME dynamise l'écosystème entrepreneurial en créant des espaces de dialogue, de partage d'expériences et de mise en réseau entre entrepreneurs, partenaires institutionnels et acteurs du secteur privé.</p>
<p>Cette approche contribue à stimuler l'esprit d'initiative, à encourager l'innovation et à accompagner l'émergence d'entreprises performantes, capables de jouer un rôle actif dans la diversification et la transformation de l'économie nationale.</p>
""",
    },
]


class Command(BaseCommand):
    help = "Crée les pages de contenu (À propos, services) à partir du texte de l'ancien site."

    def add_arguments(self, parser):
        parser.add_argument("--ecraser", action="store_true",
                            help="Remplace aussi les pages déjà présentes dans l'admin.")

    def handle(self, *args, **options):
        for donnees in PAGES:
            donnees = dict(donnees)
            cle = donnees.pop("cle")
            donnees["contenu"] = donnees["contenu"].strip()
            existe = Page.objects.filter(cle=cle).exists()
            if existe and not options["ecraser"]:
                self.stdout.write(f"déjà présente (non modifiée) : {cle}")
                continue
            Page.objects.update_or_create(cle=cle, defaults=donnees)
            self.stdout.write(self.style.SUCCESS(f"{'remplacée' if existe else 'créée'} : {cle}"))


            