# eindpresentatie Misbaksels
# datastructuur kan onbenoemd blijven bij de eindpresentatie

#### Taalgebruik.

Onze doelgroep: medestudenten/TA's van Programmeertheorie. Dus: casus in algemene termen die iedereen begrijpt en we niet hoeven uitleggen (constrained optimization problem, hard constraints, soft constraints) en zo concreet mogelijk wat die termen betekenen voor onze casus (in onze casus zijn de hard en soft constraints specifiek collisions etc)

Laten we goed nadenken over de termen en consistent dezelfde termen gebruiken, vakspecifieke termen die we 1x uitleggen of termen die iedereen (bij programmeertheorie) kent en we niet hoeven uitleggen.

Ik stel voor: 
    - Chip(s) (behoeft geen uitleg)
    - Gates = de te verbinden punten op de chip, kunnen niet zomaar overal liggen, maar liggen op een grid
    - Grid = het raster waarop de Gates liggen. 
    - Nets = de verbindingen tussen gates. Lopen over het raster in Manhattan style, maar dan driedimensionaal omdat er in totaal acht lagen zijn. De gates liggen wel allemaal op de onderste laag.
    - Intersections = kruisingen van draden, soft constraint want duur.
    - Collisions = de verbindingen/nets/draden mogen niet over dezelfde stukjes tussen de gridpunten lopen/ stukjes tussen twee punten. Kunnen we ook conflicten noemen? Hard constraint. Chip is onbruikbaar, oplossing is ongeldig.

#### VISUALS

Laten we een stijl kiezen en die van begin tot eind hanteren. Dus in dezelfde stijl als onze driedimensionale eindpresentatie ook de casus introduceren.

#### INHOUD
-------------------------- 1:
INTRODUCTIE VAN DE CASUS

    De termen hierboven uitleggen en dat het ons doel is om een zo kort mogelijk pad te leggen voor betere chips. 
    Kostenfunctie = n + 300 * k
    
    Visueel daarbij:
    - Leeg raster met zichtbare assen (al dan niet met de cijfer ernaast). Tweedimensionaal?
    - Zelfde plaatje met gates erin.
    - Dan met een net / meerdere nets
    - Dan met een intersection.
    - Dan met een collision
    - Dan met een geldige oplossing.
    - Dan met een optimale oplossing.



    State space formuleren aan de hand van vertakkingen van beslissingsmogelijkheden. 
    Verbindingen * stappen * aantal mogelijkheden voor elke stap = (k * n) ^ 5

        - visual van opties om te vertakken op een willekeurige plek? *** #TODO ***
        - visuals van een vermenigvuldiging van de opties? #TODO
    
    Lower bound =  manhattan distance stukjes draad n * aantal draden k

    Upper bound = aantal verbindingen * stukjes draad * aantal voorwaartse opties (anders is vrijwel oneindig en dus onzinnig)

---------------------------- 2:

METHODE VAN PROBLEEMOPLOSSING

    Pathfiding per verbinding met de volgende algoritmes:
        - Random (willekeurig pad eerst, willekeurige stapjes, tot een oplossing of vastgelopen.)
        - Dijkstra (breadth first met early exit)
        - A* (Voegt aan Dijkstra een kostenfunctie toe met behulp van de manhattan distance. 

    Idealiter leggen we een draad terwijl we rekening houden met de consequenties voor het leggen van alle andere draden - maar gezien de state space / en de complexiteit van ons probleem kunnen we niet dit alles tegelijk berekenen. 

    Om dit op te lossen splitsen we het probleem op in twee niveaus: op laag niveau willen we een zo kort mogelijk pad leggen tussen twee gates. Op hoog niveau beslissen we welke verbindingen we eerst (her)leggen. De beste resultaten hopen we te bereiken door een goede wisselwerking van deze niveaus.

    Voor een aantal iteraties of tot we een oplossing genereren die we goed genoeg achten herhalen we de volgende twee stappen:

        Stap 1 - Laag Niveau: Leg alle (overgebleven) paden 
                (eerst met aangepaste constraints)
        Stap 2 - Hoog Niveau: Verwijder problematisch pad 
                (dat meeste andere paden in de weg zit, of dat het langst is, of het hoogst gaat)

--------------------------------------- 3:

HEURISTIEKEN - Conflictanalyse en aangepaste constraints (aangepaste )

    Laag niveau: 
       
        Scary Gates - locaties rondom gates zijn duurder (constraint intensification)

        Skyscraper - omhoog bewegen is goedkoper (constraint relaxation)

    Hoog niveau:
    
        Netvolgorde: o.a. begin bij de drukste gates

        Conflictanalyse: (van een versoepelde oplossing) problematische verbindingen isoleren en aanpassen

        Efficientieanalyse: (bij een bemoeilijkte oplossing) herleg eerst de draden die onnodig lang lijken
    
    ***TODO*** Wij hebben geprobeerd verschillende parameters van a) b) c) 
       
RESULTATEN

    Onze grootste successen hebben we bereikt met heuristieken x, y en z.
    Kekke visuals door Mik Schutte.

CONCLUSIE ***TODO*** 
    
    Dit is wel/niet wat we verwacht hadden. Toekomstige verbeteringen zouden kunnen liggen in het nader onderzoeken van algoritme x of y en heuristiek x of y. 

    Bedankt voor jullie aandacht.

DISCUSSIE
    ELINE KLIK
    