# Nutzerhandbuch
Die "SCHLAUE-LISE" ist eine in Rasa entwickelte Anwendung. Mit Rasa kann jeder personalisierte, automatisierte Interaktionen mit Anwendern in einem beliebig großen Umfang erstellen. Rasa stellt die Infrastruktur und die Werkzeuge bereit, die für die Entwicklung eines Assistenten erforderlich sind, die die Kommunikation zwischen Anwender und Unternehmen grundlegend verbessert.
Diese Anwendung kann lokal auf einem Desktop-PC ausgeführt werden. Die Migration auf einem mobilen Endgerät wurde während diesem Projekt nicht getestet. Im Kern wurden die Funktionen "Schlafen", "Spenden", "Hygiene" und "Medizin" implementiert. Diese vier Funktionen sind nur ein Teil der künftig nutzbaren Anwendung und wurden zur Erstellung dieses Prototyps zufällig ausgewählt.
Die eben genannten Funktionen werden im Anschluss aufgelistet und erklärt. Dabei wird gezeigt wie einem Anwender, geholfen werden kann, ein Bedürfnis zu stillen. Der Anwender wird dabei von einen Chatbot durch die Anwendung geleitet. Hat der Anwender alle benötigten Informationen eingegeben ist das Ziel ein "Deeplink", der die benötigte Unterstützung bereithält. Die gesamte Kommunikation findet in deutscher Sprache statt. Während der Entwicklung wurde großen Wert aufgelegt, den Einstieg in die Kommunikation mit der Anwendung sehr niedrig zu gestallten. So wurde dieser eine einfache Sprache trainiert. Dabei spielt es keine Rolle, ob eine Kommunikation zwischen Anwender und Anwendung mit einem Halbsatz oder sogar mit einem Einwortsatz beginnt. Die Nutzung durch den Anwender ist in dieser Version nur textuell möglich. Am Ende und nach erfolgreicher Eingabe aller benöigten Informationen, wird dem Anwender eine Liste mit entsprechenden Einrichtungen angezeigt. Diese Liste ist wie schon beschrieben mit einem "Deeplink" verbunden und führt zu den entsprechenden Stellen.
Informationen zur Installation von Rasa und zum Tech-Stack findest du in der readme.md.
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
##### Zusammenfassug Beispiel 1:
In diesem Beispiel sucht eine Person zunächst allgemein nach Hygieneartikel. Nach der Aufforderung den gesuchten Artikel einzugeben, wird eine Liste mit Ausgabestellen angezeit. Es besteht die Möglichkeit über einen Deeplink die Ausgabestellen aufzurufen.
#### Beispiel 2 "Brauche Taschentücher":
```
Chatbot: Hallo.
Anwender: Ich will 'Taschentücher' .
Chatbot: 'Taschentücher' bekommst du bei dieser Einrichtung (Deeplink)
```
##### Zusammenfassug Beispiel 2:
In diesem Beispiel sucht eine Person direkt nach einem Hygieneartikel, dem Taschentuch. Es wird eine Liste mit Ausgabestellen angezeit. Es besteht die Möglichkeit über einen Deeplink die Ausgabestellen aufzurufen.
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
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Männer.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: Nein.
Chatbot: Diese Stellen (Deeplink) helfen dir, eine langfristige Unterkunft für Erwachsene zu finden.
```
##### Zusammenfassung Beispiel 1:
In diesem Beispiel sucht ein Erwachsener Mensch eine längerfristige Unterkunft. Er nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Unterkünften die Erwachsene aufnehmen.
#### Beispiel 2 "Langfristig Jugendlicher":
```
Chatbot: Hallo.
Anwender: Ich suche was zum Pennen.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 16.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Frauen.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 16
        - Geschlecht: weiblich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: nein
        - Unter 22 (jugendlich): ja
Chatbot: Brauchst du eine Notunterkunft?
Anwender: Nein.
Chatbot: Diese Stellen (Deeplink) helfen dir, eine langfristige Unterkunft für Jugendliche zu finden.
```
##### Zusammenfassung Beispiel 2:
In diesem Beispiel sucht ein Jugendlicher eine längerfristige Unterkunft. Er nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Unterkünften die Jugendliche aufnehmen.
#### Beispiel 3 "Notunterkunft für Männer":
```
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 23.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Männer.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: ja.
Chatbot: Hier findest du die Notunterkünfte (Deeplink) für Männer.
```
##### Zusammenfassung Beispiel 3:
In diesem Beispiel sucht ein erwachener Mann eine Notunterkunft. Er nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Männer ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 4 "Notunterkunft für Frauen":
```
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 23.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Frauen.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 23
        - Geschlecht: weiblich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: ja.
