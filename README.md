# adpme-website
```
cd existing_repo
git remote add origin https://gitlab.com/jozykial/caravane-refont.git
git branch -M main
git push -uf origin main

```

## Pour commiter le projet
```
1- git status
2- git add .
3- git commit -m "Nom du commit"
4- git push origin main
```

## Activer le env dans le bash de pythonanywhere
```
source ~/nom_variable_environnement/bin/activate
```

## Commit le projet en ligne sur pythonanywhere
```
1- Accerder à votre dossier dans la console
    - cd ~/path/to/your/project
2- Faites le pull pour intégrer les nouvelles modifications depuis le dépôt distant :
    - git pull origin main
3- # (résolvez les conflits si nécessaire)
    - git add .
4- Commiter et enoyer les mises à jour
    - git commit -m "Votre message de commit"
    - git push origin main

```

## suppression de la base de données SQLite
rm db.sqlite3

## Supprimer tous les fichiers de migrations sauf __init__.py
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```
## Supprimer les migrations d'une application
```
del utilisateur\migrations\0*.py
```

# Variante : Solution sans supprimer toute la base (si déjà en prod)
## Si vous ne pouvez pas supprimer les migrations ou la base :
```
py manage.py migrate utilisateur zero
py manage.py migrate admin zero

```

## Recréer la base de données et appliquer les migrations
```
python manage.py makemigrations
python manage.py migrate

```

## Exporter la base SQLite vers Mysql
### 1 exporter la base sqlite vers json
python manage.py dumpdata --natural-primary --natural-foreign --indent 4 > data.json

```
Cela va générer un fichier data.json contenant toutes les données de ta base SQLite.
```

### 2 appliquer les migrations
python manage.py migrate

### 3 importer les données
python manage.py loaddata data.json

## Pour installer les dépendances existante dans le requirements
pip install -r requirements.txt

## Supprimer un environnement pour en crée un autre
```
Si l'environnement .env a été créé avec l'ancien Python, il ne fonctionnera plus. 
Supprime-le et recrée-le avec la version actuelle de Python.

rd /s /q .env
python -m venv .env

Puis active-le
```

## Réinitialiser les dépendance
```
Si tu as un fichier requirements.txt, installe les packages :

pip install -r requirements.txt

```
## Déploiement Manuel via SSH
```
1- cd /home/votre_nom_utilisateur/caravane_app # Remplacez par le chemin réel
2- git pull origin master # Ou le nom de votre branche principale
3- Redémarrez votre application web (si c'est une application web) depuis l'onglet "Web" de votre tableau de bord PythonAnywhere

```
