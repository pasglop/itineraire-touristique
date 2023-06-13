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



A definition list or a glossary:

First Term
: This is the definition of the first term.

Second Term
: This is the definition of the second term.
