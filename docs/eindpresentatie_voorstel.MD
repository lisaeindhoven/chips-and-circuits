# eindpresentatie Misbaksels
# datastructuur kan onbenoemd blijven bij de eindpresentatie

#### Taalgebruik.

Onze doelgroep: medestudenten/TA's van Programmeertheorie. Dus: casus in algemene termen die iedereen begrijpt en we niet hoeven uitleggen (constrained optimization problem, hard constraints, soft constraints) en zo concreet mogelijk wat die termen betekenen voor onze casus (in onze casus zijn de hard en soft constraints specifiek collisions etc)

Laten we goed nadenken over de termen en consistent dezelfde termen gebruiken, vakspecifieke termen die we 1x uitleggen of termen die iedereen (bij programmeertheorie) kent en we niet hoeven uitleggen.

Ik stel voor: 
    - Chip(s) (behoeft geen uitleg)
    - Gates = de te verbinden punten op de chip, kunnen niet zomaar overal liggen, maar liggen op een grid
    - Grid = het raster waarop de Gates liggen. 
    - Nets = de verbindingen/nets/draden tussen gates. Lopen langs het raster, Manhattan style, maar dan driedimensionaal omdat ze er in totaal acht lagen zijn, de gates liggen       allemaal op de onderste laag.
    - Intersections = kruisingen van draden, soft constraint want duur.
    - Collisions = de verbindingen/nets/draden mogen niet over dezelfde stukjes tussen de gridpunten lopen/ stukjes tussen twee punten. Kunnen we ook conflicten noemen? Hard constraint. Chip is onbruikbaar, oplossing is ongeldig.

#### VISUALS

Laten we een stijl kiezen en die van begin tot eind hanteren. Dus in dezelfde stijl als onze driedimensionale eindpresentatie ook de casus introduceren.

#### INHOUD

INTRODUCTIE VAN DE CASUS

    De termen hierboven uitleggen en dat het ons doel is om een zo kort mogelijk pad te leggen voor betere chips.
    
    Visueel daarbij:
    - Leeg raster met zichtbare assen (al dan niet met de cijfer ernaast). Tweedimensionaal?
    - Zelfde plaatje met gates erin.
    - Dan met een net / meerdere nets
    - Dan met een intersection.
    - Dan met een collision
    - Dan met een geldige oplossing.
    - Dan met een optimale oplossing.

    State space formuleren aan de hand van vertakkingen van beslissingsmogelijkheden. 
    Aantal draden dat we leggen * eenheden pad * aantal opties om dat pad te leggen = 
    k * n * O (5 *  5 * 4-5 * 4-5 * 3-5 * 2-5 * 1-5 * 0-5)
        - visual van opties om te vertakken op een willekeurige plek?
        - visuals van een vermenigvuldiging van de opties?
    
    Lower bound =  manhattan distance stukjes draad n * aantal draden k

    Upper bound = aantal slimme opties * stukjes draad * aantal draden

METHODE VAN PROBLEEMOPLOSSING # eventueel al met de resultaten?

    We willen in beperkte tijd goede, geldige oplossingen vinden zonder inadmissible heuristics die mogelijk goede oplossingen uitsluiten.

    Idealiter leggen we een draad / terwijl we rekening houden met de consequenties voor het leggen van alle andere draden maar vanwege de complexiteit van ons probleem is dit niet mogelijk. Het zal ook onmogelijk blijken om snel, consistent tot een goede oplossing te komen zonder gebruik te maken van inadmissible heuristics.

    Om dit op te lossen splitsen we het probleem op in twee niveaus: op laag niveau willen we een zo kort mogelijk pad leggen tussen twee gates. Op hoog niveau beslissen we onder andere welk pad dat is. De beste resultaten hopen we te bereiken door een goede wisselwerking van deze niveaus.

        - Laag niveau: pathfiding per net met de volgende algoritmes:
            - Random --- willekeurig pad eerst, willekeurige stapjes, tot een oplossing of vastgelopen.
            - Greedy (manhattan distance) ---  
            - Dijkstra (breadth first met early exit?)
            - A* (Dijkstra + greedy lookahead dmv heuristiek, in ons geval manhattan distance). Sowieso superieur en de kostenfunctie leent zich goed voor de constraints van onze casus, (en komt later nog van pas voor bepaalde heuristieken.)

        - Hoog niveau: 
            - Welke nets (her)leggen we? Een (redelijke) oplossing analyseren en bepalen welke nets het meest problematisch zijn. Dat kunnen (onnodig) lange paden zijn of de paden die de meeste conflicten met andere paden veroorzaken.

    Om de beste oplossingen te generen hebben we een algoritme geschreven dat wisselt tussen de niveaus. 
    Tot we een bepaalde kwaliteit oplossing**TODO** bereikt hebben herhalen we de volgende twee stappen:

        Stap 1) Leg alle (overgebleven) paden 
                (met afnemend versoepelde constraints)
        Stap 2) Verwijder problematisch pad 
                (dat meeste andere paden in de weg zit, dat het langst is, dat het duurst is)

    Een voor de hand liggende aanpak, waarbij het kiezen van de juiste heuristieken cruciaal is. 
    Wij hebben geprobeerd verschillende parameters van a) b) c) ***TODO***
       
CONCLUSIE ***TODO*** resultaten eventueel al verweven in methode?

    Onze meest succesvolle strategie bleek ***TODO***. Hier visual met behaalde kosten per 1000 runs of whatever. 
    
    Dit is wel/niet wat we verwacht hadden. Toekomstige verbeteringen zouden kunnen liggen in het nader onderzoeken van algoritme x of y en heuristiek x of y. Natuurlijk zonder te zeggen dat we daar niet aan toe zijn gekomen o.i.d.

    Bedankt voor jullie aandacht.
