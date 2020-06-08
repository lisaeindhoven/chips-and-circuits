# stapsgewijs pseudocode versie 0.1: RANDOM ./gates&netlist/chip_0/netlist_1.csv

1) random gate kiezen

2) random verbinding kiezen tussen gate uit 1) en een van de twee mogelijke vriendjes

3) random richting: 
    - 1-4 opties: TEL OPTIES IN MATRIX
        - niet terug
        keuze gemaakt:
        PAD TOEVOEGEN AAN WIRELIJST IN GATEOBJECT
        PAD TOEVOEGEN IN MATRIX
    - 0 opties: ongeldig resultaat

4) doel bereikt? 
    nee? -> stap 3
    ja? -> stap 1, volgende gate