Chatbot: Hier findest du die Notunterkünfte (Deeplink) für Frauen.
```
##### Zusammenfassung Beispiel 4:
In diesem Beispiel sucht eine erwachene Frau eine Notunterkunft. Sie nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Frauen ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 5 "Notunterkunft für Diverse":
```
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Divers.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: divers
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: Ja.
Chatbot: Nürnberg verfügt derzeit noch über keine gesonderten Schlafplatzangebote für nicht-binäre Menschen.\n\nWir zeigen dir deshalb alle Einrichtungen für Männer und    Frauen an, damit du selbst entscheiden kannst, welche Option für dich am besten passt.
Chatbot: Hier findest du alle Notunterkünfte (Deeplink) für Erwachsene aufgelistet.
```
##### Zusammenfassung Beispiel 5:
In diesem Beispiel sucht eine erwachener Non-Binärer Mensch eine Notunterkunft. Dieser nimmt keine Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von allen Notunterkünften die Frauen und Männer ohne Haustier und ohne Drogenprobleme aufnehmen. Da es zum Zeitpunkt der Entwicklung des Prototyps keine Unterkunft für Non-Binäre Menschen gab, wird auf beide Unterkunftarten verwiesen.
#### Beispiel 6 "Notunterkunft für Jugendliche":
```
Chatbot: Hallo.
Anwender: Ich suche was zum Pennen.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 16.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Divers.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 16
        - Geschlecht: divers
        - Haustier: nein
        - Drogen: nein
        - Volljährig: nein
        - Unter 22 (jugendlich): ja
Chatbot: Brauchst du eine Notunterkunft?
Anwender: Ja.
Chatbot: Hier kannst du eine Notunterkunft (Deeplink) für junge Menschen finden.
```
##### Zusammenfassung Beispiel 6:
In diesem Beispiel sucht eine Jugendlicher eine Notunterkunft. Er nimmt keine Drogen und hat kein Haustier. Das Geschlecht spielt keine Rolle für die selektion der Unterkünfte. Der Endpunkt ist eine Auflistung von Notunterkünften die nur Jugendliche ohne Haustier und ohne Drogenprobleme aufnehmen.
#### Beispiel 7 "Notunterkunft mit Tieren":
```
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Männer.
Chatbot: Hast du ein Haustier?
Anwender: Ja.
Chatbot: Nimmst du Drogen?
Anwender: Nein.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: ja
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: ja.
Chatbot: Hier kannst du eine Notunterkunft (Deeplink) für Menschen mit Haustier finden.
```
##### Zusammenfassung Beispiel 7:
In diesem Beispiel sucht ein erwachener Mann eine Notunterkunft. Er nimmt keine Drogen und hat jedoch ein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die Menschen mit Haustier und ohne Drogenprobleme aufnehmen. Hat ein Erwachsener ein Haustier und ein Drogenproblem wird bei der Auswahl der Notunterkünfte das Haustier priorisiert. 
#### Beispiel 8 "Notunterkunft mit Drogenabhängigkeit":
```
Chatbot: Hallo.
Anwender: Ich suche eine Unterkunft.
Chatbot: Ich benötige noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Chatbot: Wie alt bist du?
Anwender: 32.
Chatbot: Welchem Geschlecht fühlst du dich zugehörig?
Anwender: Männer.
Chatbot: Hast du ein Haustier?
Anwender: Nein.
Chatbot: Nimmst du Drogen?
Anwender: Ja.
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: nännlich
        - Haustier: nein
        - Drogen: ja
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Anwender: ja.
Chatbot: Hier kannst du eine Notunterkunft (Deeplink) für Menschen mit Drogenproblemen finden.
```
##### Zusammenfassung Beispiel 8:
In diesem Beispiel sucht ein erwachener Mann eine Notunterkunft. Er nimmt Drogen und hat kein Haustier. Der Endpunkt ist eine Auflistung von Notunterkünften die Menschen ohne Haustier aber mit Drogenproblemen aufnehmen. Hat ein Erwachsener ein Haustier und ein Drogenproblem wird bei der Auswahl der Notunterkünfte das Haustier priorisiert.
