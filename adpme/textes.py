# ==========================================================================
# ADPME Congo — textes.py — v3
# Registre des « Textes du site » modifiables dans l'admin.
#
# Chaque entrée : "clé": (page, libellé affiché dans l'admin, texte par défaut)
#   - Dans un gabarit : {% load ui %} puis {% texte "accueil.cta_titre" %}
#   - Après chaque `py manage.py migrate`, les textes manquants sont créés
#     automatiquement dans l'admin avec leur valeur par défaut. Une valeur déjà
#     modifiée dans l'admin n'est jamais écrasée.
#   - Si un texte est vidé dans l'admin, la valeur par défaut ci-dessous revient.
# ==========================================================================
from .navigation import MENU_PRINCIPAL

PAGES = [
    ("general", "Général (en-tête, pied de page, référencement)"),
    ("menu", "Menu de navigation"),
    ("accueil", "Page d'accueil"),
    ("dispositifs", "Page « Dispositifs d'accompagnement »"),
    ("communs", "Libellés communs (boutons, encadrés)"),
    ("programmes", "Pages « Programmes »"),
    ("actualites", "Pages « Actualités »"),
    ("ressources", "Pages « FAQ » et « Documents »"),
    ("contact", "Page « Contact » et formulaire"),
    ("recherche", "Page « Recherche »"),
    ("agence", "Pages de l'agence et des services, discours"),
    ("opportunites", "Pages « Opportunités » (offres, emplois, appels)"),
    ("newsletter", "Lettre d'information (inscription, désinscription)"),
]

