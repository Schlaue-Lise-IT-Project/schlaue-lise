# Nutzerhandbuch
Die "SCHLAUE-LISE" ist eine in Rasa entwickelte Anwendung. Mit Rasa kann jeder personalisierte, automatisierte Interaktionen mit Anwendern in einem beliebig großen Umfang erstellen. Rasa stellt die Infrastruktur und die Werkzeuge bereit, die für die Entwicklung eines Assistenten erforderlich sind, die die Kommunikation zwischen Anwender und Unternehmen grundlegend verbessert.
Diese Anwendung kann lokal auf einem Desktop-PC ausgeführt werden. Die Migration auf einem mobilen Endgerät wurde während diesem Projekt nicht getestet. Im Kern wurden die Funktionen "Schlafen", "Spenden", "Hygiene" und "Medizin" implementiert. Diese vier Funktionen sind nur ein Teil der künftig nutzbaren Anwendung und wurden zur Erstellung dieses Prototyps zufällig ausgewählt.
Die eben genannten Funktionen werden im Anschluss aufgelistet und erklärt. Dabei wird gezeigt wie einem Anwender, geholfen werden kann, ein Bedürfnis zu stillen. Der Anwender wird dabei von einen Chatbot durch die Anwendung geleitet. Hat der Anwender alle benötigten Informationen eingegeben ist das Ziel ein "Deeplink", der die benötigte Unterstützung bereithält. Die gesamte Kommunikation findet in deutscher Sprache statt. Während der Entwicklung wurde großen Wert aufgelegt, den Einstieg in die Kommunikation mit der Anwendung sehr niedrig zu gestallten. So wurde dieser eine einfache Sprache trainiert. Dabei spielt es keine Rolle, ob eine Kommunikation zwischen Anwender und Anwendung mit einem Halbsatz oder sogar mit einem Einwortsatz beginnt. Die Nutzung durch den Anwender ist in dieser Version nur textuell möglich. Am Ende und nach erfolgreicher Eingabe aller benöigten Informationen, wird dem Anwender eine Liste mit entsprechenden Einrichtungen angezeigt. Diese Liste ist wie schon beschrieben mit einem "Deeplink" verbunden und führt zu den entsprechenden Stellen.

  

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
Ich brauche Hygieneartikel.
Wo bekomme ich Hygieneartikel her?
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
In der Funktion "Schlafen" gibt es eine Vielzahl an Möglichkeiten, die der Anwender wählen kann. Diese Vielzahl ergibt sich aus den gültigen Gesetzten und Vorschriften, denen die verschiedenen Einrichtungen bzw. Unterkünfte unterliegen. Da der Anwender diese i.d.R. nicht kennt, wurde diese Funktion so gestaltet, dass der Anwender eine Unterkunft angeboten bekommt und nicht selbst entscheiden muss, wo er schlafen möchte. Um die Eingabe so einfach wie möglich zu gestalten, werden zunächst persönliche Daten von der Anwendung abgefragt. Die persönlichen Daten sind das Alter, das Geschlecht, Haustierbesitzer und Drogenabhängigkeit. Danach wird nach der Art der Unterkunft gefragt. Diese teilen sich in zwei Kategorien, der Notunterkunft und eine längerfristige Unterkunft. Nach erfolgreicher Eingabe dieser Informationen werden dem Anwender eine oder mehrere Unterkünfte angezeigt. Auf Grund der Vielzahl an möglichen Nutzereingaben werden alle acht Endpunkte nachfolgend in Beispielen aufgelistet.
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
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Wie 
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
