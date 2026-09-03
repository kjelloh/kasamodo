# Överväg metoder för att kunna beräkna belastning och deformation på hus-stomme på fyra hörn-plintar?

## Termer

* Ett isotropt material har samma egenskaper i alla riktningar.
* Ett ortotropt material har olika egenskaper i olika, inbördes vinkelräta riktningar.
  * Trä är det klassiska exemplet.

## 20260824

Ok, nu har jag sovit på saken och läst på vad chatGPT verkar säga och som jag misstänker är bra ledtrådar?

* För fackverk av stänger verkar det finnas en vedertagen metod att applicera FEM?
* Den bygger på en elasticitetsberäkning baserat på förhållandet mellan Krafter och deformation.
* För varje stång upprättas ett förhållande F = Ku.
  * K är en styvhetsmatris som beskriver stångens materialegenskaper för töjning
  * 'u' är en vektor med rumskoordinater för alla frihetsgarder (för xz-planet två per nod = (u1x,u1y,u3x,u3y) för nod 1 och 3.)
  * Och F är kraftvektorn is amma frihetsgrader.

För hela väggen kan vi nu upprätta en 'global' styvhetsmatris för alla noder i fackverket.

* Vi fixerar (definierar) alla frihetsgrader i u.
  * I xz-planet får vi två frihetsgrader per nod.
  * För exempelväggen från igår, med fem noder, kan u bli (u1x,u1z,u2x,u2z,...u5x,u5z)
  * Detta bestämmer nu vilka krafter som är i vektorn F.

Så chatGPT beskriver ekvationen F = Ku som 'F beskriver vad som trycker/drar i konstruktionen. u beskriver hur konstruktionen får lov att röra sig'.

* Jag är lite osäker på om detta är helt korrekt?
* Vi borde ju kunna beräkna också okända krafter?

  * Om vi beskriver noder om inte får röra sig genom att sätta dem till 0.
  * Och innför de krafter som belastar kontruktionen (taklast, tyngd, vidlast).
  * Så kan vi ju fortfarande vilka beräkna vilka krafterna blir på hörn-plintarna?

Jag fick detta exempel från chatGPT som jag tyckte gav bra insikt.

```text

  Storhet         Exempel	                        Känd/okänd
  Kraft	          vindlast 10 kN	                Känd
  Förskjutning	  upplag uz=0	                    Känd
  Reaktionskraft	kraft i plint	                  Okänd
  Förskjutning	  deformation i mitten av väggen	Okänd

  FEM-systemet använder de kända storheterna för att lösa de okända.
```

Så här tänker jag nu.

* Med styvhetsmatris kan jag räkna på fackverk av stänger i tryck och drag.
* Jag kan till exempel använda en SAT-solver på metrisekvkationen med randvillkor.
  * Ur detta får jag veta sambandet mellan defomration och krafter i fackverket
* Jag verkar kunna modellera husets fysiska egenskaper genom att reducera det till 'element'

  * Stång-element (fackverk)
  * Skiv-element
  * Fästelement (skruvförband, spikförband, anhåll, svetsfogar. limfogar mm)
  * Bärelement (balkar)
  * fler...?

Det som nu verkar fattas är hur jag modellerar momentkrafter, skjuvningar, deformation inom ramen för 'Eulers knäckfall'osv? 

Jag presenterade mitt renomenag för chatGPT och fick en del ledtrådar hur jag kan lära mig mer och gå vidare.

* Det verkar som om en vanlig förenkling är att modellera fästelement som 'fjädrar'?
* Det verkar som om det är vedertagen prasix att skilja på tre domäner av modellen?

  * Elementmodell (modell av enkilda element)
  * Global FEM-modell – hur alla element kopplas ihop.
  * Dimensioneringskontroller – om de krafter/spänningar/stabilitetsfenomen som FEM ger upphov till är acceptabla.
* Det verkar som en rimlig ansats?
* **VIKTIGT**: Verktor **u är FÖRSKJUTNINGAR**!
  * Det kanske jag undermedvetet förstod, men ändå!
* Jag verkar nu känna till de vanligaste klasserna av externa laster?
  * egenvikt
  * snölast
  * vindlast
  * nyttig last (troligen möbler, vattensystem, inredning mm?)
* Jag blev rättad att en SAT-solver INTE är rätt (jag behöver en solver för linjär algebra)

  * Ku=F är ett  klassiskt linjärt algebraiskt system.
  * och löses normalt med numeriska linjäralgebra-metoder.
    * LU-faktorisering
    * Cholesky-faktorisering
    * Conjugate Gradient
    * sparse direct solvers
    * andra iterativa sparse-matrismetoder?
  * En SAT-solver är gjord för logiska satisfierbarhetsproblem, inte för den här typen av kontinuerlig mekanik.
  * Jag undrar dock om inte Microsoft Z3 'ndå klarar även linjär algebra?

