# Processing des donn&#233;es

## Introduction
Comment traiter les donn&#233;es pour les rendre utilisables par un programme.

### Chargement des objets
On remarque plusieurs choses :
- Les objets sont charg&#233;s dans un TOC (Table Of Content) qui est un dictionnaire.
- Chaque objet dans la TOC contient un nom, une date de dernière mise à jour et un chemin vers le fichier.
- Le chemin vers le fichier est relatif au dossier de la TOC.
- Ce chemin est similaire à l'attribut @id dans l'ontologie DataTourisme
ex:
```json
  {
    "label": "La Maison de Chateaubriand",
    "lastUpdateDatatourisme": "2023-02-22T06:42:37.658Z",
    "file": "0/00/13-00006084-c3d9-3d90-8a22-e0a70f5c119a.json"
  }
```
L'attribut @id du fichier correspondant :
```json
"@id": "https://data.datatourisme.fr/13/00006084-c3d9-3d90-8a22-e0a70f5c119a"
```
Cela permet de choisir cette donnée comme clé de l'objet dans la la table Places et d'utiliser
l'attribut lastUpdateDatatourisme pour vérifier si il est nécessaire de mettre à jour l'objet.

En cas de non-nécéssité de mise à jour, on peut passer l'enregistrement sans avoir eu à ouvrir le fichier.

Chaque chemin est constitué:
- d'un caractère hexadécimal (0-9, a-f)
- d'un dossier de deux caractères hexadécimaux
- d'un fichier de 36 caractères hexadécimaux

L'attribut @id de l'ontologie DataTourisme est constitué:
- d'un préfixe https://data.datatourisme.gouv.fr/
- d'un dossier de deux chiffres
- d'un fichier nommé avec les mêmes 34 caractères hexadécimaux

Il faut donc 
1. Supprimer les 2 premiers niveaux d'arborescence
2. extraire les 2 premiers chiffres (qui se retrouveront dans l'url de @id)
3. extraire les 34 caractères hexadécimaux (qui se retrouveront dans le nom du fichier)

on peut utiliser une expression régulière pour cela:
```python
import re

regex = r"[a-f0-9]{1}/[a-f0-9]{2}/([0-9]{2})-([a-f0-9-]*)\.json"
test_str = "0/00/13-00006084-c3d9-3d90-8a22-e0a70f5c119a.json"

subst = "https://data.datatourisme.fr/\\g<1>/\\g<2>"
result = re.sub(regex, subst, test_str, 0)

if result:
    print (result)


```


