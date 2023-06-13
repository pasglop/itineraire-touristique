# itineraire-touristique

## Description
Projet Datascientest by :
- Jean Beuzeval
- Marouen 
- David Delpuech

Documentation du projet : [Documentation](https://pasglop.github.io/itineraire-touristique)

## project Spaces
[Click-Up](https://app.clickup.com/4714782/v/l/s/90030384214)

## Data
* https://diffuseur.datatourisme.fr/fr/flux/16843 
* [flux zippé](raw_data/flux-16843-202305310721.zip)

## Objectif
* Charger les POIs de la région Ile de France dans une base de données Postgres
* Charger les POIs dans une base de données Neo4j
* Créer un dashboard avec les données de la base Postgres
* Créer un modèle de graph avec les données de la base Neo4j (clusterisation, centralité, etc.)
* Créer une interface Web permettant de définir :
* * un point de départ (Hotel, gare, etc.)
* * une durée de séjour
* * un budget ?
* * un type de POI (restaurant, musée, etc.)
* Générer un itinéraire en fonction des critères définis sur plusieurs jours

## Architecture
Dockerfile contient :
* un container postgres
* un container neo4j
* un container python
* un container dash (?)

## Installation
* `git clone
* `cd itineraire-touristique`
* Rename `.env.example` to `.env` and fill in the values
* `docker-compose up -d`
* PGadmin sur http://localhost:5050/
  * définir le mot de passe master de votre choix (mais s'en souvenir...)
  * Créer un serveur avec les paramètres definis dans .env
* Configure Python environnement:
  * Run `python3 -m venv venv`
  * Run `source venv/bin/activate`
  * Run `pip install -r requirements.txt`
* Run `python3 install/install.py` to load data into Postgres

## Usage
* load data
* update data
* start App