# Nutzerhandbuch

## Inhaltsverzeichnis
1. [Überblick](#überblick)
2. [Spenden](#spenden)
3. [Hygiene](#hygiene)
4. [Schlafen](#schlafen)
5. [Medizin](#medizin)
6. [URL, die am Ende erzeugt wird](#url-die-am-ende-erzeugt-wird)

## Überblick
Die "SCHLAUE-LISE" ist eine mit dem [Rasa Framework](https://rasa.com/) entwickelte Chatbot-Anwendung. Mit Rasa ist es möglich personalisierte, automatisierte Interaktionen mit Anwender:innen in einem beliebig großen Umfang zu erstellen. Rasa stellt die Infrastruktur und die Werkzeuge bereit, die für die Entwicklung eines Machine-Learning-basierten Assistenten erforderlich sind.

Die hier im Repository hinterlegte Anwendung stellt einen solchen digitalen Assistenten dar. Dieser Assistent ist eine prototypische Erweiterung zu einer bereits konzipierten mobilen Applikation, die im Rahmen des [SIWo-Projekts](https://www.e-beratungsinstitut.de/projekte/siwo/) des Instituts für E-Beratung Nürnberg entwickelt werden soll. Die Anwendung wurde im Rahmen des Studienprojekts als reine Konsolenanwendung entwickelt.

Im Kern wurden die Anwendungsfälle für die Kategorien `Schlafen`, `Spenden`, `Hygiene` und `Medizin` implementiert. Diese sind nur ein Teil der künftig nutzbaren Anwendung und wurden zur Erstellung dieses Prototyps ausgewählt.
Die Pfade für die oben genannten Anwendungsfälle werden im Anschluss aufgelistet und erklärt. Am Ende jedes Pfades wird ein sogenannter `Deep Link`, der in der finalen Version der mobile Applikation dazu genutzt werden kann, direkt zu der entsprechenden View zu springen.

Die gesamte Kommunikation findet in deutscher Sprache statt. Während der Entwicklung wurde großen Wert darauf gelegt, den Einstieg in die Kommunikation mit der Anwendung sehr niederschwellig zu gestallten. So spielt es beispielsweise keine Rolle, ob eine Kommunikation mit einem Halbsatz oder sogar nur mit einem Wort beginnt. Am Ende und nach erfolgreicher Eingabe aller benötigten Informationen, wird der nutzenden Person eine Liste mit Einrichtungen angezeigt, die in der jeweiligen Situation der Anwender:innen hilfreich sein könnten.

## Spenden

Im Anwendungsfall `Spenden` hat man die Möglichkeit, sich die Einrichtungen und Adressen anzeigen zu lassen, bei denen man Spenden erhalten oder tätigen kann. Dabei kann man entweder allgemein nach einer Spende fragen und bekommt dann eine Rückfrage, nach genaueren Informationen über den Spendenartikel oder man kann direkt nach einem bzw. mehreren konkreten Spendenartikeln fragen. Zudem kann man eine Geldspende anfragen. Dafür wird die anwendende Person vom Chatbot aufgefordert, eine entsprechende Eingabe zu tätigen. Anschließend kann die Person auswählen, ob sie die eingegebenen Artikel benötigt oder spenden möchte. Nach dieser Eingabe, wird eine Auflistung der möglichen Einrichtungen ausgegeben, welche die gewünschten Artikel anbieten. 

### Mögliche Eingaben um allgemein das Thema Spenden aufzurufen

Folgende Beispieleingaben sind für den allgemeinen Fall `Spenden` aktuell implementiert und können in einer Konversation problemlos eingesetzt werden, um dem Chatbot das Interesse am Thema Spenden mitzuteilen:

|                       | |
| --------              | --------    |
| Ich möchte ...        | [ Spenden erhalten ], [ selbst spenden ] |
| Ich brauche ...        | [ Spenden ], [ was ] | 
| Ich hab was abzugeben.| |
| Bin pleite.           | |
| Brauch Geld.          | |
|||

### Mögliche Eingabe um direkt ein (oder mehrere) spezifische Spendenartikel anzufragen

Es besteht die Möglichkeit auch direkt nach einem oder mehreren Spendenartikeln zu fragen. Folgende Beispieleingaben sind hierfür aktuell implementiert und können problemlos eingesetzt werden. Dadurch kann man den ersten Schritt durch die Konversation abkürzen.

|         |  |
| --------        | --------         |
| Ich brauche  | [ Kleidung ], [ Jacke ], [ einen Pullover ], [ dringend Unterwäsche ], [ nen Slip ], [ nen Schlafsack ], [ eine Decke ],  [ ein Kissen ], [ was zu essen ], [ Nahrungsmittel ], [ nen BH ], <br> [ nen Slip ], [ Nahrungsmittel ], [ nen Topf ], [ eine Pfanne ], [ Technik ], [ ein neues Handy ], [ Kopfhörer ], [ was zur Bildung ], [ Freizeitartikel ], [ Geld ], [ Kohle ] | 
| Ich benötige | [ eine Hose ], [ eine Isomatte ], [ Kochzubehör ], [ nen Campingkocher ] | 
| Ich will | nen Laptop|
|||

Aktuell sind folgende `Spendenartikel` im Code hinterlegt und werden vom Chatbot als solche erkannt:

|               |                  |               |                    |               |               |
| --------      | --------         | -------       | ------------       | -----         | -             |
| Kleidung      | Jacke            | Hose          | Pullover           | Unterwäsche   | BH            |
| Slip          | Schlafsack       | Isomatte      | Decke              | Kissen        | Nahrungsmittel|
| Essen         | Kochzubehör      | Topf          | Pfanne             | Campingkocher | Technik       |
| Handy         | Kopfhörer        | Laptop        | Freizeitartikel    | Bildung       | |
|               |                  |               |                    |               | |

### Beispiel Konversationen

#### Beispiel 1 "Allgemeine Anfrage nach einer Spende mit anschließender Spezifizierung (Schlafsack)":
```sh
Eingabe: Ich brauch was
Chatbot: Ich habe verstanden, dass es um das Thema Spenden geht. Um welche Spendenartikel handelt es sich?
Eingabe: Schlafsack.
Chatbot: Möchtest du diese Dinge: ['Schlafsack'] erhalten?
Eingabe: Ja.
Chatbot: Diese Artikel: 
        - Schlafsack 
        Findest du bei diesen Stellen: Obdachlosenhilfe.
        (Deep Link)
```
#### Beispiel 2 "Direkte Anfrage nach benötigtem Spendenartikel (Isomatte)":
```sh
Eingabe: Ich brauche eine Isomatte
Chatbot: Möchtest du diese Dinge: ['Isomatte'] erhalten?
Eingabe: Ja.
Chatbot: Diese Artikel: 
        - Isomatte 
        Findest du bei diesen Stellen: Obdachlosenhilfe. 
        (Deep Link)
```
#### Beispiel 3 "Eine Spende (Schlafsack) tätigen":
```sh
Eingabe: Ich hab was abzugeben
Chatbot: Ich habe verstanden, dass es um das Thema Spenden geht. Um welche Spendenartikel handelt es sich?
Eingabe: Schlafsack.
Chatbot: Möchtest du diese Dinge: ['Schlafsack'] erhalten?
Eingabe: Nein
Chatbot: Alles klar. Diese Artikel: Schlafsack kannst du bei diesen Stellen abgeben: Obdachlosenhilfe.
```
#### Beispiel 4 "Eine Geldspende erhalten"
```sh
Eingabe: Ich brauch Geld.
Chatbot: Hier ist der Ansprechpartner im Sozialamt: Ralph Wägner (0911 231 - 29 03)
        Und hier verschiedene Stiftungen: 
        ...
        (Deep Link)
```
#### Beispiel 5 "Direkte Anfrage nach mehreren Spendenartikeln (Hose, Jacke, Essen)"
```sh
Eingabe: Ich brauche eine Hose, Jacke, Essen.
Chatbot: Möchtest du diese Dinge: ['Hose', 'Jacke', 'Essen'] erhalten?
Eingabe: Ja 
Chatbot: Diese Artikel: 
        - Hose
        - Jacke
        - Essen
        Findest du bei diesen Stellen: (noch nicht im Prototyp hinterlegt)
        (Deep Link)
```

## Hygiene

Im Anwendungsfall `Hygiene` hat man die Möglichkeit, sich die Adressen und Einrichtungen anzeigen zu lassen, bei denen man beliebige Hygieneartikel erhalten kann. Dabei kann man entweder allgemein nach Hygieneartikeln fragen und bekommt dann eine Rückfrage, nach genaueren Informationen oder man kann direkt nach einem konkreten Hygieneartikel fragen. Bei erfolgreicher Anfrage werden jeweils die entsprechenden Ausgabestellen angezeigt. 

### Mögliche Eingaben um allgemein das Thema Hygieneartikel aufzurufen

Folgende Beispieleingaben sind für den allgemeinen Fall `Hygiene` aktuell implementiert und können so oder in leichter Abwandlung in einer Konversation problemlos eingesetzt werden um dem Chatbot das Interesse am Thema Hygiene mitzuteilen:

|||
|--- |--- |
| Ich brauche Hygieneartikel.||
| Ich benötige ... | [ ein Körperpflegeprodukt ], [ Hygieneartikel ] |
| Wo bekomme ich Hygieneartikel her? ||
| Wo gibt es Körperfplegeartikel ||
| Welche Einrichtung verteilt Hygienebedarf? ||
|||

### Mögliche Eingaben um direkt ein (oder mehrere) spezifische Hygieneartikel anzufragen

Es besteht die Möglichkeit auch direkt nach einem oder mehreren Hygieneartikeln zu fragen. Hierfür sind folgende Beispieleingaben aktuell implementiert und können problemlos eingesetzt werden. Durch den direkten Einstieg kann der erste Schritt durch die Konversation abgekürzt werden.

|||
|--- |--- |
| Ich brauche ... | [ Binden ], [ dringend ein OB], [ Shampoo ], [ Windeln ], [ Tempos ], [ dringend Reinigungstücher ], [ unbedingt Feuchttücher ]|
| Ich benötige ... | [ Tampons ], [ Küchenrollen oder Zewa ]|
| Brauche ... | [ eine Packung Watte ], [dringend Klopapier ], [ Taschentücher ]|
| Ich will | [ Kondome ]|
| Ich möchte | [ Duschgel ] |
| Ein Stück Seife ||
|||

Aktuell sind folgende `Hygieneartikel` im Code hinterlegt und werden vom Chatbot als solche erkannt:

|               |                 |                  |               |         |             |
----            |----             | --------         | --------      | ------- | -------     |
| Seife         | Binden          | Tampons          | OB            | Watte   | Shampoo     |
| Duschgel      | Klopapier       | Windeln          | Küchenrollen  | Zewa    | Tempos      |
| Taschentücher | Reinigungstücher| Feuchttücher     |               |         |             |
|               |                 |                  |               |         |             |

### Beispiel Konversationen

#### Beispiel 1 "Allgemeine Anfrage nach einem Hygieneartikel mit anschließender Spezifizierung (Seife)"

```
Eingabe: Ich brauch Hygieneartikel.
Chatbot: Welchen Hygieneartikel benötigst du?
Eingabe: Ich benötige Seife.
Chatbot: Alles klar. Diese Artikel:
        - Seife 
        Findest du bei diesen Stellen:
        ...
        (Deep Link)
```
#### Beispiel 2 "Direkte Anfrage nach benötigtem Hygieneartikel (Taschentücher)":

```
Eingabe: Ich will Taschentücher.
Chatbot: Alles klar. Diese Artikel: 
        - Taschentücher 
        Findes du bei diesen Stellen:
        ...
        (Deep Link)
```
#### Beispiel 3 "Direkte Anfrage nach mehreren benötigten Hygieneartikeln (Tampons, Klopapier)
```
Eingabe: Ich brauche Tampons und Klopapier.
Chatbot: Alles klar. Diese Artikel:
        - Tampons
        - Klopapier
        Findest du bei diesen Stellen:
        ...
        (Deep Link)
```

## Schlafen

Im Anwendungfall `Schlafen` gibt es eine Vielzahl an Möglichkeiten, die der oder die Anwender:in wählen kann. Diese Vielzahl ergibt sich aus den in Deutschland gültigen Gesetzten und Vorschriften, denen die verschiedenen Einrichtungen bzw. Unterkünfte unterliegen. Da die unterkunftsuchende Person diese möglicherweise nicht kennt, wurde dieser Pfad so gestaltet, dass eine passende Unterkunft angeboten bzw. angezeigt wird.

Um die Eingabe so einfach wie möglich zu gestalten, werden zunächst persönliche Daten von der Anwendung abgefragt. Die persönlichen Daten sind das Alter, das Geschlecht, die Frage nach einem Haustier und Drogenabhängigkeit. Danach wird nach der Art der Unterkunft gefragt. Diese teilen sich grundsätzlich in zwei Kategorien ein, nämlich in (kurzfristige) Notunterkunft und längerfristige Unterkunft.

Nach erfolgreicher Eingabe dieser Informationen werden eine oder mehrere Unterkunftsmöglichkeiten angezeigt.

### Mögliche Eingaben um allgemeine das Thema Schlafen aufzurufen:

Folgende Beispieleingaben sind für den allgemeinen Fall `Schlafen` aktuell implementiert und können so oder in leichter Abwandlung in einer Konversation problemlos eingesetzt werden um dem Chatbot das Interesse am Thema Schlafen mitzuteilen:

| | |
| ---- | ---- |
| Ich suche ... | [ einen Schlafplatz für heute Nacht ], [ eine Notunterkunft ], [ eine Wohnung ], [ nach einem Heimplatz ], [ längerfistig einen Schlafplatz ], [ einen Ort zum schlafen ], [ was zu pennen ], [ eine unterkunft ], [ eine Bleibe ]|
| Ich brauche ... | [ heute ein Dach über dem Kopf ], [ heute was zum pennen ], [ für heute Nacht was zum pennen ],  [ eine Wohnung ], [ einen Ort zum Pennen ], [ einen Platz zum Schlafen ], [ unterkunft ], [ einen platz zum pennen ], [ einen Schlafplatz ], [ einen Ort zum Schlafen ], [ einen Platz zum schlafen ], [ einen Platz zum pennen ], [ etwas zum schlafen ], [ eine unterkunft ]|
| Brauche was zum ... | [ pennen ], [ schlafen ]|
| Ich möchte ... | [einen Schlafplatz für heute Nacht ], [ ins Obdachlosenheim ], [ weg von der Straße ] |
| Ich will ... | [ heute Nacht einen Schlafplatz ], [ eine Wohnung ], [ pennen ] |
| Ich benötige | einen Schlafplatz für heute |
| Dach über | dem Kopf |
| Notunterkunft ||
| Wohnung ||
| schlafen ||
| ratzen ||
| knacken ||
| schlummern ||
| pennen ||

Nach einer solchen Eingabe fragt der Bot danach sukzessive die noch fehlenden Informationen über das Alter, Geschlecht, Haustier und Drogenabhängigkeit.

### Mögliche Eingaben um direkt benötigte Informationen bei einer Schlafenanfrage mitzuteilen

Es besteht die Möglichkeit auch direkt die geforderten Informationen in einer Anfrage mit zuformulieren. Hierfür ist die folgende kombinierte Beispieleingabe aktuell implementiert und kann problemlos eingesetzt werden. Durch den direkten Einstieg kann die Konversation je nach den angegeben Informationen erheblich abgekürzt werden. Man kann auch nur einen Teil der Informationen eingeben, der Chatbot fragt am Ende dann nur noch die fehlenden Informationen. 

||||||
|--- |--- |--- |--- |--- |
| Ich bin xx Jahre alt, ... | [ bin eine Frau ], [ männlich ], [ weder mann noch frau ] | habe [ einen ], [ keinen ] Hund, | nehme [ keine ] Drogen | und brauche [ einen Platz zum Schlafen ]
| Ich bin ... | [ männlich ], [ weiblich ] | habe [ einen ], [ keinen ]  Hund, | bin [ drogensüchtig ], [ nicht drogenabhängig ] | und suche [ was langfristiges ] |
|||

### Beispielkonversationen

#### Beispiel 1 "Allgemeine Anfrage nach einer Unterkunft (Langfristig Erwachsener)":

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
        - Geschlecht: männlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Brauchst du eine Notunterkunft?
Eingabe: Nein.
Chatbot: Diese Stellen (Deep Link) helfen dir, eine langfristige Unterkunft für Erwachsene zu finden.
```

#### Beispiel 2 "Anfrage nach einer Unterkunft mit direkter Eingabe der benötigten Informationen (keine Drogen, kein Haustier, männlich, volljährig)"

```
Eingabe: Ich bin 37, ein Mann, habe keinen Hund, nehme keine Drogen und brauche einen Platz zum Schlafen
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 37
        - Geschlecht: männlich
        - Haustier: nein
        - Drogen: nein
        - Volljährig: ja
        - Unter 22 (jugendlich): nein
Chatbot: Hier kannst du Notunterkünfte (Deep Link) für Männer finden.
```

#### Beispiel 3 "Anfrage nach einer Unterkunft mit direkter Eingabe eines Teils der benötigten Informationen (männlich, volljährig)"

```
Eingabe: Ich bin männlich, 32 und suche einen Platz zum schlafen
Chatbot: Ok, zum Thema 'Unterkunft' benötige ich noch einige allgemeine Informationen von dir. Diese werden nach dieser Unterhaltung nicht gespeichert.
Hast du ein Haustier?
Eingabe: Nein
Chatbot: Nimmst du Drogen?
Eingabe: Nein
Chatbot: Folgende Informationen wurden erfasst (werden nicht abgespeichert):
        - Alter: 32
        - Geschlecht: weiblich
        - Haustier: False
        - Drogen: False
        - Volljährig: True
        - Unter 22 (jugendlich): False
        Hier findest du die Notunterkünfte für Frauen.
        ...
        (Deep Link)
```

## Medizin

Im Anwendungsfall `Medizin` kann man sich die Adressen und Kontaktdaten zu medizinischen Hilfestellen entsprechend dem Versicherungsstatuses der/des Anwender:in anzeigen lassen.
Im Falle eines Notfalles, können im auch Notruf-Informationen abgefragt werden.

### Mögliche Eingaben um allgemein das Thema Medizin aufzurufen

Folgende Beispieleingaben sind für den allgemeinen Fall `Medizin` aktuell implementiert und können in einer Konversation problemlos eingesetzt werden um dem Chatbot das Interesse am Thema Medizin mitzuteilen:

|||
|--- |--- |
| Ich brauche ... | [ einen Arzt ], [ Medizin ], [ medizinische Hilfe ], [ Hilfe ]|
| Ich habe mich ... | [ verletzt ], [ geschnitten ], [ verbrannt ]|
| Ich suche einen Arzt ||
| Ich hatte einen Unfall ||
| Ich fühle mich nicht gut ||
| Unfall ||
|||

Nach einer solchen Eingabe erfolgt anschließend die Nachfrage nach dem Versicherungsstatus und ob es sich um eine Notfallsituation handelt.

### Mögliche Eingaben um direkt eine Notfallsituation anzugeben

Auch gibt es die Möglichkeit über direkte Informationseingabe eines Notfallstatus dem Chatbot das Interesse am Thema Medizin mitzuteilen. Hierzu sind folgende Beispieleingaben aktuell implementiert.

|||
|--- |--- |
| Ich brauche einen ... | [ Notartzt ], [ Sanitäter ], [ Sanni ], [ Sanka ], [ Krankenwagen ]|
| Es ist ein Notfall ||
| Notarzt ||
| Notfall ||

Nach einer solchen Eingabe wird danach nur noch der Versicherungsstatus abgefragt.

### Mögliche Eingabe um direkt den Versicherungsstatus anzugeben

Es gibt auch die Möglichkeit direkt den Versichungsstatus anzugeben um eine Medizin-Konversation zu beginnen. Folgende Beispieleingaben sind aktuell implementiert und führen ebenfalls zu einem Aufruf des Themas Medizin.

|||
|--- |--- |
| Ich bin ... | [ versichert ], [ nicht versichert ]|
| Habe ... | [ eine Versicherung ], [ keine Versicherung ]|
| Bin ... | [ versichert ], [ nicht versichert ]|
| versichert ||
| nicht versichert ||
| Versicherung
| keine Versicherung ||
|||

Nach einer solchen Eingabe wird danach nur noch nachgefragt ob es sich um eine Notfallsituation handelt und sofort ein Krankenwagen benötigt wird.

### Mögliche Eingaben um direkt Versicherungsstatus und Notfallsituation anzugeben

Man kann auch direkt in einem Satz den Versicherungsstatus und die Notfallinformation eingeben und gelangt dadurch direkt zur Ausgabe der entsprechenden Einrichtungen und Adressen. Dadurch werden in der Konversation zwei Schritte abgekürzt.

|||||
|--- |--- |--- |--- |
| Ich brauche ... | [ einen Notarzt ] | und ich bin | [ nicht versichert ], [ versichert ]|
| Ich bin ... | [ nicht versichert ], [ versichert ] | und | [ ich brauche einen Sanitäter ], [ ich brauche einen Arzt ], [ es ist ein Notfall ], [ es ist kein Notfall ] |
| Es ist | [ ein ], [ kein ] | Notfall und ich bin | [ nicht versichert ], [ versichert ] |
|||

### Beispielkonversationen

#### Beispiel 1 "Allgemeine Anfrage nach ärztlicher Hilfe":
 
```
Eingabe: Ich brauche einen Arzt 
Chatbot: Handelt es sich um einen Notfall und du brauchst sofort einen Notarzt? 
Eingabe: Nein 
Chatbot: Bist du krankenversichert? 
Eingabe: Nein 
Chatbot: > Deine erkannten Informationen sind: 
        ...
        (Deep Link)
```
#### Beispiel 2 "Medizinische Informationen in der Eingabe mitteilen - Versicherungsstatuses"

```
Eingabe: Ich bin versichert 
Chatbot: Handelt es sich um einen Notfall und du brauchst sofort einen Notarzt? 
Eingabe: Nein 
Chatbot: > Deine erkannten Informationen sind: 
        ...
        (Deep Link)
```

#### Beispiel 3: "Medizinische Informationen in der Eingabe mitteilen - Notfall"

```
Eingabe: ich brauche einen Notartz 
Chatbot: Bist du krankenversichert? 
Eingabe: Nein 
Chatbot: > Notfall registriert! 
           Öffne Notrufinformationen ...
           (Deep Link)
```

#### Beispiel 4: "Medizinische Informationen in der Eingabe mitteilen - Versicherungsstatus und Notfall"

```
Eingabe: Ich bin versichert und es ist ein Notfall 
Chatbot: > Notfall registriert! 
           Öffne Notrufinformationen ...
           (Deep Link)
```

## URL, die am Ende erzeugt wird
Am Ende jeder Story wird eine URL erzeugt, die alle befüllten Slots auflistet. Die befüllten Slots werden dabei nach dem Prinzip eines GET-Requests an die URL `www.schlaue-lise.de` gehängt. 
Wenn man diese URL antippt, soll man dann auf die Seite mit den jeweiligen Infos geleitet werden. Diese Internetseite existiert noch nicht. 
Damit die URL nach jeder Story ausgegeben wird, muss ans Ende jeder Story folgende Action hinzugefügt werden:
`action: action_answer_url`.
Hier kann es zu Timeout Errors kommen, wenn der Computer zu langsam ist. In der [README.md](README#probleme-mit-timeout-error) ist beschrieben, wie dieser behoben werden kann.
