# ==========================================================================
# ADPME Congo — utilitaires/generer_favicons.py — v1
# Génère les icônes du site (onglet du navigateur, résultats Google et Bing,
# écran d'accueil des téléphones) à partir du logo officiel.
#
# ==========================================================================
from pathlib import Path

from PIL import Image

RACINE = Path(__file__).resolve().parent.parent
LOGO = RACINE / "adpme" / "static" / "assets" / "images" / "logo" / "adpme.png"
SORTIE = RACINE / "adpme" / "static" / "v3" / "icones"

# Partie haute du logo : le bloc « adPME » avec le drapeau, sans la mention
# « Agence de développement… » (illisible en très petit).
SEUIL_MENTION = 0.62     # la mention commence à 62 % de la hauteur du logo
MARGE = 0.03             # marge blanche autour du bloc, en part du côté


def bloc_principal(logo):
    haut = logo.crop((0, 0, logo.width, int(logo.height * SEUIL_MENTION)))
    cadre = haut.getbbox()          # zone réellement dessinée (hors transparence)
    return haut.crop(cadre)


def carre(bloc, cote, fond=(255, 255, 255, 255)):
    """Bloc centré sur un carré blanc de `cote` pixels."""
    utile = int(cote * (1 - 2 * MARGE))
    ratio = min(utile / bloc.width, utile / bloc.height)
    taille = (max(1, round(bloc.width * ratio)), max(1, round(bloc.height * ratio)))
    image = bloc.resize(taille, Image.LANCZOS)
    toile = Image.new("RGBA", (cote, cote), fond)
    toile.alpha_composite(image, ((cote - taille[0]) // 2, (cote - taille[1]) // 2))
    return toile


def main():
    SORTIE.mkdir(parents=True, exist_ok=True)
    bloc = bloc_principal(Image.open(LOGO).convert("RGBA"))

    # PNG carrés : Google demande un multiple de 48 px (48, 96, 144, 192…)
    for cote in (48, 96, 192, 512):
        carre(bloc, cote).save(SORTIE / f"icone-{cote}.png", optimize=True)

    # Icône des téléphones Apple (fond blanc, sans transparence)
    carre(bloc, 180).convert("RGB").save(SORTIE / "apple-touch-icon.png", optimize=True)

    # favicon.ico classique (plusieurs tailles dans un seul fichier)
    carre(bloc, 256).save(SORTIE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    for fichier in sorted(SORTIE.iterdir()):
        print(f"créé : {fichier.relative_to(RACINE)}")


if __name__ == "__main__":
    main()


