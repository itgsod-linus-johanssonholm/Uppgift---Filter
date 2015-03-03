# Filter #

Den här uppgiften går ut på att skriva tre olika funktioner för att filtrera listor.

## Bedömningsmatris ##

## Planering ##

| Förmågor                         | E 																																   | C | A |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Aktivitetsdiagram och pseudokod  | Du använder pseudokod och/eller aktivitetsdiagram för att planera dina uppgifter utifrån exempel, eller i samråd med utbildaren.  | Som för E, men utan exempel eller handledning |   |
| Anpassning					   | Du anpassar med viss säkerhet planeringen till uppgiften 																		   |   | Som för E, men med säkerhet
| Utvärdering | Med viss säkerhet utvärderar du, med enkla omdömen, programmets prestanda, använder datalogiska begrepp, och bedömer din egen förmåga | som för E, men med nyanserade omdömen | Som för C, men med säkerhet, och med förbättringsförslag

## Syntax och Teori ##
| Förmågor                                       | E 																			| C | A |
|------------------------------------------------|------------------------------------------------------------------------------|---|---|
| Datatyper					                     | Du kan redogöra för och använda de vanligaste datatyperna                    |   |   |
| Grundläggande syntax		                     | Du kan redogöra för och använda programmeringsspråkets grundläggande syntax  |   |   |
| Villkor och IF-satser		                     | Du kan redogöra för och använda villkor och IF-satser                        |   |   |
| Loopar & iteration                             | Du kan redogöra för och använda loopar och iterera över listor               |   |   |

## Kodning och kodningsstil ##

| Förmågor                                      | E                                                                         | C                                               | A                                              |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| Komplexitet									| *Du kan skriva enkla program*                                               | Du kan skriva lite mer avancerade program       | Du kan skriva komplexa program
| Sekventiell- & funktionsbaserad programmering | Du använder dig av sekventiell programmering och fördefinerade funktioner | *Du skapar och använder enkla funktioner*         | Du skapar mer komplexa funktioner              |
| Struktur		 				                | Du skriver kod som är delvis strukturerad, har en konsekvent kodningsstil och tydlig namngivning | Som för E, men du skriver kod som är helt strukturerad |   			   |
| Felsökning                                    | Du felsöker på egen hand enkla syntaxfel | Som för E, men systematiskt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men med effektivitet   	   |
| Dokumentering 								| Du skriver kod som är delvis kommenterad									|  												  | Du skriver kod som är utförligt kommenterad    |



## Uppgiftsbeskrivning ##

Du har fått i uppdrag att skriva ett program som filtrerar listor.
Den skall innehålla tre funktioner: `filter`, `exclude`, och `unique`.

Filtrera: `filter`

`filter` tar en array och ett värde som argument, och returnerar en lista endast innhållande dessa värden.

Utesluta: `exclude`

`exclude` tar en array och ett värde som argument, och returnerar en lista utan dessa värden.

Unika: `unique`

`unique` tar en array och returnerar en lista med unika värden.

### Exempel ###

### Python ####

    filter(array: [["bosse", "daniel", "edvard", "bosse", "bosse"], "bosse") >>> ["bosse", "bosse", "bosse"]

    exclude(array: [["bosse", "daniel", "edvard", "bosse", "bosse"], "bosse") >>> [daniel", "edvard"]

    unique(array: [["bosse", "daniel", "edvard", "bosse", "bosse"]) >>> ["bosse","daniel", "edvard"]

## Genomförande ##

### Versionshantering ###

Gör en `fork` av repot. Klona sen ner till din dator. Kom ihåg att checka in dina ändringar och synka med GitHub.

### Flödesschema ###

Innan du börjar koda ska du skapa ett flödesschema för programmet.
När du känner att du har ett fungerande flödesschema, be läraren att kolla på det.

### Kodning ###

Programmet skall utvecklas med hjälp av testerna.

##### Python #####

Skapa funktionerna i `lib/filters.py`

Testerna finns i `test/testexclude.py`,`test/testfilter.py` och `test/testunique.py`

Kor `nosetests --rednose test/<testfilnamn>` för att köra testerna för den specifika funktionen, eller enbart `nosetests --rednose` för att köra samtliga testfiler.

## Tips och länkar ##

* Om du inte kan beskriva lösningen i ord kommer det vara så gott som omöjligt att skapa ett flödesschema
* Fundera på vilka variabler som behövs
* Testa flödesschemat med hjälp av penna och papper

### Python ###

Läs mer om villkor och if-satser i övning 27-30 och while-loopar i övning 33 i [*Learn Python the Hard Way*](http://learnpythonthehardway.org)

* [Learn Python the Hard Way - Exercise 27: Memorizing Logic](http://learnpythonthehardway.org/book/ex27.html)
* [Learn Python the Hard Way - Exercise 28: Boolean Practice](http://learnpythonthehardway.org/book/ex28.html)
* [Learn Python the Hard Way - Exercise 29: What If](http://learnpythonthehardway.org/book/ex29.html)
* [Learn Python the Hard Way - Exercise 30: Else and If](http://learnpythonthehardway.org/book/ex30.html)
* [Learn Python the Hard Way - Exercise 33: While loops](http://learnpythonthehardway.org/book/ex33.html)