TEXTES = {
    # ── Général ──────────────────────────────────────────────────────────
    "general.titre_suffixe": ("general", "Suffixe ajouté au titre des pages (onglet du navigateur)", "ADPME Congo"),
    "general.meta_description": ("general", "Description par défaut pour Google (160 caractères maximum)",
        "L'ADPME accompagne les porteurs d'idées et de projets et les dirigeants de TPME dans la formalisation, "
        "le développement et la pérennisation de leurs entreprises — Brazzaville, République du Congo."),
    "general.partage_titre": ("general", "Titre par défaut lors d'un partage sur les réseaux sociaux",
        "ADPME — Agence de Développement des TPME"),
    "general.partage_description": ("general", "Description par défaut lors d'un partage sur les réseaux sociaux",
        "L'ADPME accompagne les porteurs d'idées et de projets et les dirigeants de TPME dans la formalisation "
        "et le développement de leurs entreprises au Congo."),
    "general.bouton_contact": ("general", "En-tête : bouton de contact", "Nous contacter"),
    "general.recherche_placeholder": ("general", "En-tête : texte d'exemple du champ de recherche",
        "Rechercher une page, une actualité, une question…"),
    "general.menu_aide_titre": ("general", "Menu déroulant : titre de l'encadré d'aide", "Besoin d'un renseignement ?"),
    "general.menu_aide_bouton": ("general", "Menu déroulant : bouton de l'encadré d'aide", "Écrire à l'agence"),
    "general.pied_acces": ("general", "Pied de page : titre de la colonne des liens directs", "Accès directs"),
    "general.pied_qr_titre": ("general", "Pied de page : titre du QR code", "Le site sur mobile"),
    "general.pied_qr_texte": ("general", "Pied de page : texte sous le QR code",
        "Scannez ce code pour ouvrir le site sur votre téléphone."),
    "general.pied_mention": ("general", "Pied de page : mention après le nom de l'agence", "République du Congo"),

    # ── Libellés communs ─────────────────────────────────────────────────
    "communs.aside_titre": ("communs", "Colonne latérale : titre de l'encadré de contact", "Besoin d'un renseignement ?"),
    "communs.aside_bouton": ("communs", "Colonne latérale : bouton de l'encadré de contact", "Nous contacter"),
    "communs.chiffres_surtitre": ("communs", "Bloc « En chiffres » : surtitre", "En chiffres"),
    "communs.chiffres_titre": ("communs", "Bloc « En chiffres » : titre", "L'action de l'agence"),
    "communs.fil_accueil": ("communs", "Fil d'Ariane : premier lien", "Accueil"),
    "communs.en_savoir_plus": ("communs", "Cartes et blocs : lien par défaut", "En savoir plus"),

    # ── Page d'accueil ───────────────────────────────────────────────────
    "accueil.titre_page": ("accueil", "Titre de la page (onglet du navigateur et Google)",
        "ADPME — Agence de Développement des TPME | Congo"),
    "accueil.hero_surtitre": ("accueil", "Bandeau sans slide : surtitre", "République du Congo"),
    "accueil.hero_titre": ("accueil", "Bandeau sans slide : titre",
        "Agence de Développement des Très Petites, Petites et Moyennes Entreprises"),
    "accueil.hero_bouton1": ("accueil", "Bandeau sans slide : premier bouton", "M'informer et m'orienter"),
    "accueil.hero_bouton2": ("accueil", "Bandeau sans slide : second bouton", "Nous contacter"),
    "accueil.acces_titre": ("accueil", "Accès rapides : titre", "Que souhaitez-vous faire ?"),
    "accueil.parcours_surtitre": ("accueil", "Parcours « Vous êtes… » : surtitre", "Votre parcours"),
    "accueil.parcours_titre": ("accueil", "Parcours « Vous êtes… » : titre", "Vous êtes…"),
    "accueil.programmes_surtitre": ("accueil", "Programmes : surtitre", "Nos programmes"),
    "accueil.programmes_titre": ("accueil", "Programmes : titre", "Les programmes portés par l'agence"),
    "accueil.programmes_bouton": ("accueil", "Programmes : bouton", "Tous les programmes"),
    "accueil.mot_lien": ("accueil", "Mot du Directeur général : texte du lien", "Lire le message complet"),
    "accueil.actus_surtitre": ("accueil", "Actualités : surtitre", "Actualités"),
    "accueil.actus_titre": ("accueil", "Actualités : titre", "Les dernières nouvelles de l'agence"),
    "accueil.actus_bouton": ("accueil", "Actualités : bouton", "Toutes les actualités"),
    "accueil.partenaires_surtitre": ("accueil", "Partenaires : surtitre", "Ils nous accompagnent"),
    "accueil.partenaires_titre": ("accueil", "Partenaires : titre", "Nos partenaires"),
    "accueil.cta_titre": ("accueil", "Appel à l'action (bas de page) : titre", "Un projet, une question ?"),
    "accueil.cta_texte": ("accueil", "Appel à l'action : texte",
        "Écrivez-nous, appelez l'agence ou consultez les questions fréquentes."),
    "accueil.cta_bouton1": ("accueil", "Appel à l'action : premier bouton", "Nous contacter"),
    "accueil.cta_bouton2": ("accueil", "Appel à l'action : second bouton", "Consulter la FAQ"),

    # ── Dispositifs d'accompagnement ─────────────────────────────────────
    "dispositifs.titre_page": ("dispositifs", "Titre de la page (onglet du navigateur et Google)",
        "Dispositifs d'accompagnement des TPME au Congo — ADPME"),
    "dispositifs.meta_description": ("dispositifs", "Description pour Google",
        "Information, conseil, accompagnement, formation et programmes : tous les dispositifs de l'ADPME pour "
        "formaliser, structurer et développer votre entreprise au Congo."),
    "dispositifs.titre": ("dispositifs", "Titre principal", "Dispositifs d'accompagnement"),
    "dispositifs.intro": ("dispositifs", "Introduction sous le titre",
        "Information, conseil, accompagnement, formation et programmes : l'ensemble des appuis de l'ADPME pour "
        "formaliser, structurer et développer votre entreprise au Congo."),
    "dispositifs.stat_services": ("dispositifs", "Compteur : libellé des services", "services d'appui"),
    "dispositifs.stat_etapes": ("dispositifs", "Compteur : libellé des étapes", "étapes de parcours"),
    "dispositifs.stat_programmes": ("dispositifs", "Compteur : libellé des programmes", "programmes"),
    "dispositifs.services_surtitre": ("dispositifs", "Offre de services : surtitre", "Notre offre"),
    "dispositifs.services_titre": ("dispositifs", "Offre de services : titre",
        "Des services adaptés à chaque étape de votre projet"),
    "dispositifs.services_intro": ("dispositifs", "Offre de services : introduction",
        "Que vous ayez une idée, un projet en cours ou une entreprise à développer, l'ADPME vous propose des "
        "services non financiers adaptés à votre situation."),
    "dispositifs.etapes_surtitre": ("dispositifs", "Parcours : surtitre", "Votre parcours"),
    "dispositifs.etapes_titre": ("dispositifs", "Parcours : titre", "Un accompagnement en 7 étapes"),
    "dispositifs.etapes_intro": ("dispositifs", "Parcours : introduction",
        "De l'accueil à la consolidation de votre entreprise, un parcours personnalisé selon vos besoins."),
    "dispositifs.etapes_bouton": ("dispositifs", "Parcours : bouton", "Le processus en détail"),
    "dispositifs.programmes_surtitre": ("dispositifs", "Programmes : surtitre", "Programmes"),
    "dispositifs.programmes_titre": ("dispositifs", "Programmes : titre", "Les programmes portés par l'agence"),
    "dispositifs.ressources_surtitre": ("dispositifs", "Ressources : surtitre", "Ressources"),
    "dispositifs.ressources_titre": ("dispositifs", "Ressources : titre", "Pour aller plus loin"),
    "dispositifs.res_formation_titre": ("dispositifs", "Ressource « Formation » : titre", "Formation et animation entrepreneuriale"),
    "dispositifs.res_formation_texte": ("dispositifs", "Ressource « Formation » : texte",
        "Ateliers pratiques, séminaires et formations de proximité pour renforcer vos compétences."),
    "dispositifs.res_documents_titre": ("dispositifs", "Ressource « Documents » : titre", "Documents à télécharger"),
    "dispositifs.res_documents_texte": ("dispositifs", "Ressource « Documents » : texte",
        "Textes, guides pratiques, formulaires et rapports publiés par l'agence."),
    "dispositifs.res_formation_lien": ("dispositifs", "Ressource « Formation » : texte du lien", "Découvrir les formations"),
    "dispositifs.res_documents_lien": ("dispositifs", "Ressource « Documents » : texte du lien", "Consulter les documents"),
    "dispositifs.res_faq_lien": ("dispositifs", "Ressource « FAQ » : texte du lien", "Lire la FAQ"),
    "dispositifs.res_faq_titre": ("dispositifs", "Ressource « FAQ » : titre", "Questions fréquentes"),
    "dispositifs.res_faq_texte": ("dispositifs", "Ressource « FAQ » : texte",
        "Les réponses aux questions les plus souvent posées à l'ADPME."),
    "dispositifs.cta_titre": ("dispositifs", "Appel à l'action : titre", "Prêt à vous faire accompagner ?"),
    "dispositifs.cta_texte": ("dispositifs", "Appel à l'action : texte",
        "Présentez-nous votre projet : l'ADPME vous oriente vers le dispositif le plus adapté."),
    "dispositifs.cta_bouton1": ("dispositifs", "Appel à l'action : premier bouton", "Nous contacter"),
    "dispositifs.cta_bouton2": ("dispositifs", "Appel à l'action : second bouton", "M'informer et m'orienter"),

    # ── Programmes ───────────────────────────────────────────────────────
    "programmes.titre_page": ("programmes", "Liste : titre de la page (onglet du navigateur et Google)", "Programmes"),
    "programmes.meta_description": ("programmes", "Liste : description pour Google",
        "Les programmes portés par l'ADPME pour accompagner les porteurs d'idées et de projets et les dirigeants "
        "de TPME en République du Congo."),
    "programmes.titre": ("programmes", "Liste : titre principal", "Programmes"),
    "programmes.intro": ("programmes", "Liste : introduction",
        "Les programmes portés par l'agence pour les porteurs d'idées et de projets et les dirigeants d'entreprises."),
    "programmes.vide_texte": ("programmes", "Liste : message s'il n'y a aucun programme",
        "Les programmes de l'agence seront bientôt présentés sur cette page."),
    "programmes.vide_bouton": ("programmes", "Liste : bouton s'il n'y a aucun programme", "Se renseigner auprès de l'agence"),
    "programmes.fiche_public": ("programmes", "Fiche : titre « public concerné »", "Public concerné"),
    "programmes.fiche_site": ("programmes", "Fiche : bouton vers le site du programme", "Site du programme"),
    "programmes.fiche_bouton": ("programmes", "Fiche : bouton de contact", "Se renseigner"),
    "programmes.autres_surtitre": ("programmes", "Fiche : surtitre des autres programmes", "Programmes"),
    "programmes.autres_titre": ("programmes", "Fiche : titre des autres programmes", "Autres programmes"),

    # ── Actualités ───────────────────────────────────────────────────────
    "actualites.titre_page": ("actualites", "Liste : titre de la page (onglet du navigateur et Google)", "Actualités"),
    "actualites.meta_description": ("actualites", "Liste : description pour Google",
        "Les actualités de l'ADPME : programmes, formations, événements et accompagnement des entrepreneurs "
        "en République du Congo."),
    "actualites.titre": ("actualites", "Liste : titre principal", "Actualités"),
    "actualites.intro": ("actualites", "Liste : introduction",
        "Les nouvelles de l'agence : programmes, formations, événements et rencontres avec les entrepreneurs."),
    "actualites.filtre_toutes": ("actualites", "Liste : filtre « toutes les catégories »", "Toutes"),
    "actualites.vide": ("actualites", "Liste : message s'il n'y a aucune actualité", "Aucune actualité publiée pour le moment."),
    "actualites.vide_categorie": ("actualites", "Liste : message si la catégorie choisie est vide",
        "Aucune actualité publiée dans cette catégorie pour le moment."),
    "actualites.carte_lien": ("actualites", "Carte d'actualité : texte du lien", "Lire l'article"),
    "actualites.partage_titre": ("actualites", "Article : titre du bloc de partage", "Partager cet article"),
    "actualites.copier_lien": ("actualites", "Article : bouton « copier le lien »", "Copier le lien"),
    "actualites.retour": ("actualites", "Article : lien de retour vers la liste", "Toutes les actualités"),
    "actualites.lies_surtitre": ("actualites", "Article : surtitre des articles liés", "À lire aussi"),
    "actualites.lies_titre": ("actualites", "Article : titre des articles liés", "D'autres actualités"),

    # ── FAQ et documents ─────────────────────────────────────────────────
    "ressources.faq_titre_page": ("ressources", "FAQ : titre de la page (onglet du navigateur et Google)", "Questions fréquentes"),
    "ressources.faq_meta_description": ("ressources", "FAQ : description pour Google",
        "Les réponses aux questions les plus posées à l'ADPME : services, programmes, accompagnement des entrepreneurs."),
    "ressources.faq_titre": ("ressources", "FAQ : titre principal", "Questions fréquentes"),
    "ressources.faq_intro": ("ressources", "FAQ : introduction", "Les réponses aux questions les plus souvent posées à l'agence."),
    "ressources.faq_filtre": ("ressources", "FAQ : libellé du champ de recherche", "Rechercher dans les questions"),
    "ressources.faq_filtre_exemple": ("ressources", "FAQ : texte d'exemple du champ de recherche", "Ex. : formation, financement…"),
    "ressources.faq_aucune": ("ressources", "FAQ : message si la recherche ne donne rien",
        "Aucune question ne correspond. Posez-nous directement votre question :"),
    "ressources.faq_aucune_bouton": ("ressources", "FAQ : bouton si la recherche ne donne rien", "Nous contacter"),
    "ressources.faq_vide": ("ressources", "FAQ : message s'il n'y a aucune question", "Les questions fréquentes seront bientôt publiées."),
    "ressources.docs_titre_page": ("ressources", "Documents : titre de la page (onglet du navigateur et Google)",
        "Documents à télécharger"),
    "ressources.docs_meta_description": ("ressources", "Documents : description pour Google",
        "Textes, guides pratiques, formulaires et rapports de l'ADPME à télécharger."),
    "ressources.docs_titre": ("ressources", "Documents : titre principal", "Documents à télécharger"),
    "ressources.docs_intro": ("ressources", "Documents : introduction",
        "Textes, guides pratiques, formulaires et rapports publiés par l'agence."),
    "ressources.docs_tous": ("ressources", "Documents : filtre « toutes les catégories »", "Tous"),
    "ressources.docs_vide": ("ressources", "Documents : message s'il n'y a aucun document", "Aucun document publié pour le moment."),

    # ── Contact ──────────────────────────────────────────────────────────
    "contact.titre_page": ("contact", "Titre de la page (onglet du navigateur et Google)", "Contact"),
    "contact.meta_description": ("contact", "Description pour Google",
        "Contactez l'ADPME à Brazzaville : formulaire, téléphone, adresse et horaires d'accueil."),
    "contact.titre": ("contact", "Titre principal", "Nous contacter"),
    "contact.intro": ("contact", "Introduction", "Une question, un projet ? Écrivez-nous ou venez nous rencontrer."),
    "contact.form_titre": ("contact", "Formulaire : titre", "Écrire à l'agence"),
    "contact.form_obligatoire": ("contact", "Formulaire : mention des champs obligatoires",
        "Les champs marqués d'un astérisque (*) sont obligatoires."),
    "contact.champ_nom": ("contact", "Formulaire : libellé du nom", "Nom complet"),
    "contact.champ_nom_exemple": ("contact", "Formulaire : exemple dans le champ nom", "Votre nom complet"),
    "contact.champ_email": ("contact", "Formulaire : libellé de l'e-mail", "Adresse e-mail"),
    "contact.champ_email_exemple": ("contact", "Formulaire : exemple dans le champ e-mail", "Votre adresse e-mail"),
    "contact.champ_sujet": ("contact", "Formulaire : libellé du sujet", "Sujet"),
    "contact.champ_sujet_exemple": ("contact", "Formulaire : exemple dans le champ sujet", "Sujet de votre message"),
    "contact.champ_message": ("contact", "Formulaire : libellé du message", "Message"),
    "contact.champ_message_exemple": ("contact", "Formulaire : exemple dans le champ message", "Votre message…"),
    "contact.form_bouton": ("contact", "Formulaire : bouton d'envoi", "Envoyer le message"),
    "contact.message_succes": ("contact", "Message affiché après un envoi réussi",
        "Votre message a bien été envoyé. Nous vous répondrons dans les plus brefs délais."),
    "contact.message_erreur": ("contact", "Message affiché si l'envoi échoue",
        "Une erreur est survenue lors de l'envoi. Veuillez réessayer ou nous contacter directement par téléphone."),
    "contact.coord_titre": ("contact", "Coordonnées : titre", "Coordonnées"),
    "contact.coord_adresse": ("contact", "Coordonnées : libellé de l'adresse", "Adresse"),
    "contact.coord_telephone": ("contact", "Coordonnées : libellé du téléphone", "Téléphone"),
    "contact.coord_whatsapp": ("contact", "Coordonnées : libellé de WhatsApp", "WhatsApp"),
    "contact.coord_email": ("contact", "Coordonnées : libellé de l'e-mail", "E-mail"),
    "contact.coord_horaires": ("contact", "Coordonnées : libellé des horaires", "Horaires d'accueil"),
    "contact.reseaux": ("contact", "Coordonnées : titre des réseaux sociaux", "Suivez l'agence"),
    "contact.carte_titre": ("contact", "Carte : description (lecteurs d'écran)", "Plan d'accès à la Direction générale de l'ADPME"),
    "contact.antennes_surtitre": ("contact", "Antennes : surtitre", "Près de chez vous"),
    "contact.antennes_titre": ("contact", "Antennes : titre", "Nos antennes"),
    "contact.antennes_itineraire": ("contact", "Antennes : bouton d'itinéraire", "Itinéraire"),

    # ── Recherche ────────────────────────────────────────────────────────
    "recherche.titre_page": ("recherche", "Titre de la page (onglet du navigateur)", "Recherche"),
    "recherche.titre": ("recherche", "Titre principal", "Rechercher sur le site"),
    "recherche.bouton": ("recherche", "Bouton de recherche", "Rechercher"),
    "recherche.aucun": ("recherche", "Message si aucun résultat (suivi du mot cherché)", "Aucun résultat pour"),
    "recherche.groupe_pages": ("recherche", "Titre du groupe « pages »", "Pages"),
    "recherche.groupe_actualites": ("recherche", "Titre du groupe « actualités »", "Actualités"),
    "recherche.groupe_faq": ("recherche", "Titre du groupe « questions »", "Questions fréquentes"),
    "recherche.groupe_documents": ("recherche", "Titre du groupe « documents »", "Documents"),
    "recherche.groupe_offres": ("recherche", "Titre du groupe « opportunités »", "Opportunités"),
    "recherche.suggestion": ("recherche", "Message de suggestion si aucun résultat", "Essayez un autre mot, ou consultez directement :"),
    "recherche.lien_faq": ("recherche", "Suggestion : bouton FAQ", "La FAQ"),
    "recherche.lien_actualites": ("recherche", "Suggestion : bouton actualités", "Les actualités"),
    "recherche.lien_contact": ("recherche", "Suggestion : bouton contact", "Nous contacter"),

    # ── Pages de l'agence et discours ────────────────────────────────────
    "agence.mis_a_jour": ("agence", "Pages : mention de date (suivie de la date)", "Mis à jour le"),
    "agence.mot_dg": ("agence", "Titre de la page « Mot du Directeur général »", "Mot du Directeur général"),
    "agence.mot_ministre": ("agence", "Titre de la page « Mot de la Ministre »", "Mot de la Ministre"),

    # ── Opportunités ─────────────────────────────────────────────────────
    "opportunites.titre_page": ("opportunites", "Liste : titre de la page (onglet du navigateur et Google)", "Opportunités"),
    "opportunites.meta_description": ("opportunites", "Liste : description pour Google",
        "Appels d'offres, offres d'emploi et de stage, appels à candidatures : les opportunités publiées par "
        "l'ADPME en République du Congo."),
    "opportunites.titre": ("opportunites", "Liste : titre principal", "Opportunités"),
    "opportunites.intro": ("opportunites", "Liste : introduction",
        "Appels d'offres, offres d'emploi et de stage, appels à candidatures : retrouvez ici les opportunités "
        "publiées par l'agence."),
    "opportunites.onglet_toutes": ("opportunites", "Onglet « toutes les opportunités »", "Toutes"),
    "opportunites.type_appel_offres": ("opportunites", "Nom de la rubrique « appels d'offres »", "Appels d'offres"),
    "opportunites.type_emploi": ("opportunites", "Nom de la rubrique « emplois et stages »", "Emplois et stages"),
    "opportunites.type_candidature": ("opportunites", "Nom de la rubrique « appels à candidatures »", "Appels à candidatures"),
    "opportunites.statut_en_cours": ("opportunites", "Filtre « en cours »", "En cours"),
    "opportunites.statut_cloturees": ("opportunites", "Filtre « clôturées »", "Clôturées"),
    "opportunites.badge_ouverte": ("opportunites", "Étiquette d'une opportunité ouverte", "Ouvert"),
    "opportunites.badge_close": ("opportunites", "Étiquette d'une opportunité clôturée", "Clôturé"),
    "opportunites.date_limite": ("opportunites", "Libellé de la date limite", "Date limite"),
    "opportunites.publie_le": ("opportunites", "Libellé de la date de publication", "Publié le"),
    "opportunites.reference": ("opportunites", "Libellé de la référence", "Référence"),
    "opportunites.lieu": ("opportunites", "Libellé du lieu", "Lieu"),
    "opportunites.vide_en_cours": ("opportunites", "Message s'il n'y a aucune opportunité en cours",
        "Aucune opportunité en cours dans cette rubrique pour le moment."),
    "opportunites.vide_cloturees": ("opportunites", "Message s'il n'y a aucune opportunité clôturée",
        "Aucune opportunité clôturée dans cette rubrique."),
    "opportunites.vide_newsletter": ("opportunites", "Invitation à s'inscrire quand la liste est vide",
        "Inscrivez-vous à la lettre d'information, en bas de page, pour être informé des prochaines publications."),
    "opportunites.carte_lien": ("opportunites", "Liste : texte du lien vers le détail", "Voir le détail"),
    "opportunites.fiche_infos": ("opportunites", "Fiche : titre de l'encadré d'informations", "En bref"),
    "opportunites.fiche_modalites": ("opportunites", "Fiche : titre de la section « comment postuler »", "Comment postuler"),
    "opportunites.fiche_document": ("opportunites", "Fiche : bouton de téléchargement du dossier", "Télécharger le dossier"),
    "opportunites.fiche_lien": ("opportunites", "Fiche : bouton vers le lien externe", "Consulter l'annonce en ligne"),
    "opportunites.fiche_contact": ("opportunites", "Fiche : libellé de l'e-mail de contact", "Contact"),
    "opportunites.fiche_close": ("opportunites", "Fiche : message quand l'opportunité est clôturée",
        "Cette opportunité est clôturée : les candidatures et offres ne sont plus acceptées."),
    "opportunites.fiche_retour": ("opportunites", "Fiche : lien de retour vers la liste", "Toutes les opportunités"),
    "opportunites.autres_surtitre": ("opportunites", "Fiche : surtitre des autres opportunités", "Opportunités"),
    "opportunites.autres_titre": ("opportunites", "Fiche : titre des autres opportunités", "Autres opportunités en cours"),

    # ── Lettre d'information ─────────────────────────────────────────────
    "newsletter.titre": ("newsletter", "Pied de page : titre du bloc d'inscription", "Restez informé"),
    "newsletter.texte": ("newsletter", "Pied de page : texte du bloc d'inscription",
        "Recevez les appels à candidatures, les opportunités et les actualités de l'ADPME."),
    "newsletter.champ": ("newsletter", "Champ e-mail : texte d'exemple", "Votre adresse e-mail"),
    "newsletter.bouton": ("newsletter", "Bouton d'inscription", "S'inscrire"),
    "newsletter.mention": ("newsletter", "Mention sous le formulaire",
        "Votre adresse sert uniquement à l'envoi des informations de l'ADPME. Désinscription possible à tout moment."),
    "newsletter.succes": ("newsletter", "Message après une inscription réussie",
        "Merci ! Votre inscription à la lettre d'information de l'ADPME est enregistrée."),
    "newsletter.deja": ("newsletter", "Message si l'adresse est déjà inscrite", "Cette adresse est déjà inscrite. Merci de votre fidélité !"),
    "newsletter.erreur": ("newsletter", "Message si l'adresse est invalide", "Veuillez saisir une adresse e-mail valide."),
    "newsletter.desinscription_titre": ("newsletter", "Désinscription : titre de la page", "Se désinscrire"),
    "newsletter.desinscription_texte": ("newsletter", "Désinscription : question de confirmation",
        "Vous ne recevrez plus la lettre d'information de l'ADPME à l'adresse suivante :"),
    "newsletter.desinscription_bouton": ("newsletter", "Désinscription : bouton de confirmation", "Confirmer la désinscription"),
    "newsletter.desinscription_ok": ("newsletter", "Désinscription : message de confirmation",
        "Votre désinscription est enregistrée. Vous pouvez vous réinscrire à tout moment."),
}


