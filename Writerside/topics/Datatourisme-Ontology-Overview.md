# Datatourisme Ontology Overview


Dataset listant l’ensemble des activités réalisables dans une commune, on appelle cela un POI (Place/Point of Interest). 


## Structure
Il y a différents formats de fichiers utilisables :
- XML/RDF - turtle : Format de description de données structurées, mixant data et metadata.
- JSON : Format de description de données structurées, plus léger que le XML. Chaque objet est un fichier JSON

[Visualisation d'un exemple de fichier JSON](https://jsoncrack.com/editor?json=6488336f63cfc1b442f457c4)

## Ontology
L’ontologie est un ensemble de règles qui permettent de décrire les données. 
Chaque donnée structurée est décrite par un [ensemble de propriétés](https://www.datatourisme.fr/ontology/core/).

### Espaces de noms utilisés dans le document
|[Ontology NS Prefix]|<https://www.datatourisme.fr/ontology/core>|
|:----|:----|
|schema|<http://schema.org>|
|owl|<http://www.w3.org/2002/07/owl>|
|xsd|<http://www.w3.org/2001/XMLSchema>|
|skos|<http://www.w3.org/2004/02/skos/core>|
|rdfs|<http://www.w3.org/2000/01/rdf-schema>|
|olo|<http://purl.org/ontology/olo/core>|
|rdf|<http://www.w3.org/1999/02/22-rdf-syntax-ns>|
|terms|<http://purl.org/dc/terms>|
|xml|<http://www.w3.org/XML/1998/namespace>|
|ebucore|<http://www.ebu.ch/metadata/ontologies/ebucore/ebucore>|
|foaf|<http://xmlns.com/foaf/0.1>|
|dc|<http://purl.org/dc/elements/1.1>|

### Les Classes
Les classes sont des concepts qui permettent de décrire les données.

## Les Thèmes

Culture
: [#CulturalTheme](https://www.datatourisme.fr/ontology/core#CulturalTheme)

Nom d'itinéraire 
: [#RouteTheme](https://www.datatourisme.fr/ontology/core#RouteTheme)

Style architectural 
: [#ArchitecturalStyle](https://www.datatourisme.fr/ontology/core#ArchitecturalStyle)

Thème d'environnement de POI 
: [#SpatialEnvironmentTheme](https://www.datatourisme.fr/ontology/core#SpatialEnvironmentTheme)

Thème de fête et évènement 
: [#EntertainmentAndEventTheme](https://www.datatourisme.fr/ontology/core#EntertainmentAndEventTheme)

Thème de parc et jardin 
: [#ParkAndGardenTheme](https://www.datatourisme.fr/ontology/core#ParkAndGardenTheme)

Thème de restauration 
: [#FoodEstablishmentTheme](https://www.datatourisme.fr/ontology/core#FoodEstablishmentTheme)

Thème de santé 
: [#HealthTheme](https://www.datatourisme.fr/ontology/core#HealthTheme)

Thèmes d’activité et évènements sport et loisirs 
: [#SportsTheme](https://www.datatourisme.fr/ontology/core#SportsTheme)

Type de cuisine 
: [#CuisineCategory](https://www.datatourisme.fr/ontology/core#CuisineCategory)

Type de mêts 
: [#FoodProduct](https://www.datatourisme.fr/ontology/core#FoodProduct)


## Analyse des données
| Niveau | Titre                            | Type (date, int...)    | Description                                                                                           | SBD Cible          | Commentaire                                                              | Table/collection                       |
|:-------|:---------------------------------|:-----------------------|:------------------------------------------------------------------------------------------------------|:-------------------|:-------------------------------------------------------------------------|:---------------------------------------|
| 1      | @id                              | string                 | url du flux de données correspondant au POI                                                           | PostgreSQL         |                                                                          | places.schema_url                      |
| 1      | dc:identifier                    | int                    | identifiant à 7 chiffres                                                                              | neo4j / PostgreSQL | Clé primaire distribuée                                                  | places.id (PK)                         |
| 1      | @type                            | string list            | liste des catégories dans lequel entre le POI                                                         | PostgreSQL         | besoin de lister toutes les valeurs possibles                            | place_types                            |
| 1      | rdfs:comment                     | dictionnaire string    | clé = langue    valeur = description longue du POI dans la langue choisie                             | PostgreSQL         | redondant hasDescription.shortDescription                                |                                        |
| 1      | rdfs:label                       | dictionnaire string    | clé = "fr"    valeur = type du POI (ex : "Centre aquatique municipal")                                | PostgreSQL         | correspond au label de l'index.json                                      | places.name                            |
| 1      | hasBeenCreatedBy                 | dictionnaire           | url fiche contact créateur                                                                            |                    | redondant avec hasContact                                                |                                        |
| 2      | @id                              | string                 | url datatoursime pour la section "hasBeenCreatedBy"                                                   |                    |                                                                          |                                        |
| 2      | dc:identifier                    | int                    | identifiant à 4 chiffres                                                                              |                    |                                                                          |                                        |
| 2      | schema:email                     | string list            | liste des adresses mail pour contacter l'orgnanisme                                                   |                    |                                                                          |                                        |
| 2      | schema:legalName                 | string                 | nom de l'organisme/site                                                                               |                    |                                                                          |                                        |
| 2      | @type                            | string list            | "schema:Organization", "foaf:Agent", "Agent"                                                          |                    |                                                                          |                                        |
| 2      | foaf:homepage                    | string                 | url de l'organisme                                                                                    |                    |                                                                          |                                        |
| 1      | hasBeenPublishedBy               |                        |                                                                                                       |                    |                                                                          |                                        |
| 2      | @id                              | string                 | url datatoursime pour la section "hasBeenPublishedBy"                                                 |                    |                                                                          |                                        |
| 2      | schema:legalName                 | string                 | nom de l'organisme ayant publié les informations du POI                                               |                    |                                                                          |                                        |
| 2      | @type                            | string list            | "schema:Organization", "foaf:Agent", "Agent"                                                          |                    |                                                                          |                                        |
| 2      | foaf:homepage                    | string                 | url de l'organisme ayant publié les informations du POI                                               |                    |                                                                          |                                        |
| 1      | hasContact                       |                        |                                                                                                       | PostgreSQL         |                                                                          | contacts [FK places.id]                |
| 2      | @id                              | string                 | url datatoursime relatif au contact du site                                                           | PostgreSQL         |                                                                          | contacts.schema_url                    |
| 2      | schema:telephone                 | string                 | n° de telephone                                                                                       | PostgreSQL         | prévoir contacts.email                                                   | contacts.phone                         |
| 2      | @type                            | string list            | "foaf:Agent", "Agent"                                                                                 | PostgreSQL         | Probablement différent type -> listing                                   | contacts.type                          |
| 2      | foaf:homepage                    | string                 | url homepage organisme                                                                                | PostgreSQL         | website dans contacts ou dans places ??                                  | places.website                         |
| 1      | hasDescription                   |                        |                                                                                                       | PostgreSQL         |                                                                          | descriptions [places_id FK, lang, ...] |
| 2      | @id                              |                        | url datatourisme relatif à la description du lieu                                                     | PostgreSQL         |                                                                          | descriptions.schema_url                |
| 2      | @type                            |                        | "Description"                                                                                         |                    |                                                                          |                                        |
| 2      | hasTranslatedProperty            | liste de dictionnaire  | informations relatives à la traduction dans chaque langue                                             |                    |                                                                          |                                        |
| 2      | shortDescription                 | liste de dictionnaire  | clé = langue    valeur = description                                                                  | PostgreSQL         | dans l'ontologie, il n'y a pas de longDesc                               | descriptions.lang                      |
| 1      | hasTheme                         | liste de dictionnaire  | cf [themes](#les-th-mes)                                                                              | PostgreSQL         |                                                                          | themes                                 |
| 1      | hasTranslatedProperty            | liste de dictionnaires | informations relatives à la traduction dans chaque langue                                             |                    |                                                                          |                                        |
| 1      | isLocatedAt                      |                        |                                                                                                       |                    | Adresse & geoloc                                                         |                                        |
| 2      | @id                              |                        | url datatourisme relatif à la localisation                                                            |                    | redondant                                                                |                                        |
| 2      | schema:address                   |                        |                                                                                                       |                    |                                                                          | addresses [FK places.id]               |
| 3      | @id                              | string                 | url datatourisme relatif à l'adresse                                                                  |                    |                                                                          | addresses.schema_url                   |
| 3      | schema:addressLocality           | string                 | nom de l'endroit                                                                                      |                    | ou city ??                                                               | addresses.locality                     |
| 3      | schema:postalCode                | int                    | code postal                                                                                           |                    |                                                                          | addresses.zipcode                      |
| 3      | schema:streetAddress             | string                 | n° et rue                                                                                             |                    |                                                                          | addresses.street                       |
| 3      | @type                            | string list            | type d'adresse (ex : "schema:PostalAddress", "PostalAddress")                                         |                    | redondant                                                                |                                        |
| 3      | hasAddressCity                   |                        |                                                                                                       |                    | Ce niveau de détail est-il nécessaire ? Obligerai à créer une table city |                                        |
| 4      | @id                              |                        | identifiant contenant le numero INSEE de la commune (ex : "kb:78358")                                 |                    |                                                                          |                                        |
| 4      | @type                            |                        | type (ex : ville, village...)                                                                         |                    |                                                                          |                                        |
| 4      | rdfs:label                       | dictionnaire           | clé = langue    valeur = nom de l'organisme                                                           |                    |                                                                          |                                        |
| 4      | insee                            |                        | numero INSEE de la commune                                                                            |                    |                                                                          |                                        |
| 4      | isPartOfDepartment               | dictionnaire           |                                                                                                       |                    |                                                                          |                                        |
| 5      | @id                              | string                 | id relatif au département (ex : "kb:France1178")                                                      |                    |                                                                          |                                        |
| 5      | @type                            | string                 | type = departement                                                                                    |                    |                                                                          |                                        |
| 5      | rdfs:label                       | dictionnaire           | clé = langue     valeur = nom du département                                                          |                    |                                                                          |                                        |
| 5      | insee                            | int                    | numéro INSEE du département (ex : 78)                                                                 |                    |                                                                          |                                        |
| 5      | isPartOfRegion                   | dictionnaire           |                                                                                                       |                    |                                                                          |                                        |
| 6      | @id                              |                        | id relatif à la région (ex : "kb:France11")                                                           |                    |                                                                          |                                        |
| 6      | @type                            |                        | type = Region                                                                                         |                    |                                                                          |                                        |
| 6      | rdfs:label                       |                        | clé = langue    valeur = nom de la région                                                             |                    |                                                                          |                                        |
| 6      | insee                            |                        | numéro INSEE de la région                                                                             |                    |                                                                          |                                        |
| 6      | isPartOfCountry                  | dictionnaire           |                                                                                                       |                    |                                                                          |                                        |
| 7      | @id                              |                        | id relatif au pays (ex : "kb:France")                                                                 |                    |                                                                          |                                        |
| 7      | @type                            |                        | type = "schema:Country"                                                                               |                    |                                                                          |                                        |
| 7      | rdfs:label                       |                        | clé = langue    valeur = nom du pays                                                                  |                    |                                                                          |                                        |
| 2      | schema:geo                       |                        |                                                                                                       |                    | geoloc                                                                   | Attributs des nodes POI                |
| 3      | @id                              | string                 | url datatourisme                                                                                      |                    |                                                                          |                                        |
| 3      | schema:latitude                  | float                  | coordonnées GPS                                                                                       |                    |                                                                          | places.lat                             |
| 3      | schema:longitude                 | float                  | coordonnées GPS                                                                                       |                    |                                                                          | places.long                            |
| 3      | @type                            | string                 | type schema:GeoCoordinates                                                                            |                    |                                                                          |                                        |
| 2      | schema:openingHoursSpecification |                        |                                                                                                       |                    | Peux exister en plusieurs periodes                                       | openings [FK places.id]                |
| 3      | @id                              | string                 | url datatourisme                                                                                      |                    |                                                                          |                                        |
| 3      | schema:validFrom                 | datetime               | "2023-01-01T00:00:00" peut être la période d'ouverture sur une année complète                         |                    |                                                                          | openings.from                          |
| 3      | schema:validThrough              | datetime               | "2023-12-31T23:59:59" peut être la période d'ouverture sur une année complète                         |                    |                                                                          | openings.through                       |
| 3      | schema:opens                     | time                   |                                                                                                       |                    |                                                                          | open,ings.opens                        |
| 3      | schema:closes                    | time                   |                                                                                                       |                    |                                                                          | openings.closes                        |
| 3      | @type                            | string                 | type "schema:OpeningHoursSpecification"                                                               |                    |                                                                          |                                        |
| 2      | @type                            | string                 | type = place                                                                                          |                    |                                                                          |                                        |
| 1      | isOwnedBy                        | dictionnaire           |                                                                                                       |                    | redondant                                                                |                                        |
| 2      | @id                              | string                 | url datatourisme                                                                                      |                    |                                                                          |                                        |
| 2      | schema:email                     | string list            | adresses mail de l'organisme propriétaire                                                             |                    |                                                                          |                                        |
| 2      | schema:legalName                 | string                 | nom du propriètaire du POI                                                                            |                    |                                                                          |                                        |
| 2      | @type                            | string list            | "schema:Organization", "foaf:Agent", "Agent"                                                          |                    |                                                                          |                                        |
| 2      | foaf:homepage                    | string                 | url de l'organisme propriétaire                                                                       |                    |                                                                          |                                        |
| 1      | lastUpdate                       | date                   | date de la dernière mise à jour (de la part de l'orgnansime qui transmet ces données à datatourisme?) |                    | on garde celle qui suit                                                  |                                        |
| 1      | lastUpdateDatatourisme           | datetime               | date de la dernière mise à jour de la part de Datatourisme                                            |                    |                                                                          | places.sourceUpdated                   |