* Det verkar som chatGPT bekräftar min förståelse av olika slags 'element' för modellen?

  * Den återgav det jag sagt som en slags grafik (med engelska och svenska termer)

  ```text
                           MODEL
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
        Beam               Shell             Truss
          │                  │                  │
      balkar              skivor             stänger
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                       Connector
                             │
                     skruv/spik/beslag
  ```

Jag fick också återkoppling på hur vridmoment faktiskt hanteras i samma ekvation F = Km.

* Men nu innförs vridning som en egen dimension.
* Och motsvarande 'kraft' är ett moment.
* Jag fick exemplet för en '2D Euler–Bernoulli-balk'
  * varje nod typiskt tre frihetsgrader: ux,uz, phi_y
  * Där phi_y är rotation kring en y-axel
* Jag förstår detta som att även rotaion är en 'töjning'
* Så vi kan beskriva rotations-töjning i styvhetsmatrisen
* Och uttöka även F med en komponent My (moment kring en y-axel)

Så det verkar som om vi täcker alla deformationer i konstruktionen relaterat till töjning med en styvhetsmatris?

Nu står jag innför att förstå (påminna mig) termer och samband som chatGPT nämner men som jag ännu inte riktigt grundar i min fysikförståelse.

* Jag tror **τ=Gγ** avser skjuvning?
  * G är skjuvmodulen (analog med Töjningsmodulen E i **σ=Eϵ**)
  * Men hur såg dessa storheter ut nu igen?
* Jag tror **EI** avser 'styvhet'
  * Där I är 'vridstyvhetsmomentet' eller vad det nu hette?
  * Och I hade en väldigt konstig dimension?
  * Hur kan jag förstå EI relativt Ku (K beror ju på E)?
* Det verkar som 'knäckning' handlar om stabilitet?
  * Jag får intrycket att knäckning aldig skall uppstå?
  * Men vi behöver säkra upp att vi har tillräckliga marginaler för att förhindra knäckning?
  * Och kanske marginaler att bära upp även om knäckning skulle uppstå?

Jag gick också igång på chatGPT sammanfattningar om utfall från olika analyser?

* Från globala F = Ku får vi:
  * nodförskjutningar
  * nodrotationer
  * stödreaktioner.
* För varje element F = Ku fpr vi:
  * normalkraft N
  * tvärkraft V
  * moment M
  * torsion T
  * spänningar
  * töjningar.
 
* Därefter kan vi göra stabilitetsanalysen?
  * Riskerar vi (klarar vi) knäckning?
  * Riskerar vi (klarar vi) buckling?
  * P-Δ-effekter (Vad är det?)
  * geometrisk icke-linearitet (Vad är det?)
* Och slutligen säkerställer vi dimensioneringen?
  * Det vill säga, Klarar materialet och förbanden de krafter som uppstår?
  * Eller, hur dimensionerar jag material och förband så de klarar de krafter som uppstår?
* För skivelement verkar följande storheter användas?
  * Ex,Ez,Gxz (för xz-planet)
  * Storheten ν och skivans tjocklek.
  * Men vilken ekvation löser vi här?

Jag undrar också om det förslag chatGPT gav på ordning av implementering kanske faktiskt har värde?

* Steg 1 — 2D truss (stång, fackverk) F = Ku med u = (ux,uz)
  * Element: EA/L
  * Resultat: N,σ,ϵ,u.

* Steg 2 — 2D balk F = Ku med u = (ux,uz,θy)​	
  * Elementet får: EA, EI, GA
  * och kan ge: N,V,M.

* Steg 3 — 2D skiva
  * Lägg till skivelement med: Ex,Ez,Gxz,ν,tjocklek.
  * Ge akt på att modellera trä (även OSB?) som ortropt 

* Steg 4 — connectors (förband)
  * Modellera exempelvis skruvförband som fjädrar: F=kΔu.
  * 'Det är en väldigt användbar förenkling.'

* Steg 5 — 3D. Varje nod får exempelvis: u = (ux,uy,uz,θx,θy,θz)
  'Nu börjar du kunna representera hela huset.'

* Steg 6 — stabilitet (knäckning, buckling, andra ordningen)
  * Jag antar chatGPT avser 'andra ordningens deformationer'?
  * Så defaormationer som inte faller ut av linjär analys F = Ku?
  * Vad kan det vara för någonint?
  * Plastisk deformation?
  * Brott?

Men jag får nog jobba lite med att formulera stegen på ett sätt som jag själv förstår. För nu duger det chatGPT föreslagit som ledtrådar till de bakomliggande fysikaliska principerna, storheterna och sambanden?

Jag undrar om Microsoft Solever Z3 kan lösa linjära ekvationssystem?

