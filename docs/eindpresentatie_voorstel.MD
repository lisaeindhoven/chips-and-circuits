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

    - State space formuleren aan de hand van vertakkingen van beslissingsmogelijkheden. 
        - visual van opties om te vertakken op een willekeurige plek?
        - visuals van een vermenigvuldiging van de opties?
        

METHODE VAN PROBLEEMOPLOSSING # eventueel al met de resultaten?

    Idealiter leggen we een draad / terwijl we rekening houden met de consequenties voor het leggen van alle andere draden maar vanwege de grootte van ons probleem / de state space is dit niet mogelijk. Het zal ook onmogelijk blijken om consistent tot een goede, geldige oplossing te komen zonder gebruik te maken van inadmissible heuristics.

    Om dit op te lossen splitsen we het probleem op in twee niveaus:

        - Laag niveau: pathfiding per net. 

            - Random
            - Greedy (even noemen ook als we die niet gemaakt hebben)
            - Dijkstra (breadth first met early exit?)
            - A* (Dijkstra + greedy lookahead dmv heuristiek manhattan distance)
            
            Benoemen wat we verwachten dat het voordeel is van een algoritme ten opzichte van bovenstaande. 
            Maatstaven: geldige oplossingen vinden. Goede oplossingen vinden. Geen oplossingen uitsluiten (alleen admissible heuristics (onmogelijk bij ons want optimale pad A sluit mogelijk al opties pad B uit etc)). Sneller door te prunen (eventueel zelfs met inadmissible heuristics).

        - Hoog niveau: 

            - Simpelweg de volgorde waarin we op laag niveau de nets leggen.
            - Ingewikkelder: 
                Hill descent toepassen om sommige draden te verkorten. We kiezen de draden die we schrappen en herleggen aan de hand van bepaalde heuristieken.

                Eerst op laag niveau nets leggen zonder rekening te houden met soft constraints of zelfs hard constraints en daarna op hoog niveau bekijken welke conflicten zijn ontstaan, voordat we die op laag niveau oplossen door sommige paden te herleggen, nu wel rekening houdend met de constraints.

CONCLUSIE TODO resultaten eventueel al verweven in methode?
    Resultaten tonen per algoritme als we dat nog niet gedaan hebben. Algoritmes vergelijken. Eventueel benoemen dat de algoritmes werken zoals we verwachten. Zeker benoemen als dat niet zo is.

    Toekomstige verbeteringen zouden kunnen liggen in het toepassen van heuristiek x of y. Natuurlijk zonder te zeggen dat we daar niet aan toe zijn gekomen o.i.d.
