Toestandsruimte / state space:
    - alle logische configuraties: 
        elke weg (tussen twee aangrenzende coordinaten) kan wel of niet bezet worden * n (zonder enig constraint, dus inclusief dubbele alignments).
        Dit gaat ervan uit dat routes niet achteruitgaan over dezelfde wegen maar wel elke mogelijke weg kunnen bezetten(in de praktijk onmogelijk)
        4x4 grid heeft 5x4 horizontale en 5x4 verticale wegen = 40
        nxn grid heeft 2 (weg wel of niet begaan) * 2 * n * (n+1)?

    een "weg", al dan niet ingevuld/gevolgd, ligt hier tussen

Lower bound:

    - (onhaalbare) ideale oplossing is n (gates) * kortste afstand, i.e. (absolute (verschil x) + absolute (verschil y) tussen twee gates.

Upper bound:

    - n (gates) * langste afstand (zoals hierboven) tussen twee gates. Eventueel + 2 voor een verdieping om de terugweg af te leggen zonder de eerdere routes te kruisen. Zie weergave hieronder:
    A->B->C->D->E
    up<-<-<-<-down

Datastructuur: 

    Path objecten met:

        - x, y(, z) coordinaat
        
        - adjacency list met gates waaraan dit path verbonden is
        
        OF

        - adjacency dict met gate(s) met dict met de route [(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)]


Python Graphs:
