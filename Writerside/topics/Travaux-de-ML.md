# Travaux de ML

l'objectif de ces travaux est de mettre en place une clusterisation des POIs en fonction d'une journée de visite commencant à 9h et finissant à 20h.

## 1. Préparation des données
On va charger les données depuis un export de la base de données de l'application. On va ensuite les préparer pour pouvoir les utiliser dans un algorithme de clusterisation.
Pour cela, on va charger chaque POI en tant que noeud dans un graphe. Chaque noeud aura pour attributs:
- son identifiant
- son nom
- sa latitude
- sa longitude
- adresse
- code postal
- ville
- (son type / sa catégorie) (en attente de la donnée dans la base de données)
- (son temps de visite) v2
- (son temps d'ouverture) v2
- (son temps de fermeture) v2

On va ensuite créer des relations entre les noeuds en fonction de leur distance. On va créer une relation entre deux noeuds si la distance entre eux est inférieure à 500m. La relation aura pour attributs:
- la distance entre les deux noeuds
- le temps de trajet entre les deux noeuds
- le type de transport utilisé pour le trajet

## 2. Algorithme de clusterisation
On va utiliser l'algorithme de clusterisation DBSCAN. Cet algorithme permet de clusteriser des données en fonction de leur proximité. Il est donc adapté à notre cas d'utilisation.
Dans Neo4J, on peut utiliser l'algorithme de clusterisation DBSCAN avec la requête suivante:
```
CALL gds.alpha.ml.dbscan.stream({
  nodeProjection: 'POI',
  relationshipProjection: {
    RELATION: {
      type: 'RELATION',
      orientation: 'UNDIRECTED'
    }
  },
  relationshipWeightProperty: 'distance',
  epsilon: 500,
  minPts: 2,
  includeIntermediateCommunities: true
})

YIELD nodeId, communityId, intermediateCommunityIds
RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds

ORDER BY communityId ASC
```
```cypher
CALL gds.graph.project(
    'itinaries',
    {
      POI: {
        properties: 'coordinates'
      }
    },
    '*'
)
```

```cypher
CALL gds.beta.kmeans.stream('itinaries', {
  nodeProperty: 'coordinates',
  nodeLabels: ['POI'],
  k: 8,
  seedCentroids: [[40.712776,-74.005974]]
})
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).name AS name, communityId
ORDER BY communityId, name ASC
```
## 3. Résultats
On obtient les résultats suivants:

