# Nutzerhandbuch
Die "SCHLAUE-LISE" ist eine mit dem Rasa Framework entwickelte Chatbot-Anwendung. Mit Rasa ist es möglich personalisierte, automatisierte Interaktionen mit Anwender:innen in einem beliebig großen Umfang zu erstellen. Rasa stellt die Infrastruktur und die Werkzeuge bereit, die für die Entwicklung eines Machine-Learning-basierten Assistenten erforderlich sind.


Die hier im Repository hinterlegte Anwendung stellt einen solchen digitalen Assistenten dar. Dieser Assistent ist eine prototypische Erweiterung zu einer bereits konzipierten Mobile App, die im Rahmen des [SiWo-Projekts](https://www.e-beratungsinstitut.de/projekte/siwo/) des Instituts für E-Beratung Nürnberg entwickelt werden soll. Die Anwendung wurde im Rahmen des Studienprojekts nur als reine Konsolenanwendung entwickelt. 

Im Kern wurden die Use-Cases für die Kategorien `Schlafen`, `Spenden`, `Hygiene` und `Medizin` implementiert. Diese sind nur ein Teil der künftig nutzbaren Anwendung und wurden zur Erstellung dieses Prototyps ausgewählt.
Die Pfade für die oben genannten Use-Cases werden im Anschluss aufgelistet und erklärt. Am Ende jedes Pfades wird ein sogenannter `Deep Link`, der in der finalen Version der Mobile App dazu genutzt werden kann, direkt zu der entsprechenden View zu springen. 

Die gesamte Kommunikation findet in deutscher Sprache statt. Während der Entwicklung wurde großen Wert darauf gelegt, den Einstieg in die Kommunikation mit der Anwendung sehr niederschwellig zu gestallten. So spielt es beispielsweise keine Rolle, ob eine Kommunikation mit einem Halbsatz oder sogar nur mit einem Wort beginnt. Am Ende und nach erfolgreicher Eingabe aller benötigten Informationen, wird der nutzenden Person eine Liste mit Einrichtungen angezeigt, die in der Situation des Menschen hilfreich sein könnten.

  

## Spenden
In der Funktion "Spenden" besteht die Möglichkeit zu wählen, welche Art von Spende getätigt werden möchte. Der Anwender hat die Wahl, ob er eine Spende benötigt oder eine Spende geben möchte. Dazu fordert der Chatbot den Anwender auf eine entsprechende Eingabe zu tätigen. Nach der Auswahl kann nun ein Artikel eingegeben werden. Nach der Eingabe wird eine Liste mit Einrichtungen angezeigt, die entsprechend Spenden annehmen oder Spenden verteilen. Wenn eine benötigte Spende ein Hygieneartikel ist, wird der Anwender in die Funktion "Hygieneartikel" weitergeleitet.
### Beispieleingaben (Intents) des Anwenders:
#### Spenden erhalten:
```
Ich brauch Spenden.
Ich brauch was.
Ich möchte Spenden erhalten.
```

#### Selbst spenden: 
```
Ich möchte selbst spenden.
Ich hab was abzugeben.
```

#### Geldspende benötigen:
```
Ich brauch Geld.
Ich brauch Kohle.
Bin pleite.
```
#### Beispiel 1 "Spende Hygieneartikel benötigt":
```
Chatbot: Hallo.
Anwender: Ich brauch was.
Chatbot: ... gehe zu Spenden-Übersicht.
Chatbot: Was für Spenden benötigst du?
Anwender: Ob.
Chatbot: Ob und andere Hygieneartikel findest du bei dieser Einrichtung (Deeplink).
```
#### Beispiel 2 "Eine Spende tätigen":
```
Chatbot: Hallo.
Anwender: Ich hab etwas abzugeben.
Chatbot: ...gehe zu Selbst Spenden.
Chatbot: Worum handelt es sich bei deiner Spende?
Anwender: Schlafsack.
Chatbot: Schlafsack kannst du in dieser Einrichtung (Deeplink) abgeben.
```
#### Beispiel 1 "Geldspende erhalten"
```
Chatbot: Hallo.
Anwender: Ich brauch Geld.
Chatbot: ...gehe zu Geldspenden-Übersicht.
Chatbot: ...hier ist der Ansprechpartner im Sozialamt (Deeplink). Und hier verschiedene Stiftungen (Deeplink)
```
## Hygieneartikel
Die Funktion "Hygieneartikel" ist total großartig. Hier kann der Anwender beliebige Hygieneartikel anfragen und bekommt die entsprechenden Ausgabestellen angezeigt. diese sind wieder mit einem "Deeplink" verbunden.
### Beispieleingaben (Intents) des Anwenders:
#### Hygieneartikel benötigt:
```

```
#### Beispiel 1 "Seife benötigt"
```
Chatbot: Hallo.
Anwender: Ich brauch 'Hygieneartikel'.
Chatbot: Welchen 'Hygieneartikel' benötigst du?
Anwender: Ich benötige 'Seife'.
Chatbot: 'Seife' bekommst du bei dieser Einrichtung (Deeplink)
```
#### Beispiel 2 "Brauche Taschentücher":
```
Chatbot: Hallo.
Anwender: Ich will 'Taschentücher' .
Chatbot: 'Taschentücher' bekommst du bei dieser Einrichtung (Deeplink)
```
## Schlafen
Im Use Case `Schlafen` gibt es eine Vielzahl an Möglichkeiten, die der oder die Anwender:in wählen kann. Diese Vielzahl ergibt sich aus den in Deutschland gültigen Gesetzten und Vorschriften, denen die verschiedenen Einrichtungen bzw. Unterkünfte unterliegen. Da die unterkunftsuchende Person diese möglicherweise nicht kennt, wurde dieser Pfad so gestaltet, dass eine passende Unterkunft angeboten bzw. angezeigt wird.

 Um die Eingabe so einfach wie möglich zu gestalten, werden zunächst persönliche Daten von der Anwendung abgefragt. Die persönlichen Daten sind das Alter, das Geschlecht, die Frage nach einem Haustier und Drogenabhängigkeit. Danach wird nach der Art der Unterkunft gefragt. Diese teilen sich grundsätzlich in zwei Kategorien ein, nämlich in (kurzfristige) Notunterkunft und längerfristige Unterkunft. 
 
Nach erfolgreicher Eingabe dieser Informationen werden eine oder mehrere Unterkunftsmöglichkeiten angezeigt. Aufgrund der Vielzahl an möglichen Eingaben werden alle acht Endpunkte nachfolgend in Beispielen aufgelistet.
### Beispieleingaben (Intents) des Anwenders:
#### Unterkunft benötigt:
```
Ich suche einen Schlafplatz für heute Nacht.
Ich suche eine Wohnung.
Ich möchte weg von der Straße.
Bleibe.
Schlafen.
```
#### Beispiel 1 "Langfristig Erwachsener":
```
```
#### Beispiel 2 "Langfristig Jugendlicher":
```
```
#### Beispiel 3 "Notunterkunft für Männer":
```
```
#### Beispiel 4 "Notunterkunft für Frauen":
```
```
#### Beispiel 5 "Notunterkunft für Diverse":
```
```
#### Beispiel 6 "Notunterkunft für Jugendliche":
```
```
#### Beispiel 7 "Notunterkunft mit Tieren":
```
```
#### Beispiel 8 "Notunterkunft mit Drogenabhängigkeit":
```
```
