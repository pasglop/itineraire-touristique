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
Abbaye 
: [Abbey](https://www.datatourisme.fr/ontology/core#Abbey)

Accompagnement 
: [AccompaniedPractice](https://www.datatourisme.fr/ontology/core#AccompaniedPractice)

Adresse postale 
: [PostalAddress](https://www.datatourisme.fr/ontology/core#PostalAddress)

Agence de guides 
: [TourGuideAgency](https://www.datatourisme.fr/ontology/core#TourGuideAgency)

Agent 
: [Agent](https://www.datatourisme.fr/ontology/core#Agent)

Aire de camping-car 
: [CamperVanArea](https://www.datatourisme.fr/ontology/core#CamperVanArea)

Aire de covoiturage 
: [CarpoolArea](https://www.datatourisme.fr/ontology/core#CarpoolArea)

Aire de jeux 
: [PlayArea](https://www.datatourisme.fr/ontology/core#PlayArea)

Aire de pique-nique 
: [PicnicArea](https://www.datatourisme.fr/ontology/core#PicnicArea)

Aire, station de taxis 
: [TaxiStation](https://www.datatourisme.fr/ontology/core#TaxiStation)

Alpage 
: [AlpinePasture](https://www.datatourisme.fr/ontology/core#AlpinePasture)

Animation locale 
: [LocalAnimation](https://www.datatourisme.fr/ontology/core#LocalAnimation)

Annotation 
: [Annotation](https://www.datatourisme.fr/ontology/core#Annotation)

Antiquaire et brocanteur 
: [AntiqueAndSecondhandGoodDealer](https://www.datatourisme.fr/ontology/core#AntiqueAndSecondhandGoodDealer)

Appartement 
: [Apartment](https://www.datatourisme.fr/ontology/core#Apartment)

Aquatique 
: [AquaticLocomotionMode](https://www.datatourisme.fr/ontology/core#AquaticLocomotionMode)

Aqueduc 
: [Aqueduct](https://www.datatourisme.fr/ontology/core#Aqueduct)

Arc de triomphe 
: [TriumphalArch](https://www.datatourisme.fr/ontology/core#TriumphalArch)

Arrêt, station de transport en commun 
: [BusStop](https://www.datatourisme.fr/ontology/core#BusStop)

Artisan d'art 
: [CraftsmanShop](https://www.datatourisme.fr/ontology/core#CraftsmanShop)

Arène 
: [Arena](https://www.datatourisme.fr/ontology/core#Arena)

Atelier de formation 
: [TrainingWorkshop](https://www.datatourisme.fr/ontology/core#TrainingWorkshop)

Auberge de jeunesse et centre international de séjour 
: [YouthHostelAndInternationalCenter](https://www.datatourisme.fr/ontology/core#YouthHostelAndInternationalCenter)

Audience 
: [Audience](https://www.datatourisme.fr/ontology/core#Audience)

Audience de personnes, clients 
: [PeopleAudience](https://www.datatourisme.fr/ontology/core#PeopleAudience)

Auditorium 
: [Auditorium](https://www.datatourisme.fr/ontology/core#Auditorium)

Aérodrôme 
: [Airfield](https://www.datatourisme.fr/ontology/core#Airfield)

Aéroport 
: [Airport](https://www.datatourisme.fr/ontology/core#Airport)

Baptême sportif 
: [FirstPractice](https://www.datatourisme.fr/ontology/core#FirstPractice)

Bar, bar à thème 
: [BarOrPub](https://www.datatourisme.fr/ontology/core#BarOrPub)

Barrage, digue 
: [LevyOrDike](https://www.datatourisme.fr/ontology/core#LevyOrDike)

Base nautique / centre nautique 
: [NauticalCentre](https://www.datatourisme.fr/ontology/core#NauticalCentre)

Basilique 
: [Basilica](https://www.datatourisme.fr/ontology/core#Basilica)

Bastide 
: [Bastide](https://www.datatourisme.fr/ontology/core#Bastide)

Bateau promenade 
: [SightseeingBoat](https://www.datatourisme.fr/ontology/core#SightseeingBoat)

Bateau-restaurant 
: [BoatRestaurant](https://www.datatourisme.fr/ontology/core#BoatRestaurant)

Bibliothèque - Médiathèque 
: [Library](https://www.datatourisme.fr/ontology/core#Library)

Bistrot - Bar à vin 
: [BistroOrWineBar](https://www.datatourisme.fr/ontology/core#BistroOrWineBar)

Bocage 
: [Bocage](https://www.datatourisme.fr/ontology/core#Bocage)

Borne de charge véhicule électrique 
: [ElectricVehicleChargingPoint](https://www.datatourisme.fr/ontology/core#ElectricVehicleChargingPoint)

Borne de charge électrique pour vélo, vtt 
: [ElectricBycicleChargingPoint](https://www.datatourisme.fr/ontology/core#ElectricBycicleChargingPoint)

Borne de service camping car 
: [RVServiceArea](https://www.datatourisme.fr/ontology/core#RVServiceArea)

Borne ou station de réparation - gonflage 
: [GarageOrAirPump](https://www.datatourisme.fr/ontology/core#GarageOrAirPump)

Boulangerie 
: [Bakery](https://www.datatourisme.fr/ontology/core#Bakery)

Boulodrome 
: [BoulesPitch](https://www.datatourisme.fr/ontology/core#BoulesPitch)

Boutique, commerce de proximité 
: [BoutiqueOrLocalShop](https://www.datatourisme.fr/ontology/core#BoutiqueOrLocalShop)

Bowling 
: [BowlingAlley](https://www.datatourisme.fr/ontology/core#BowlingAlley)

Brasserie ou taverne 
: [BrasserieOrTavern](https://www.datatourisme.fr/ontology/core#BrasserieOrTavern)

Brasseur 
: [Brewery](https://www.datatourisme.fr/ontology/core#Brewery)

Brocante 
: [BricABrac](https://www.datatourisme.fr/ontology/core#BricABrac)

Bulle 
: [Bubble](https://www.datatourisme.fr/ontology/core#Bubble)

Bungalow, Mobil Home 
: [Bungalow](https://www.datatourisme.fr/ontology/core#Bungalow)

Bungatoile 
: [Bungatoile](https://www.datatourisme.fr/ontology/core#Bungatoile)

Bureau éxécutif 
: [ExecutiveBoardMeeting](https://www.datatourisme.fr/ontology/core#ExecutiveBoardMeeting)

Bus touristique 
: [TouristBus](https://www.datatourisme.fr/ontology/core#TouristBus)

Bâteau habitable 
: [HouseBoat](https://www.datatourisme.fr/ontology/core#HouseBoat)

Bâtiment civil remarquable 
: [RemarkableBuilding](https://www.datatourisme.fr/ontology/core#RemarkableBuilding)

Cabane 
: [Hut](https://www.datatourisme.fr/ontology/core#Hut)

Cabane dans les arbres 
: [TreeHouse](https://www.datatourisme.fr/ontology/core#TreeHouse)

Cabaret 
: [Cabaret](https://www.datatourisme.fr/ontology/core#Cabaret)

Café ou salon de thé 
: [CafeOrTeahouse](https://www.datatourisme.fr/ontology/core#CafeOrTeahouse)

Cafétéria - Self 
: [SelfServiceCafeteria](https://www.datatourisme.fr/ontology/core#SelfServiceCafeteria)

Calvaire et enclos paroissiaux 
: [Calvary](https://www.datatourisme.fr/ontology/core#Calvary)

Camping 
: [Camping](https://www.datatourisme.fr/ontology/core#Camping)

Camping car 
: [CampingCar](https://www.datatourisme.fr/ontology/core#CampingCar)

Canal 
: [Canal](https://www.datatourisme.fr/ontology/core#Canal)

Canyon 
: [Canyon](https://www.datatourisme.fr/ontology/core#Canyon)

Caravane 
: [Caravan](https://www.datatourisme.fr/ontology/core#Caravan)

Carnaval 
: [Carnival](https://www.datatourisme.fr/ontology/core#Carnival)

Cascade 
: [Waterfall](https://www.datatourisme.fr/ontology/core#Waterfall)

Cascade de glace 
: [Icefall](https://www.datatourisme.fr/ontology/core#Icefall)

Casino 
: [Casino](https://www.datatourisme.fr/ontology/core#Casino)

Cathédrale 
: [Cathedral](https://www.datatourisme.fr/ontology/core#Cathedral)

Causse 
: [Causse](https://www.datatourisme.fr/ontology/core#Causse)

Cave de dégustation 
: [WineCellar](https://www.datatourisme.fr/ontology/core#WineCellar)

Cave ou caveau 
: [Cellar](https://www.datatourisme.fr/ontology/core#Cellar)

Centre d'interprétation 
: [InterpretationCentre](https://www.datatourisme.fr/ontology/core#InterpretationCentre)

Centre de balnéothérapie 
: [BalneotherapyCentre](https://www.datatourisme.fr/ontology/core#BalneotherapyCentre)

Centre de congrès 
: [ConventionCentre](https://www.datatourisme.fr/ontology/core#ConventionCentre)

Centre de remise en forme - fitness 
: [FitnessCenter](https://www.datatourisme.fr/ontology/core#FitnessCenter)

Centre de thalassothérapie 
: [ThalassotherapyCentre](https://www.datatourisme.fr/ontology/core#ThalassotherapyCentre)

Centre de vacances et de loisirs 
: [HolidayCentre](https://www.datatourisme.fr/ontology/core#HolidayCentre)

Centre et galerie commerciale 
: [ShoppingCentreAndGallery](https://www.datatourisme.fr/ontology/core#ShoppingCentreAndGallery)

Centre équestre 
: [EquestrianCenter](https://www.datatourisme.fr/ontology/core#EquestrianCenter)

Chalet 
: [Chalet](https://www.datatourisme.fr/ontology/core#Chalet)

Chalet résidentiel de loisirs 
: [LeisureChalet](https://www.datatourisme.fr/ontology/core#LeisureChalet)

Chambre 
: [Room](https://www.datatourisme.fr/ontology/core#Room)

Chambre d'hôtes 
: [Guesthouse](https://www.datatourisme.fr/ontology/core#Guesthouse)

Chambre de commerce et d'industrie 
: [ChamberOfCommerceAndIndustry](https://www.datatourisme.fr/ontology/core#ChamberOfCommerceAndIndustry)

Chambre et table d'hôtes 
: [TableHoteGuesthouse](https://www.datatourisme.fr/ontology/core#TableHoteGuesthouse)

Chapelle 
: [Chapel](https://www.datatourisme.fr/ontology/core#Chapel)

Chartreuse 
: [Chartreuse](https://www.datatourisme.fr/ontology/core#Chartreuse)

Chaumes 
: [StubbleFields](https://www.datatourisme.fr/ontology/core#StubbleFields)

Château 
: [Castle](https://www.datatourisme.fr/ontology/core#Castle)

Château et demeure de prestige 
: [CastleAndPrestigeMansion](https://www.datatourisme.fr/ontology/core#CastleAndPrestigeMansion)

Château fort 
: [FortifiedCastle](https://www.datatourisme.fr/ontology/core#FortifiedCastle)

Cimetière civil 
: [CivilCemetery](https://www.datatourisme.fr/ontology/core#CivilCemetery)

Cimetière militaire et mémorial 
: [MilitaryCemetery](https://www.datatourisme.fr/ontology/core#MilitaryCemetery)

Cinéma 
: [Cinema](https://www.datatourisme.fr/ontology/core#Cinema)

Cinémathèque 
: [Cinematheque](https://www.datatourisme.fr/ontology/core#Cinematheque)

Circuit automobile ou moto 
: [RacingCircuit](https://www.datatourisme.fr/ontology/core#RacingCircuit)

Cirque 
: [CircusPlace](https://www.datatourisme.fr/ontology/core#CircusPlace)

Cirque naturel 
: [Cirque](https://www.datatourisme.fr/ontology/core#Cirque)

Citadelle 
: [Citadel](https://www.datatourisme.fr/ontology/core#Citadel)

Classement 
: [Review](https://www.datatourisme.fr/ontology/core#Review)

Classement par label 
: [LabelReview](https://www.datatourisme.fr/ontology/core#LabelReview)

Classement par note 
: [ScaleReview](https://www.datatourisme.fr/ontology/core#ScaleReview)

Cloître 
: [Cloister](https://www.datatourisme.fr/ontology/core#Cloister)

Club de plage 
: [BeachClub](https://www.datatourisme.fr/ontology/core#BeachClub)

Club de sport 
: [SportsClub](https://www.datatourisme.fr/ontology/core#SportsClub)

Club enfants 
: [KidsClub](https://www.datatourisme.fr/ontology/core#KidsClub)

Club et village vacances 
: [ClubOrHolidayVillage](https://www.datatourisme.fr/ontology/core#ClubOrHolidayVillage)

Col 
: [Col](https://www.datatourisme.fr/ontology/core#Col)

Collégiale 
: [Collegiate](https://www.datatourisme.fr/ontology/core#Collegiate)

Comité départemental du tourisme 
: [DepartementTourismCommittee](https://www.datatourisme.fr/ontology/core#DepartementTourismCommittee)

Comité régional du tourisme 
: [RegionalTourismCommittee](https://www.datatourisme.fr/ontology/core#RegionalTourismCommittee)

Commanderie 
: [Commanderie](https://www.datatourisme.fr/ontology/core#Commanderie)

Commerce de détail 
: [Store](https://www.datatourisme.fr/ontology/core#Store)

Commune 
: [City](https://www.datatourisme.fr/ontology/core#City)

Commémoration 
: [Commemoration](https://www.datatourisme.fr/ontology/core#Commemoration)

Compagnie de taxis 
: [TaxiCompany](https://www.datatourisme.fr/ontology/core#TaxiCompany)

Complexe de loisirs (loisirs regroupés) 
: [LeisureComplex](https://www.datatourisme.fr/ontology/core#LeisureComplex)

Complèxe ou terrain de tennis 
: [TennisComplex](https://www.datatourisme.fr/ontology/core#TennisComplex)

Compétition 
: [Competition](https://www.datatourisme.fr/ontology/core#Competition)

Compétition sportive 
: [SportsCompetition](https://www.datatourisme.fr/ontology/core#SportsCompetition)

Concert 
: [Concert](https://www.datatourisme.fr/ontology/core#Concert)

Conditions de pratique de l'itinéraire 
: [PracticeCondition](https://www.datatourisme.fr/ontology/core#PracticeCondition)

Conférence 
: [Conference](https://www.datatourisme.fr/ontology/core#Conference)

Congrès 
: [Congress](https://www.datatourisme.fr/ontology/core#Congress)

Conseil d'administration 
: [BoardMeeting](https://www.datatourisme.fr/ontology/core#BoardMeeting)

Consigne à bagages 
: [LeftLuggage](https://www.datatourisme.fr/ontology/core#LeftLuggage)

Coopérative 
: [Cooperative](https://www.datatourisme.fr/ontology/core#Cooperative)

Cours 
: [Course](https://www.datatourisme.fr/ontology/core#Course)

Couvent 
: [Convent](https://www.datatourisme.fr/ontology/core#Convent)

Crête 
: [Crest](https://www.datatourisme.fr/ontology/core#Crest)

Cuesta 
: [Cuesta](https://www.datatourisme.fr/ontology/core#Cuesta)

Culture 
: [CulturalTheme](https://www.datatourisme.fr/ontology/core#CulturalTheme)

Culture 
: [Culture](https://www.datatourisme.fr/ontology/core#Culture)

Curiosité naturelle 
: [NaturalCuriosity](https://www.datatourisme.fr/ontology/core#NaturalCuriosity)

Cybercafé 
: [Cybercafe](https://www.datatourisme.fr/ontology/core#Cybercafe)

Cyclable 
: [BicycleLocomotionMode](https://www.datatourisme.fr/ontology/core#BicycleLocomotionMode)

Cône 
: [ConeNeck](https://www.datatourisme.fr/ontology/core#ConeNeck)

Côte, littoral 
: [Coastline](https://www.datatourisme.fr/ontology/core#Coastline)

Côteau 
: [Hillsides](https://www.datatourisme.fr/ontology/core#Hillsides)

Description 
: [Description](https://www.datatourisme.fr/ontology/core#Description)

Discothèque 
: [NightClub](https://www.datatourisme.fr/ontology/core#NightClub)

Disposition de la salle 
: [RoomLayout](https://www.datatourisme.fr/ontology/core#RoomLayout)

Distributeur automatique de billets, DAB 
: [ATM](https://www.datatourisme.fr/ontology/core#ATM)

Document GPX 
: [GPX](https://www.datatourisme.fr/ontology/core#GPX)

Document KML 
: [KML](https://www.datatourisme.fr/ontology/core#KML)

Document PDF 
: [PDF](https://www.datatourisme.fr/ontology/core#PDF)

Document texte 
: [Text](https://www.datatourisme.fr/ontology/core#Text)

Domaine de ski alpin 
: [DownhillSkiResort](https://www.datatourisme.fr/ontology/core#DownhillSkiResort)

Domaine de ski nordique 
: [CrossCountrySkiResort](https://www.datatourisme.fr/ontology/core#CrossCountrySkiResort)

Donjon 
: [Dungeon](https://www.datatourisme.fr/ontology/core#Dungeon)

Dune 
: [Dune](https://www.datatourisme.fr/ontology/core#Dune)

Dédicace et rencontre d'artiste 
: [ArtistSigning](https://www.datatourisme.fr/ontology/core#ArtistSigning)

Défilé Cortège Parade 
: [Parade](https://www.datatourisme.fr/ontology/core#Parade)

Dégustation 
: [Tasting](https://www.datatourisme.fr/ontology/core#Tasting)

Démonstration sportive 
: [SportsDemonstration](https://www.datatourisme.fr/ontology/core#SportsDemonstration)

Département 
: [Department](https://www.datatourisme.fr/ontology/core#Department)

Ecluse 
: [Lock](https://www.datatourisme.fr/ontology/core#Lock)

Ecole et centre d'apprentissage 
: [SchoolOrTrainingCentre](https://www.datatourisme.fr/ontology/core#SchoolOrTrainingCentre)

Eglise 
: [Church](https://www.datatourisme.fr/ontology/core#Church)

Embarcadère 
: [Jetty](https://www.datatourisme.fr/ontology/core#Jetty)

Emplacement de camping 
: [CampingPitch](https://www.datatourisme.fr/ontology/core#CampingPitch)

Ensemble fortifié 
: [FortifiedSet](https://www.datatourisme.fr/ontology/core#FortifiedSet)

Equestre 
: [EquestrianLocomotionMode](https://www.datatourisme.fr/ontology/core#EquestrianLocomotionMode)

Etablissement thermal 
: [Spa](https://www.datatourisme.fr/ontology/core#Spa)

Etang 
: [Pond](https://www.datatourisme.fr/ontology/core#Pond)

Etape de l'itinéraire 
: [TourPath](https://www.datatourisme.fr/ontology/core#TourPath)

Evènement commercial 
: [SaleEvent](https://www.datatourisme.fr/ontology/core#SaleEvent)

Evènement jeune public 
: [ChildrensEvent](https://www.datatourisme.fr/ontology/core#ChildrensEvent)

Evènement professionnel d'entreprise 
: [BusinessEvent](https://www.datatourisme.fr/ontology/core#BusinessEvent)

Evènement social 
: [SocialEvent](https://www.datatourisme.fr/ontology/core#SocialEvent)

Evéché 
: [Bishopric](https://www.datatourisme.fr/ontology/core#Bishopric)

Exposition 
: [Exhibition](https://www.datatourisme.fr/ontology/core#Exhibition)

Falaise 
: [Cliff](https://www.datatourisme.fr/ontology/core#Cliff)

Ferme 
: [Farm](https://www.datatourisme.fr/ontology/core#Farm)

Ferme et auberge de campagne 
: [FarmhouseInn](https://www.datatourisme.fr/ontology/core#FarmhouseInn)

Ferme pédagogique 
: [TeachingFarm](https://www.datatourisme.fr/ontology/core#TeachingFarm)

Festival 
: [Festival](https://www.datatourisme.fr/ontology/core#Festival)

Foire ou salon 
: [FairOrShow](https://www.datatourisme.fr/ontology/core#FairOrShow)

Fontaine 
: [Fountain](https://www.datatourisme.fr/ontology/core#Fountain)

Forge 
: [Forge](https://www.datatourisme.fr/ontology/core#Forge)

Fort 
: [Fort](https://www.datatourisme.fr/ontology/core#Fort)

Forêt 
: [Forest](https://www.datatourisme.fr/ontology/core#Forest)

Fournisseur de dégustation 
: [TastingProvider](https://www.datatourisme.fr/ontology/core#TastingProvider)

Fronton, mur de frappe 
: [FrontonBelotaCourt](https://www.datatourisme.fr/ontology/core#FrontonBelotaCourt)

Fête et manifestation 
: [EntertainmentAndEvent](https://www.datatourisme.fr/ontology/core#EntertainmentAndEvent)

Fête traditionnelle 
: [TraditionalCelebration](https://www.datatourisme.fr/ontology/core#TraditionalCelebration)

Galerie d'art, galerie d'exposition 
: [ArtGalleryOrExhibitionGallery](https://www.datatourisme.fr/ontology/core#ArtGalleryOrExhibitionGallery)

Gare ferroviaire 
: [TrainStation](https://www.datatourisme.fr/ontology/core#TrainStation)

Gare routière 
: [BusStation](https://www.datatourisme.fr/ontology/core#BusStation)

Glacier 
: [IceCreamShop](https://www.datatourisme.fr/ontology/core#IceCreamShop)

Glacier de montagne 
: [Glacier](https://www.datatourisme.fr/ontology/core#Glacier)

Gorge 
: [Gorge](https://www.datatourisme.fr/ontology/core#Gorge)

Grand magasin 
: [DepartmentStore](https://www.datatourisme.fr/ontology/core#DepartmentStore)

Grande et moyenne surface 
: [HypermarketAndSupermarket](https://www.datatourisme.fr/ontology/core#HypermarketAndSupermarket)

Grotte, gouffre, aven, caverne, carrière 
: [CaveSinkholeOrAven](https://www.datatourisme.fr/ontology/core#CaveSinkholeOrAven)

Groupement de producteurs 
: [ProducersGroup](https://www.datatourisme.fr/ontology/core#ProducersGroup)

Guide professionnel 
: [ProfessionalTourGuide](https://www.datatourisme.fr/ontology/core#ProfessionalTourGuide)

Gîte d'enfants 
: [ChildrensGite](https://www.datatourisme.fr/ontology/core#ChildrensGite)

Gîte de groupe 
: [GroupLodging](https://www.datatourisme.fr/ontology/core#GroupLodging)

Halle, marché couvert 
: [CoveredMarket](https://www.datatourisme.fr/ontology/core#CoveredMarket)

Halte et port fluvial 
: [RiverPort](https://www.datatourisme.fr/ontology/core#RiverPort)

Hammam 
: [Hammam](https://www.datatourisme.fr/ontology/core#Hammam)

Haras 
: [Stables](https://www.datatourisme.fr/ontology/core#Stables)

Hippodrome 
: [Racetrack](https://www.datatourisme.fr/ontology/core#Racetrack)

Horaires d'ouverture 
: [OpeningHoursSpecification](https://www.datatourisme.fr/ontology/core#OpeningHoursSpecification)

Hotspot Wifi 
: [WifiHotSpot](https://www.datatourisme.fr/ontology/core#WifiHotSpot)

Hébergement 
: [Accommodation](https://www.datatourisme.fr/ontology/core#Accommodation)

Hébergement collectif 
: [CollectiveAccommodation](https://www.datatourisme.fr/ontology/core#CollectiveAccommodation)

Hébergement locatif 
: [RentalAccommodation](https://www.datatourisme.fr/ontology/core#RentalAccommodation)

Hôte bénévole, greeter 
: [VolunteerTourGuideOrGreeter](https://www.datatourisme.fr/ontology/core#VolunteerTourGuideOrGreeter)

Hôtel 
: [Hotel](https://www.datatourisme.fr/ontology/core#Hotel)

Hôtel-restaurant 
: [HotelRestaurant](https://www.datatourisme.fr/ontology/core#HotelRestaurant)

Hôtellerie 
: [HotelTrade](https://www.datatourisme.fr/ontology/core#HotelTrade)

Hôtellerie de plein air 
: [CampingAndCaravanning](https://www.datatourisme.fr/ontology/core#CampingAndCaravanning)

Ile - presqu'île 
: [IslandPeninsula](https://www.datatourisme.fr/ontology/core#IslandPeninsula)

Itinéraire cyclable 
: [CyclingTour](https://www.datatourisme.fr/ontology/core#CyclingTour)

Itinéraire fluvial ou maritime 
: [FluvialTour](https://www.datatourisme.fr/ontology/core#FluvialTour)

Itinéraire pédestre 
: [WalkingTour](https://www.datatourisme.fr/ontology/core#WalkingTour)

Itinéraire routier 
: [RoadTour](https://www.datatourisme.fr/ontology/core#RoadTour)

Itinéraire sous-marin 
: [UnderwaterRoute](https://www.datatourisme.fr/ontology/core#UnderwaterRoute)

Itinéraire touristique 
: [Tour](https://www.datatourisme.fr/ontology/core#Tour)

Itinéraire VTT 
: [MTBRouteTheme](https://www.datatourisme.fr/ontology/core#MTBRouteTheme)

Itinéraire vélo route 
: [CycleRouteTheme](https://www.datatourisme.fr/ontology/core#CycleRouteTheme)

Itinéraire équestre 
: [HorseTour](https://www.datatourisme.fr/ontology/core#HorseTour)

Jetée 
: [Pier](https://www.datatourisme.fr/ontology/core#Pier)

Jeu, concours 
: [Game](https://www.datatourisme.fr/ontology/core#Game)

Label 
: [LabelRating](https://www.datatourisme.fr/ontology/core#LabelRating)

Lac 
: [Lake](https://www.datatourisme.fr/ontology/core#Lake)

Landes 
: [Landes](https://www.datatourisme.fr/ontology/core#Landes)

Lavoir 
: [WashHouse](https://www.datatourisme.fr/ontology/core#WashHouse)

Lieu 
: [Place](https://www.datatourisme.fr/ontology/core#Place)

Lieu 
: [PlaceOfInterest](https://www.datatourisme.fr/ontology/core#PlaceOfInterest)

Lieu de mémoire 
: [RemembranceSite](https://www.datatourisme.fr/ontology/core#RemembranceSite)

Lieu de santé 
: [MedicalPlace](https://www.datatourisme.fr/ontology/core#MedicalPlace)

Lieu de soins 
: [HealthcarePlace](https://www.datatourisme.fr/ontology/core#HealthcarePlace)

Lit 
: [Bed](https://www.datatourisme.fr/ontology/core#Bed)

Location 
: [Rental](https://www.datatourisme.fr/ontology/core#Rental)

Location de matériel 
: [EquipmentRental](https://www.datatourisme.fr/ontology/core#EquipmentRental)

Location de salle 
: [NonHousingRealEstateRental](https://www.datatourisme.fr/ontology/core#NonHousingRealEstateRental)

Loueur de matériel 
: [EquipmentRentalShop](https://www.datatourisme.fr/ontology/core#EquipmentRentalShop)

Maison 
: [House](https://www.datatourisme.fr/ontology/core#House)

Maison de pays, produits du terroir 
: [LocalProductsShop](https://www.datatourisme.fr/ontology/core#LocalProductsShop)

Maison du tourisme 
: [TourismCentre](https://www.datatourisme.fr/ontology/core#TourismCentre)

Maison remarquable 
: [RemarkableHouse](https://www.datatourisme.fr/ontology/core#RemarkableHouse)

Marais 
: [Swamp](https://www.datatourisme.fr/ontology/core#Swamp)

Marché 
: [Market](https://www.datatourisme.fr/ontology/core#Market)

Meublés de tourisme 
: [SelfCateringAccommodation](https://www.datatourisme.fr/ontology/core#SelfCateringAccommodation)

Mine 
: [Mine](https://www.datatourisme.fr/ontology/core#Mine)

Mini golf 
: [MiniGolf](https://www.datatourisme.fr/ontology/core#MiniGolf)

Mode de locomotion pour les itinéraires 
: [LocomotionMode](https://www.datatourisme.fr/ontology/core#LocomotionMode)

Mode de tarification 
: [PricingMode](https://www.datatourisme.fr/ontology/core#PricingMode)

Monastère, prieuré 
: [Monastery](https://www.datatourisme.fr/ontology/core#Monastery)

Montagne 
: [Mountain](https://www.datatourisme.fr/ontology/core#Mountain)

Mosquée 
: [Mosque](https://www.datatourisme.fr/ontology/core#Mosque)

Moulin 
: [Mill](https://www.datatourisme.fr/ontology/core#Mill)

Multiactivités 
: [MultiActivity](https://www.datatourisme.fr/ontology/core#MultiActivity)

Musée 
: [Museum](https://www.datatourisme.fr/ontology/core#Museum)

Mégalithes, menhirs et dolmens 
: [MegalithDolmenMenhir](https://www.datatourisme.fr/ontology/core#MegalithDolmenMenhir)

Niveau de difficulté 
: [DifficultyLevel](https://www.datatourisme.fr/ontology/core#DifficultyLevel)

Nom d'itinéraire 
: [RouteTheme](https://www.datatourisme.fr/ontology/core#RouteTheme)

Note 
: [ScaleRating](https://www.datatourisme.fr/ontology/core#ScaleRating)

Négociant 
: [Trader](https://www.datatourisme.fr/ontology/core#Trader)

Office de tourisme 
: [LocalTouristOffice](https://www.datatourisme.fr/ontology/core#LocalTouristOffice)

Opéra 
: [Opera](https://www.datatourisme.fr/ontology/core#Opera)

Organisation 
: [Organisation](https://www.datatourisme.fr/ontology/core#Organisation)

Organisme réceptif 
: [IncomingTravelAgency](https://www.datatourisme.fr/ontology/core#IncomingTravelAgency)

Palais 
: [Palace](https://www.datatourisme.fr/ontology/core#Palace)

Palais des sports 
: [SportsHall](https://www.datatourisme.fr/ontology/core#SportsHall)

Parc de loisirs, parc à thème 
: [ThemePark](https://www.datatourisme.fr/ontology/core#ThemePark)

Parc et jardin 
: [ParkAndGarden](https://www.datatourisme.fr/ontology/core#ParkAndGarden)

Parc naturel 
: [NaturalPark](https://www.datatourisme.fr/ontology/core#NaturalPark)

Parcours de Santé 
: [FitnessPath](https://www.datatourisme.fr/ontology/core#FitnessPath)

Parking 
: [Parking](https://www.datatourisme.fr/ontology/core#Parking)

Patinoire 
: [IceSkatingRink](https://www.datatourisme.fr/ontology/core#IceSkatingRink)

Patrimoine industriel, artisanal, rural, agricole et technique 
: [TechnicalHeritage](https://www.datatourisme.fr/ontology/core#TechnicalHeritage)

Pelouse calcaire 
: [ChalkyLawn](https://www.datatourisme.fr/ontology/core#ChalkyLawn)

Personne 
: [Person](https://www.datatourisme.fr/ontology/core#Person)

Phare 
: [Lighthouse](https://www.datatourisme.fr/ontology/core#Lighthouse)

Pharmacie 
: [Pharmacy](https://www.datatourisme.fr/ontology/core#Pharmacy)

Pic 
: [Peak](https://www.datatourisme.fr/ontology/core#Peak)

Pierre, rocher 
: [Stone](https://www.datatourisme.fr/ontology/core#Stone)

Pigeonnier 
: [PigeonLoft](https://www.datatourisme.fr/ontology/core#PigeonLoft)

Piscine 
: [SwimmingPool](https://www.datatourisme.fr/ontology/core#SwimmingPool)

Piste de chien de traineau 
: [DogSleddingTrail](https://www.datatourisme.fr/ontology/core#DogSleddingTrail)

Piste de luge / bobsleigh 
: [TobogganBobsleigh](https://www.datatourisme.fr/ontology/core#TobogganBobsleigh)

Piste de luge d'été 
: [SummerToboggan](https://www.datatourisme.fr/ontology/core#SummerToboggan)

Piste de roller ou de skate board 
: [TrackRollerOrSkateBoard](https://www.datatourisme.fr/ontology/core#TrackRollerOrSkateBoard)

Piste de ski alpin 
: [DownhillSkiRun](https://www.datatourisme.fr/ontology/core#DownhillSkiRun)

Piste de ski de fond 
: [CrossCountrySkiTrail](https://www.datatourisme.fr/ontology/core#CrossCountrySkiTrail)

Pièce 
: [RoomAmenity](https://www.datatourisme.fr/ontology/core#RoomAmenity)

Pièce de théâtre 
: [TheaterEvent](https://www.datatourisme.fr/ontology/core#TheaterEvent)

Plage 
: [Beach](https://www.datatourisme.fr/ontology/core#Beach)

Plaine 
: [Plain](https://www.datatourisme.fr/ontology/core#Plain)

Plateau 
: [Plateau](https://www.datatourisme.fr/ontology/core#Plateau)

Point d'eau 
: [WaterSource](https://www.datatourisme.fr/ontology/core#WaterSource)

Point d'intérêt 
: [PointOfInterest](https://www.datatourisme.fr/ontology/core#PointOfInterest)

Point de vue 
: [PointOfView](https://www.datatourisme.fr/ontology/core#PointOfView)

Politique tarifaire 
: [PricingPolicy](https://www.datatourisme.fr/ontology/core#PricingPolicy)

Pont 
: [Bridge](https://www.datatourisme.fr/ontology/core#Bridge)

Port de plaisance 
: [Marina](https://www.datatourisme.fr/ontology/core#Marina)

Port maritime 
: [Seaport](https://www.datatourisme.fr/ontology/core#Seaport)

Portes ouvertes 
: [OpenDay](https://www.datatourisme.fr/ontology/core#OpenDay)

Portée géographique 
: [GeographicReach](https://www.datatourisme.fr/ontology/core#GeographicReach)

Prairie 
: [Grassland](https://www.datatourisme.fr/ontology/core#Grassland)

Pratique 
: [Practice](https://www.datatourisme.fr/ontology/core#Practice)

Pratique libre 
: [FreePractice](https://www.datatourisme.fr/ontology/core#FreePractice)

Prestataire d'activité 
: [ActivityProvider](https://www.datatourisme.fr/ontology/core#ActivityProvider)

Prestataire d'activité culturelle 
: [CulturalActivityProvider](https://www.datatourisme.fr/ontology/core#CulturalActivityProvider)

Prestataire d'activité sportive et de loisir 
: [LeisureSportActivityProvider](https://www.datatourisme.fr/ontology/core#LeisureSportActivityProvider)

Prestataire de service 
: [ServiceProvider](https://www.datatourisme.fr/ontology/core#ServiceProvider)

Prestation 
: [Offer](https://www.datatourisme.fr/ontology/core#Offer)

Prestation tarifée 
: [PricingOffer](https://www.datatourisme.fr/ontology/core#PricingOffer)

Prestation tarifée d'hébergement 
: [AccommodationPricingOffer](https://www.datatourisme.fr/ontology/core#AccommodationPricingOffer)

Prestation tarifée d'une activité 
: [ActivityPricingOffer](https://www.datatourisme.fr/ontology/core#ActivityPricingOffer)

Prestation tarifée de location (hors hébergement): vélo, salle de réunion 
: [RentalPricingOffer](https://www.datatourisme.fr/ontology/core#RentalPricingOffer)

Prestation tarifée de restauration 
: [CateringPricingOffer](https://www.datatourisme.fr/ontology/core#CateringPricingOffer)

Prestation tarifée générale 
: [GeneralPricingOffer](https://www.datatourisme.fr/ontology/core#GeneralPricingOffer)

Producteur 
: [Producer](https://www.datatourisme.fr/ontology/core#Producer)

Produit 
: [Product](https://www.datatourisme.fr/ontology/core#Product)

Produit d'hébergement 
: [AccommodationProduct](https://www.datatourisme.fr/ontology/core#AccommodationProduct)

Professionnel de santé 
: [HealthcareProfessional](https://www.datatourisme.fr/ontology/core#HealthcareProfessional)

Projection, cinéma 
: [ScreeningEvent](https://www.datatourisme.fr/ontology/core#ScreeningEvent)

Pèlerinage et procession 
: [PilgrimageAndProcession](https://www.datatourisme.fr/ontology/core#PilgrimageAndProcession)

Pédestre 
: [PedestrianLocomotionMode](https://www.datatourisme.fr/ontology/core#PedestrianLocomotionMode)

Période 
: [Period](https://www.datatourisme.fr/ontology/core#Period)

Période limitée 
: [LimitedPeriod](https://www.datatourisme.fr/ontology/core#LimitedPeriod)

Période récurrente 
: [RecurrentPeriod](https://www.datatourisme.fr/ontology/core#RecurrentPeriod)

Quantité 
: [Quantity](https://www.datatourisme.fr/ontology/core#Quantity)

Quartier 
: [District](https://www.datatourisme.fr/ontology/core#District)

Rallye 
: [Rally](https://www.datatourisme.fr/ontology/core#Rally)

Rampe de mise à l'eau 
: [LaunchingRamp](https://www.datatourisme.fr/ontology/core#LaunchingRamp)

Randonnée, balade 
: [Rambling](https://www.datatourisme.fr/ontology/core#Rambling)

Refuge et gîte d'étape 
: [StopOverOrGroupLodge](https://www.datatourisme.fr/ontology/core#StopOverOrGroupLodge)

Restaurant 
: [Restaurant](https://www.datatourisme.fr/ontology/core#Restaurant)

Restaurant d'altitude / Restaurant d'alpage 
: [MountainRestaurant](https://www.datatourisme.fr/ontology/core#MountainRestaurant)

Restaurant gastronomique 
: [GourmetRestaurant](https://www.datatourisme.fr/ontology/core#GourmetRestaurant)

Restauration 
: [FoodEstablishment](https://www.datatourisme.fr/ontology/core#FoodEstablishment)

Restauration ambulante, Food truck 
: [StreetFood](https://www.datatourisme.fr/ontology/core#StreetFood)

Restauration Rapide 
: [FastFoodRestaurant](https://www.datatourisme.fr/ontology/core#FastFoodRestaurant)

Rivière ou fleuve 
: [River](https://www.datatourisme.fr/ontology/core#River)

Routier 
: [RoadsideLocomotionMode](https://www.datatourisme.fr/ontology/core#RoadsideLocomotionMode)

Ruines et vestiges 
: [Ruins](https://www.datatourisme.fr/ontology/core#Ruins)

Ruisseau 
: [Stream](https://www.datatourisme.fr/ontology/core#Stream)

Récital 
: [Recital](https://www.datatourisme.fr/ontology/core#Recital)

Région 
: [Region](https://www.datatourisme.fr/ontology/core#Region)

Réparateur de matériel 
: [EquipmentRepairShop](https://www.datatourisme.fr/ontology/core#EquipmentRepairShop)

Résidence de tourisme 
: [HolidayResort](https://www.datatourisme.fr/ontology/core#HolidayResort)

Réunion de travail 
: [WorkMeeting](https://www.datatourisme.fr/ontology/core#WorkMeeting)

Saison tarifaire 
: [PricingSeason](https://www.datatourisme.fr/ontology/core#PricingSeason)

Salle de billard 
: [BilliardRoom](https://www.datatourisme.fr/ontology/core#BilliardRoom)

Salle de squash 
: [SquashCourt](https://www.datatourisme.fr/ontology/core#SquashCourt)

Salle ou terrain de sport, gymnase 
: [Gymnasium](https://www.datatourisme.fr/ontology/core#Gymnasium)

Salle polyvalente, salle des fêtes 
: [MultiPurposeRoomOrCommunityRoom](https://www.datatourisme.fr/ontology/core#MultiPurposeRoomOrCommunityRoom)

Semaine du mois 
: [WeekOfTheMonth](https://www.datatourisme.fr/ontology/core#WeekOfTheMonth)

Sentier de découverte et d'interprétation 
: [EducationalTrail](https://www.datatourisme.fr/ontology/core#EducationalTrail)

Service 
: [Service](https://www.datatourisme.fr/ontology/core#Service)

Service d'information touristique 
: [TouristInformationCenter](https://www.datatourisme.fr/ontology/core#TouristInformationCenter)

Service pratique 
: [ConvenientService](https://www.datatourisme.fr/ontology/core#ConvenientService)

Site archéologique 
: [ArcheologicalSite](https://www.datatourisme.fr/ontology/core#ArcheologicalSite)

Site culturel 
: [CulturalSite](https://www.datatourisme.fr/ontology/core#CulturalSite)

Site d'affaires 
: [BusinessPlace](https://www.datatourisme.fr/ontology/core#BusinessPlace)

Site de défense 
: [DefenceSite](https://www.datatourisme.fr/ontology/core#DefenceSite)

Site et mur d'escalade 
: [ClimbingWall](https://www.datatourisme.fr/ontology/core#ClimbingWall)

Site industriel 
: [IndustrialSite](https://www.datatourisme.fr/ontology/core#IndustrialSite)

Site naturel 
: [NaturalHeritage](https://www.datatourisme.fr/ontology/core#NaturalHeritage)

Site religieux 
: [ReligiousSite](https://www.datatourisme.fr/ontology/core#ReligiousSite)

Site sportif, récréatif et de loisirs 
: [SportsAndLeisurePlace](https://www.datatourisme.fr/ontology/core#SportsAndLeisurePlace)

Sommet 
: [Summit](https://www.datatourisme.fr/ontology/core#Summit)

Son 
: [Sound](https://www.datatourisme.fr/ontology/core#Sound)

Son et lumière, feu d'artifice 
: [VisualArtsEvent](https://www.datatourisme.fr/ontology/core#VisualArtsEvent)

Source 
: [Source](https://www.datatourisme.fr/ontology/core#Source)

Spectacle 
: [ShowEvent](https://www.datatourisme.fr/ontology/core#ShowEvent)

Spectacle de cirque 
: [CircusEvent](https://www.datatourisme.fr/ontology/core#CircusEvent)

Spectacle de danse 
: [DanceEvent](https://www.datatourisme.fr/ontology/core#DanceEvent)

Sports adaptés 
: [AdaptedsportsLocomotionMode](https://www.datatourisme.fr/ontology/core#AdaptedsportsLocomotionMode)

Sports d'hiver 
: [WintersportsLocomotionMode](https://www.datatourisme.fr/ontology/core#WintersportsLocomotionMode)

Spécification d'équipement commun 
: [CommonFeatureSpecification](https://www.datatourisme.fr/ontology/core#CommonFeatureSpecification)

Spécification d'équipement d'hôtellrie de plein air 
: [CampingAndCaravanningFeatureSpecification](https://www.datatourisme.fr/ontology/core#CampingAndCaravanningFeatureSpecification)

Spécification d'équipement d'information 
: [InformativeFeatureSpecification](https://www.datatourisme.fr/ontology/core#InformativeFeatureSpecification)

Spécification d'équipement de dégustation 
: [TastingFeatureSpecification](https://www.datatourisme.fr/ontology/core#TastingFeatureSpecification)

Spécification d'équipement de patrimoine culturel 
: [CulturalHeritageFeatureSpecification](https://www.datatourisme.fr/ontology/core#CulturalHeritageFeatureSpecification)

Spécification d'équipement de patrimoine naturel 
: [NaturalHeritageFeatureSpecification](https://www.datatourisme.fr/ontology/core#NaturalHeritageFeatureSpecification)

Spécification d'équipement de pièce 
: [RoomFeatureSpecification](https://www.datatourisme.fr/ontology/core#RoomFeatureSpecification)

Spécification d'équipement de restauration 
: [CateringFeatureSpecification](https://www.datatourisme.fr/ontology/core#CateringFeatureSpecification)

Spécification d'équipement et service 
: [FeatureSpecification](https://www.datatourisme.fr/ontology/core#FeatureSpecification)

Spécification d'équipement-service d'hébergement 
: [AccommodationFeatureSpecification](https://www.datatourisme.fr/ontology/core#AccommodationFeatureSpecification)

Stade 
: [Stadium](https://www.datatourisme.fr/ontology/core#Stadium)

Stage d'initiation 
: [IntroductionCourse](https://www.datatourisme.fr/ontology/core#IntroductionCourse)

Stage de perfectionnement 
: [DevelopmentCourse](https://www.datatourisme.fr/ontology/core#DevelopmentCourse)

Stage, atelier 
: [Traineeship](https://www.datatourisme.fr/ontology/core#Traineeship)

Station de lavage 
: [CarOrBikeWash](https://www.datatourisme.fr/ontology/core#CarOrBikeWash)

Station de montagne 
: [MountainResort](https://www.datatourisme.fr/ontology/core#MountainResort)

Station ou dépôt de vélo 
: [BikeStationOrDepot](https://www.datatourisme.fr/ontology/core#BikeStationOrDepot)

Station thermale 
: [SpaResort](https://www.datatourisme.fr/ontology/core#SpaResort)

Style architectural 
: [ArchitecturalStyle](https://www.datatourisme.fr/ontology/core#ArchitecturalStyle)

Suite 
: [HotelSuite](https://www.datatourisme.fr/ontology/core#HotelSuite)

Synagogue 
: [Synagogue](https://www.datatourisme.fr/ontology/core#Synagogue)

Système de classement 
: [ReviewSystem](https://www.datatourisme.fr/ontology/core#ReviewSystem)

Système de classement par label 
: [LabelReviewSystem](https://www.datatourisme.fr/ontology/core#LabelReviewSystem)

Système de classement par note 
: [ScaleReviewSystem](https://www.datatourisme.fr/ontology/core#ScaleReviewSystem)

Séminaire 
: [Seminar](https://www.datatourisme.fr/ontology/core#Seminar)

Table d'hôtes 
: [TableHotes](https://www.datatourisme.fr/ontology/core#TableHotes)

Tarif 
: [PriceSpecification](https://www.datatourisme.fr/ontology/core#PriceSpecification)

Temple 
: [Temple](https://www.datatourisme.fr/ontology/core#Temple)

Temple bouddhique 
: [BuddhistTemple](https://www.datatourisme.fr/ontology/core#BuddhistTemple)

Tente 
: [Tent](https://www.datatourisme.fr/ontology/core#Tent)

Terrain de golf 
: [GolfCourse](https://www.datatourisme.fr/ontology/core#GolfCourse)

Terrain park 
: [TerrainPark](https://www.datatourisme.fr/ontology/core#TerrainPark)

Thème 
: [Theme](https://www.datatourisme.fr/ontology/core#Theme)

Thème d'environnement de POI 
: [SpatialEnvironmentTheme](https://www.datatourisme.fr/ontology/core#SpatialEnvironmentTheme)

Thème de fête et évènement 
: [EntertainmentAndEventTheme](https://www.datatourisme.fr/ontology/core#EntertainmentAndEventTheme)

Thème de parc et jardin 
: [ParkAndGardenTheme](https://www.datatourisme.fr/ontology/core#ParkAndGardenTheme)

Thème de restauration 
: [FoodEstablishmentTheme](https://www.datatourisme.fr/ontology/core#FoodEstablishmentTheme)

Thème de santé 
: [HealthTheme](https://www.datatourisme.fr/ontology/core#HealthTheme)

Thèmes d’activité et évènements sport et loisirs 
: [SportsTheme](https://www.datatourisme.fr/ontology/core#SportsTheme)

Théatre, Salle de spectacle 
: [Theater](https://www.datatourisme.fr/ontology/core#Theater)

Tipi 
: [Tipi](https://www.datatourisme.fr/ontology/core#Tipi)

Toilettes publiques 
: [PublicLavatories](https://www.datatourisme.fr/ontology/core#PublicLavatories)

Tour 
: [Tower](https://www.datatourisme.fr/ontology/core#Tower)

Tourbière 
: [Bog](https://www.datatourisme.fr/ontology/core#Bog)

Train touristique 
: [TouristTrain](https://www.datatourisme.fr/ontology/core#TouristTrain)

Transport 
: [Transport](https://www.datatourisme.fr/ontology/core#Transport)

Transporteur 
: [Transporter](https://www.datatourisme.fr/ontology/core#Transporter)

Tremplin 
: [Trampoline](https://www.datatourisme.fr/ontology/core#Trampoline)

Type d'itinéraire 
: [TourType](https://www.datatourisme.fr/ontology/core#TourType)

Type de cuisine 
: [CuisineCategory](https://www.datatourisme.fr/ontology/core#CuisineCategory)

Type de lit 
: [TypeOfBed](https://www.datatourisme.fr/ontology/core#TypeOfBed)

Type de mêts 
: [FoodProduct](https://www.datatourisme.fr/ontology/core#FoodProduct)

Type de terrain 
: [LandType](https://www.datatourisme.fr/ontology/core#LandType)

Type de terrain 
: [LandTypeName](https://www.datatourisme.fr/ontology/core#LandTypeName)

Téléphérique 
: [CableCarStation](https://www.datatourisme.fr/ontology/core#CableCarStation)

Téléphérique touristique 
: [TourismCableCar](https://www.datatourisme.fr/ontology/core#TourismCableCar)

Valeur de classement 
: [Rating](https://www.datatourisme.fr/ontology/core#Rating)

Vallée 
: [Valley](https://www.datatourisme.fr/ontology/core#Valley)

Vendange, récolte 
: [Harvest](https://www.datatourisme.fr/ontology/core#Harvest)

Verger conservatoire 
: [Orchard](https://www.datatourisme.fr/ontology/core#Orchard)

Via ferrata 
: [ViaFerrata](https://www.datatourisme.fr/ontology/core#ViaFerrata)

Vide-grenier 
: [GarageSale](https://www.datatourisme.fr/ontology/core#GarageSale)

Vidéo 
: [Video](https://www.datatourisme.fr/ontology/core#Video)

Ville et village 
: [CityHeritage](https://www.datatourisme.fr/ontology/core#CityHeritage)

Visite 
: [Visit](https://www.datatourisme.fr/ontology/core#Visit)

Vivarium - Aquarium 
: [VivariumAquarium](https://www.datatourisme.fr/ontology/core#VivariumAquarium)

Voie romaine 
: [RomanPath](https://www.datatourisme.fr/ontology/core#RomanPath)

Volcan 
: [Volcano](https://www.datatourisme.fr/ontology/core#Volcano)

Voyagiste 
: [TourOperatorOrTravelAgency](https://www.datatourisme.fr/ontology/core#TourOperatorOrTravelAgency)

Vélodrome 
: [Velodrome](https://www.datatourisme.fr/ontology/core#Velodrome)

Vélorail 
: [RailBike](https://www.datatourisme.fr/ontology/core#RailBike)

Yacht Club 
: [YachtClub](https://www.datatourisme.fr/ontology/core#YachtClub)

Yourte 
: [Yurt](https://www.datatourisme.fr/ontology/core#Yurt)

Zone halophile 
: [HalophilicArea](https://www.datatourisme.fr/ontology/core#HalophilicArea)

Zone humide 
: [Wetland](https://www.datatourisme.fr/ontology/core#Wetland)

Zone ou port de mouillage 
: [MooringArea](https://www.datatourisme.fr/ontology/core#MooringArea)

Zoo - parc animalier 
: [ZooAnimalPark](https://www.datatourisme.fr/ontology/core#ZooAnimalPark)

Éleveur 
: [Farmer](https://www.datatourisme.fr/ontology/core#Farmer)

Équipement et service 
: [Amenity](https://www.datatourisme.fr/ontology/core#Amenity)

Équipement et service basique 
: [CommonAmenity](https://www.datatourisme.fr/ontology/core#CommonAmenity)

Équipement et service d'hébergement 
: [AccommodationAmenity](https://www.datatourisme.fr/ontology/core#AccommodationAmenity)

Équipement et service d'hôtellerie de plein air 
: [CampingAndCaravanningAmenity](https://www.datatourisme.fr/ontology/core#CampingAndCaravanningAmenity)

Équipement et service d'information 
: [InformativeAmenity](https://www.datatourisme.fr/ontology/core#InformativeAmenity)

Équipement et service de patrimoine culturel 
: [CulturalHeritageAmenity](https://www.datatourisme.fr/ontology/core#CulturalHeritageAmenity)

Équipement et service de patrimoine naturel 
: [NaturalHeritageAmenity](https://www.datatourisme.fr/ontology/core#NaturalHeritageAmenity)

Équipement et service de restauration 
: [CateringAmenity](https://www.datatourisme.fr/ontology/core#CateringAmenity)

Évènement culturel 
: [CulturalEvent](https://www.datatourisme.fr/ontology/core#CulturalEvent)

Évènement religieux 
: [ReligiousEvent](https://www.datatourisme.fr/ontology/core#ReligiousEvent)

Évènement sports et loisirs 
: [SportsEvent](https://www.datatourisme.fr/ontology/core#SportsEvent)

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


