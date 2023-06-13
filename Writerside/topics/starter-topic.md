# Bienvenue sur %product%

<!--Writerside adds this topic when you create a new documentation project.
You can use it as a sandbox to play with Writerside features, and remove it from the TOC when you don't need it anymore.-->

## Récolte des données
[DATAtourisme](https://www.datatourisme.gouv.fr/) est une plateforme qui permet de récolter des données touristiques de différentes sources. 
* Nous avons choisi de travailler sur les données de la ville de Paris et de ses environs. 
* Nous avons donc récupéré les données de la zone sur le site de DATAtourisme. 
* Nous avons récupéré les données en format JSON, CSV et turtle.

[Data Discovery](Datatourisme-Ontology-Overview.md)

![Itinary DB.png](../../artifacts/ItinaryDB.png)
[DB Diagramme](https://dbdiagram.io/d/64887fb9722eb77494e43a40)

## Consommation de la donnée 
Appliquer le clustering pour pouvoir faire des trajets dans les clusters, le but ce serait d’arriver à avoir un trajet, ensuite il faut visualiser un trajet via Dash. 

Ils pourront récupérer le travail d’un groupe précédent pour la partie clustering. 


## Mise en production
Ils pourront dès lors coupler leur dashboard avec une API pour pouvoir utiliser la base de données Neo4j. 

Il faudra aussi utiliser Docker pour containeriser tous les micro services

For example, this is how you inject a procedure:

<procedure title="Inject a procedure" id="inject-a-procedure">
    <step>
        <p>Start typing and select a procedure type from the completion suggestions:</p>
        <img src="completion_procedure.png" alt="completion suggestions for procedure" border-effect="line"/>
    </step>
    <step>
        <p>Press <shortcut>Tab</shortcut> or <shortcut>Enter</shortcut> to insert the markup.</p>
    </step>
</procedure>

## Automatisation du flux de la donnée 
ÉTAPE FACULTATIVE

Les activités sont actualisées, c’est pourquoi il faut scraper de manière régulière pour avoir une application à jour et utile.


### Tabs
To add switchable content, you can make use of tabs (inject them by starting to type `tab` on a new line):

<tabs>
    <tab title="Markdown">
        <code-block lang="plain text">![Alt Text](new_topic_options.png){ width=450 }</code-block>
    </tab>
    <tab title="Semantic markup">
        <code-block lang="xml">
            <![CDATA[<img src="new_topic_options.png" alt="Alt text" width="450px"/>]]></code-block>
    </tab>
</tabs>

### Collapsible blocks
Apart from injecting entire XML elements, you can use attributes to configure the behavior of certain elements.
For example, you can collapse a chapter that contains non-essential information:

#### Supplementary info {collapsible="true"}
Content under such header will be collapsed by default, but you can modify the behavior by adding the following attribute:
`default-state="expanded"`

### Convert selection to XML
If you need to extend an element with more functions, you can convert selected content from Markdown to semantic markup.
For example, if you want to merge cells in a table, it's much easier to convert it to XML than do this in Markdown.
Position the caret anywhere in the table and press <shortcut>Alt+Enter</shortcut>:

<img src="convert_table_to_xml.png" alt="Convert table to XML" width="706" border-effect="line"/>
