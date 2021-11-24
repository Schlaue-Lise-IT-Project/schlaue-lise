# Nutzerhandbuch
Die "SCHLAUE-LISE" ist eine mit dem Rasa Framework entwickelte Chatbot-Anwendung. Mit Rasa ist es möglich personalisierte, automatisierte Interaktionen mit Anwender:innen in einem beliebig großen Umfang zu erstellen. Rasa stellt die Infrastruktur und die Werkzeuge bereit, die für die Entwicklung eines Machine-Learning-basierten Assistenten erforderlich sind.


Die hier im Repository hinterlegte Anwendung stellt einen solchen digitalen Assistenten dar. Dieser Assistent ist eine prototypische Erweiterung zu einer bereits konzipierten mobilen Applikation, die im Rahmen des [SiWo-Projekts](https://www.e-beratungsinstitut.de/projekte/siwo/) des Instituts für E-Beratung Nürnberg entwickelt werden soll. Die Anwendung wurde im Rahmen des Studienprojekts als reine Konsolenanwendung entwickelt. 

Im Kern wurden die Anwendungsfälle für die Kategorien `Schlafen`, `Spenden`, `Hygiene` und `Medizin` implementiert. Diese sind nur ein Teil der künftig nutzbaren Anwendung und wurden zur Erstellung dieses Prototyps ausgewählt.
Die Pfade für die oben genannten Anwendungsfälle werden im Anschluss aufgelistet und erklärt. Am Ende jedes Pfades wird ein sogenannter `Deep Link`, der in der finalen Version der mobile Applikation dazu genutzt werden kann, direkt zu der entsprechenden View zu springen. 

Die gesamte Kommunikation findet in deutscher Sprache statt. Während der Entwicklung wurde großen Wert darauf gelegt, den Einstieg in die Kommunikation mit der Anwendung sehr niederschwellig zu gestallten. So spielt es beispielsweise keine Rolle, ob eine Kommunikation mit einem Halbsatz oder sogar nur mit einem Wort beginnt. Am Ende und nach erfolgreicher Eingabe aller benötigten Informationen, wird der nutzenden Person eine Liste mit Einrichtungen angezeigt, die in der jeweiligen Situation der Anwender:innen hilfreich sein könnten.

  

## Spenden
Im Anwendungsfall "Spenden" hat man die Möglichkeit, Spenden zu erhalten oder zu tätigen. Zudem kann man eine Geldspende anfragen. Dafür wird die anwendende Person vom Chatbot aufgefordert, eine entsprechende Eingabe zu tätigen. Anschließend kann die Person auswählen, ob sie die eingegebenen Artikel benötigt oder spenden möchte. Nach dieser Eingabe, wird eine Auflistung der Einrichtungen ausgegeben.
### Beispieleingaben:
#### Um zum Thema Spenden zu kommen:
```
Ich möchte Spenden erhalten
Ich brauche Spenden
ich brauch was
Ich möchte selbst spenden
Ich hab was abzugeben
Ich brauch Kleidung
ich brauch Jacke
Ich benötige eine Hose
Ich brauch einen Pullover
ich brauch dringend Unterwäsche
brauch nen BH
ich brauch nen Slip
ich brauch nen Schlafsack
benötige eine Isomatte
ich brauch eine Decke
ich brauch ein Kissen
ich brauch was zu essen
ich brauch Nahrungsmittel
ich benötige Kochzubehör
ich brauch nen Topf
ich brauch eine Pfanne
benötige nen Campingkocher
ich brauch Technik
ich brauch ein neues Handy
ich brauch Kopfhörer
ich will nen Laptop
ich brauch Freizeitartikel
ich brauch was zur Bildung
```
#### Geldspende benötigen:
```
Ich brauch Geld.
Ich brauch Kohle.
Bin pleite.
brauch geld.
```
#### Beispiel 1 "Spende Hygieneartikel benötigt":
```
Eingabe: Ich brauch was.
Chatbot: Ich habe verstanden, dass es um das Thema Spenden geht. Um welche Spendenartikel handelt es sich?
Eingabe: Tampons.
Chatbot: Tampons und andere Hygieneartikel findest du bei dieser Einrichtung (Deep Link).
```
##### Zusammenfassung Beispiel 1:
Die Person benötigt Tampons.
#### Beispiel 2 "Eine Spende benötigen":
```
Eingabe: Ich brauch was
Chatbot: Ich habe verstanden, dass es um das Thema Spenden geht. Um welche Spendenartikel handelt es sich?
Eingabe: Schlafsack.
Chatbot: Möchtest du diese Dinge: Schlafsack erhalten?
Eingabe: Ja.
Chatbot: Alles klar. Diese Artikel: Schlafsack findest du bei diesen Stellen: Obdachlosenhilfe.
```
##### Zusammenfassung Beispiel 2: 
In diesem Beispiel sucht die Person nach einem Schlafsack.
#### Beispiel 3 "Eine Spende tätigen":
```
Eingabe: Ich hab was abzugeben
Chatbot: Ich habe verstanden, dass es um das Thema Spenden geht. Um welche Spendenartikel handelt es sich?
Eingabe: Schlafsack.
Chatbot: Möchtest du diese Dinge: Schlafsack erhalten?
Eingabe: Nein
Chatbot: Alles klar. Diese Artikel: Schlafsack kannst du bei diesen Stellen abgeben: Obdachlosenhilfe.
```
##### Zusammenfassung Beispiel 3:
Die Person möchte einen Schlafsack spenden.
#### Beispiel 4 "Geldspende erhalten"
```
Eingabe: Ich brauch Geld.
Chatbot: ...hier ist der Ansprechpartner im Sozialamt (Deep Link). Und hier verschiedene Stiftungen (Deep Link)
```
##### Zusammenfassung Beispiel 4:
Die Person benötigt Geld.
## Hygieneartikel
Hier können Anwender:innen beliebige Hygieneartikel anfragen und bekommt die entsprechenden Ausgabestellen angezeigt. Diese sind wieder mit einem `Deep Link` verbunden.
### Beispieleingaben:
#### Allgemein Hygieneartikel benötigt:
```
Ich brauche Hygieneartikel.
Wo bekomme ich Hygieneartikel her?
```
#### Spezifische Suche:
```
Ich brauche Binden
Ich will Kondome
Ich brauche dringend ein OB
Brauch eine Packung Watte
Ein Stück Seife
Ich benötige Tampons
Ich brauche Shampoo
Ich möchte Duschgel
Brauche dringend Klopapier
Ich brauche Windeln
Ich benötige Küchenrollen oder Zewa
Ich brauche Tempos
Brauche Taschentücher
Ich brauche dringend Reinigungstücher
Ich brauche unbedingt Feuchttücher]
```
#### Mögliche Hygieneartikel:
```
Seife
Binden
Tampons
OB
Watte
Shampoo
Duschgel
Klopapier
Windeln
Küchenrollen
Zewa
Tempos
Taschentücher
Reinigungstücher
Feuchttücher
```
#### Beispiel 1 "Seife benötigt"
```
Eingabe: Ich brauch Hygieneartikel.
Chatbot: Welchen Hygieneartikel benötigst du?
Eingabe: Ich benötige Seife.
Chatbot: Seife bekommst du bei dieser Einrichtung (Deep Link)
```
##### Zusammenfassug Beispiel 1:
In diesem Beispiel sucht eine Person zunächst allgemein nach Hygieneartikel. Nach der Aufforderung den gesuchten Artikel einzugeben, wird eine Liste mit Ausgabestellen angezeit. Es besteht die Möglichkeit über einen Deep Link die Ausgabestellen aufzurufen.
#### Beispiel 2 "Brauche Taschentücher":
```
Eingabe: Ich will Taschentücher .
Chatbot: Taschentücher bekommst du bei dieser Einrichtung (Deep Link)
```
##### Zusammenfassung Beispiel 2:
In diesem Beispiel sucht eine Person direkt nach einem Hygieneartikel, dem Taschentuch. Es wird eine Liste mit Ausgabestellen angezeit. Es besteht die Möglichkeit über einen Deep Link die Ausgabestellen aufzurufen.
## Schlafen
Im Anwendungfall `Schlafen` gibt es eine Vielzahl an Möglichkeiten, die der oder die Anwender:in wählen kann. Diese Vielzahl ergibt sich aus den in Deutschland gültigen Gesetzten und Vorschriften, denen die verschiedenen Einrichtungen bzw. Unterkünfte unterliegen. Da die unterkunftsuchende Person diese möglicherweise nicht kennt, wurde dieser Pfad so gestaltet, dass eine passende Unterkunft angeboten bzw. angezeigt wird.

Um die Eingabe so einfach wie möglich zu gestalten, werden zunächst persönliche Daten von der Anwendung abgefragt. Die persönlichen Daten sind das Alter, das Geschlecht, die Frage nach einem Haustier und Drogenabhängigkeit. Danach wird nach der Art der Unterkunft gefragt. Diese teilen sich grundsätzlich in zwei Kategorien ein, nämlich in (kurzfristige) Notunterkunft und längerfristige Unterkunft. 
 
Nach erfolgreicher Eingabe dieser Informationen werden eine oder mehrere Unterkunftsmöglichkeiten angezeigt. Aufgrund der Vielzahl an möglichen Eingaben werden alle acht Endpunkte nachfolgend in Beispielen aufgelistet.
### Beispieleingaben:
#### Unterkunft benötigt:
```
Ich suche einen Schlafplatz für heute Nacht
Ich benötige einen Schlafplatz für heute
Ich will heute Nacht einen Schlafplatz
Ich möchte einen Schlafplatz für heute Nacht
Ich brauche heute ein Dach über dem Kopf
Ich brauche heute was zum pennen
Ich brauche für heute Nacht was zum pennen
Notunterkunft
Ich suche eine Notunterkunft
Ich suche eine Wohnung
Ich brauche eine Wohnung
Ich will eine Wohnung
Ich suche nach einem Heimplatz
Ich möchte ins Obdachlosenheim
Ich suche längerfistig einen Schlafplatz
Ich möchte weg von der Straße
Wohnung
schlafen
Dach über dem Kopf
ratzen
knacken
schlummern
pennen
Ich brauche einen Ort zum Pennen
```
#### Beispiel 1 "Langfristig Erwachsener":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Männer.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: Nein.
Chatbot: Diese Stellen (Deep Link) helfen dir, eine langfristige Unterkunft für Erwachsene zu finden.
```
##### Zusammenfassung Beispiel 1:
In diesem Beispiel sucht ein Erwachsener eine längerfristige Unterkunft. Er nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Einrichtungen, die Unterstützung bei der Suche nach einer längerfristigen Unterkunft für Erwachsene anbieten.
#### Beispiel 2 "Langfristig für Jugendliche":
```
Eingabe: Ich suche was zum Pennen.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 16.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Frauen.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 16
        - Geschlecht: weiblich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: nein
        - Unter 22 (jugendlich): ja
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: Nein.
Chatbot: Diese Stellen (Deep Link) helfen dir, eine langfristige Unterkunft für Jugendliche zu finden.
```
##### Zusammenfassung Beispiel 2:
In diesem Beispiel sucht eine Jugendliche eine längerfristige Unterkunft. Sie nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Einrichtungen, die Unterstützung bei der Suche nach einer längerfristigen Unterkunft für Jugendliche anbieten.
#### Beispiel 3 "Notunterkunft für Männer":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 23.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Männer.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: ja.
Chatbot: Hier findest du die Notunterkünfte (Deep Link) für Männer.
```
##### Zusammenfassung Beispiel 3:
In diesem Beispiel sucht ein junger Erwachsener eine Notunterkunft. Er nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Männer ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 4 "Notunterkunft für Frauen":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 23.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Frauen.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 23
        - Geschlecht: weiblich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: ja.
Chatbot: Hier findest du die Notunterkünfte (Deep Link) für Frauen.
```
##### Zusammenfassung Beispiel 4:
In diesem Beispiel sucht eine erwachsene Frau eine Notunterkunft. Sie nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Frauen ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 5 "Notunterkunft für Diverse":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Divers.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: divers
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: Ja.
Chatbot: Nürnberg verfügt derzeit noch über keine gesonderten Schlafplatzangebote für nicht-binäre Menschen.\n\nWir zeigen dir deshalb alle Einrichtungen für Männer und    Frauen an, damit du selbst entscheiden kannst, welche Option für dich am besten passt.
Chatbot: Hier findest du alle Notunterkünfte (Deep Link) für Erwachsene aufgelistet.
```
##### Zusammenfassung Beispiel 5:
In diesem Beispiel sucht eine erwachsener non-binärer Mensch eine Notunterkunft. Dieser nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von allen Notunterkünften die Frauen und Männer ohne Haustier und ohne Drogenprobleme aufnehmen. Da es zum Zeitpunkt der Entwicklung des Prototyps keine Unterkunft für non-binäre Menschen gab, wird auf beide Unterkunftarten verwiesen.
#### Beispiel 6 "Notunterkunft für Jugendliche":
```
Eingabe: Ich suche was zum Pennen.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 16.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Divers.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 16
        - Geschlecht: divers
        - Haustier: nein
        - Drogen: nein
        - Volljährig: nein
        - Unter 22 (jugendlich): ja
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: Ja.
Chatbot: Hier kannst du eine Notunterkunft (Deep Link) für junge Menschen finden.
```
##### Zusammenfassung Beispiel 6:
In diesem Beispiel sucht ein non-binärer Jugendlicher eine Notunterkunft. Er nimmt keine Drogen und hat kein Haustier. Das Geschlecht spielt keine Rolle für die Auswahl der Unterkünfte, da es in Nürnberg nur danach geht, ob der Mensch jugendlich ist oder nicht. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Jugendliche ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 7 "Notunterkunft mit Tieren":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Männer.
Chatbot: Hast du ein Haustier?
Eingabe: Ja.
Chatbot: Nimmst du Drogen?
Eingabe: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: ja
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: ja.
Chatbot: Hier kannst du eine Notunterkunft (Deep Link) für Menschen mit Haustier finden.
```
##### Zusammenfassung Beispiel 7:
In diesem Beispiel sucht ein erwachsener Mann eine Notunterkunft. Er nimmt keine Drogen, hat jedoch ein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die Menschen mit Haustier und ohne Drogenprobleme aufnehmen. Hat ein Hilfesuchender ein Haustier und ein Drogenproblem wird bei der Auswahl der Notunterkünfte das Haustier priorisiert. Auch das Alter spielt keine Rolle. 
#### Beispiel 8 "Notunterkunft mit Drogenabhängigkeit":
```
Eingabe: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Eingabe: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Eingabe: Männer.
Chatbot: Hast du ein Haustier?
Eingabe: Nein.
Chatbot: Nimmst du Drogen?
Eingabe: Ja.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: ja
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: ja.
Chatbot: Hier kannst du eine Notunterkunft (Deep Link) für Menschen mit Drogenproblemen finden.
```
##### Zusammenfassung Beispiel 8:
In diesem Beispiel sucht ein erwachsener Mann eine Notunterkunft. Er nimmt Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die Menschen ohne Haustier aber mit Drogenproblemen aufnehmen. Hat ein Hilfesuchender ein Haustier und ein Drogenproblem wird bei der Auswahl der Notunterkünfte das Haustier priorisiert. 