* Nja, visar det sig.
  * Z3 är en 'optimerare' som söker lösningar på 'olikheter'
  * T.ex., Givet u>0 vilken är det optimala värdet av F = Ku?
  * Kanske är chatGPT ute och cyklar, men jag köper att vi söker en entydig last och deformation med F = Ku.
* För huskontruktioner har F = Ku alltid en unik lösning för en unik belastning.
  * För små (elastiska) defomationer u är K konstant.
* Och för att lösa detta system använder vi hällre en speciell algorithm för linjär algebra.
  * Matrisen F verkar bli 'gles' då många (alla?) interna noder har kraftsumman 0.
  * Så en lösare specialiserad på glesa matriser är av värde.
* P-Delta-effekter är kraftförändringar som uppstår på grund av förskjutningar i sidled.

  * En kraft P som normal går rakt ner genom en stång, kan föskjutas så den 'lutar'
  * Nu är P inte längre rakt ner genom stången (regeln) utan skapar ett moment runt foten.
  * Om förskjutningen av toppen är 'delta' blir momenten rint foten 'delta x P'.
  * Därav namnet 'Delta-P-effekter'
* Det verkar som om för Delta-P-effekter behöver vi iterera defomrationerna?
  * K är fortfarande konstant.
  * Men deformationen orsakar nya krafter och nya deformationer.
  * Min intuition säger mig att vi klan behöva iterera till stabilt läge?
* För icke länjär deformation kan vi behöva använda numeriska metoder?
  * Om vi till exempel vill räkna på plastisk deformation?
  * Eller på brott i trä-element?
  * Och ändå säkerställa stabilitet?
  * Då blir K en funktion av u.
  * Och vi kan använda till-exmpel newton-rapson-linkande numeriska metoder?
* Det kan kanske bli aktuellt att 'optimera' (använda Z3) av andra skäl?
  * Kanske minimera material och materialkostnader?
  * Men då förändrar vi ju också K (andra material)?
  * Så då är systemet inte längre linjärt.
  * Och vi löser en annan ekvation = kostnaden för att uppnå godtagbart K?
  * Men kanske just därför är Z3 ett bra hjälpmedel för detta?

Jag undrar vilka C++-bibliotek för lösning av linjära ekvationssystem det finns?

Jag frågade chatGPT och fick förslag.

* [Eigen](https://libeigen.gitlab.io/?utm_source=chatgpt.com)

```cpp
Eigen::SparseMatrix<double> K;
Eigen::VectorXd F;
Eigen::VectorXd u;

Eigen::SimplicialLDLT<Eigen::SparseMatrix<double>> solver;

solver.compute(K);
u = solver.solve(F);
```

  * Jag blir ju sugen att starta ett C++-projekt i Kasamodo repo?!

* [SuiteSparse](https://github.com/DrTimothyAldenDavis/SuiteSparse/tree/dev)


## 20260823

Så var det dags att börja bena ut hur vi kan säkra upp Kasamodos stomme?

Jag vill kunna ställa husets stomme på bara fyra plintar i hörnen. Så jag behöver en metod att beräkna belastning och deformation för den konstruktion jag väljer.

* Vilken matte var det igen som man använder?
  * Det har något att göra med en skjuv-modul om jag kommer ihåg rätt?
* Kan jag hacka ihop en funktion för att räkna på en trä-vägg med fackverk?

Det verkar som om vi kan börja med en 2D-modell av en vägg med skiva och fackverk?

* En enkel vägg kan väl vara fyra hörn och två diagonaler (fackverk)

```text
z
↑
│   3 ●────────────● 4
│     │╲          ╱│
│     │ ╲        ╱ │
│     │  ╲      ╱  │
│     │   ╲    ╱   │
│     │    ╲  ╱    │
│   1 ●─────●─────● 2
│           5
└────────────────────→ x
```

* Vi har då 5 noder där vi kan ansätta randvillkor och beräkna jämvikt?
  * Position i xz för varje nod.
  * Krafter i varje nod.
  * Moment i varje nod

* För denna beräkning behöver vi materialens fysiska egenskaper.

  * Elasticitestmodul (Youngs modul) E (N/m2 i.e., Pa)
  * Används i sambandet σ=Eϵ
    * Normalspänning σ (N / m2)
    * Töjning ϵ (faktor)

Sedan är det kanske Eulers knäckningsfall som ger möjliga deformationer i y-led som vi behöver räkna på?

Lite snack med chatGPT ger mig lite ledtrådar.

För FEM i ett fackverk verkar det som om vi räknar på varje nod-par för sig?

* För FEM söker vi **F = Ku** för säg stången 1,3 i xz-planet.

  * u är då kolumn-vektorn **(u1x,u1z,u3x,u3z)**
  * **K** är styvhetsmatrisen.
  * Och **F** är kraftvektorn (kolumnvektor) **(F1x,F1z,F3x,F3z)**