# ── Libellés du menu : générés à partir de navigation.py ────────────────
for _rubrique in MENU_PRINCIPAL:
    if "liens" in _rubrique:
        TEXTES[f"menu.{_rubrique['id']}"] = ("menu", f"Rubrique « {_rubrique['titre']} »", _rubrique["titre"])
        for _lien in _rubrique["liens"]:
            TEXTES[f"menu.{_lien['url']}"] = ("menu", f"{_rubrique['titre']} › {_lien['titre']}", _lien["titre"])
    else:
        TEXTES[f"menu.{_rubrique['url']}"] = ("menu", f"Lien direct « {_rubrique['titre']} »", _rubrique["titre"])


TEXTES["menu.recherche"] = ("menu", "Pied de page › lien vers la recherche", "Recherche")
TEXTES["menu.contact"] = ("menu", "Pied de page › lien vers le contact", "Contact")


def defaut(cle):
    """Texte par défaut d'une clé (chaîne vide si la clé est inconnue)."""
    return TEXTES.get(cle, (None, None, ""))[2]


def texte_admin(cle):
    """Même chose que {% texte %}, depuis le code Python (vues, formulaires) :
    texte saisi dans l'admin s'il existe, sinon texte par défaut."""
    from .models import TexteSite

    valeur = TexteSite.objects.filter(cle=cle).values_list("valeur", flat=True).first()
    return valeur.strip() if valeur and valeur.strip() else defaut(cle)

