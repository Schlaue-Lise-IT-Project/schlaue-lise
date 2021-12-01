# IT-Projekt: Schlaue Lise

## Inhaltsverzeichnis

1. [Anaconda Installation](#anaconda-installation)
2. [Rasa X](#rasa-x)
3. [Pipeline Deployment](#pipeline-deployment)
3. [Probleme mit Timeout Error](#Probleme-mit-Timeout-Error)
4. [Rasa Befehle](#rasa-befehle)

## Anaconda Installation

Eine benutzerfreundliche Python-Distribution ist Anaconda.
Hier die Anleitung dazu von Herrn Prof. Dr.
Albrecht von der TH Nürnberg aus der Vorlesung _Text Analytics_.

### Lokale Installation

Es bietet sich an, mit **virtuellen Environments** zu arbeiten, wenn man mit Python arbeitet,
um (Dependency-) Konflikte mit anderen Projekten zu vermeiden.

Dazu gibt es hier im Verzeichnis die Datei [`environments.yml`](environment.yml). 
Über diese Datei wird automatisch ein Environment für das Projekt angelegt.

Weiterführende Informationen dazu hier:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Zunächst muss allerdings erst Anaconda installiert sein, siehe nächster Schritt [Installation](#installation).

### Installation

Eine populäre Python-Distribution ist [Anaconda](https://www.anaconda.com/).
Wenn diese Distribution installiert wird, werden automatisch eine Vielzahl an Werkzeugen und Bibliotheken für Data Science mit installiert.
Entweder installiert man Anaconda (inklusive GUI für die Verwaltung), oder wenn man volle Kontrolle über alles haben will und sich auf der Kommandozeile zu Hause fühlt, kann man stattdessen [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installieren.

Weblinks zu den Installationsanleitungen:

- <https://docs.anaconda.com/anaconda/install>
- <https://docs.conda.io/en/latest/miniconda.html>

### Installation weiterer Packages

Darüber hinaus werden noch weitere Packages benötigt.
Für die Installation gibt es bei Anaconda den Kommandozeilen-Befehl `conda`,
der ein sauberes Paket-Management beinhaltet. Er ist für das Basis-Setup dem Standard-Installer `pip`
für Python vorzuziehen. Allerdings sind nicht alle Pakte über `conda` verfügbar,
sodass gelegentlich auf `pip` ausgewichen werden muss. Die notwendigen Pakete stehen in der Datei [`environments.yml`](environment.yml).

Nach der Anaconda-Installation kann das "Anaconda Prompt" (z.B. in Windows aus dem Startmenü erreichbar) genutzt werden.

Folgende Kommandos sind auf der Kommandozeile auszuführen:

**Optional**, wenn schon mal gemacht:

```sh
> conda config --append channels conda-forge
> conda update -n base conda
```

Dieser Schritt ist **IMMER AUSZUFÜHREN**:

```sh
# Wechsel in das Projektverzeichnis
> cd /Path/To/Project

# Erstellen des Environments hier im Projekt
> conda env create --prefix ./env -f environment.yml
```

Dieser Schritt ist **optional**, wenn es schon einmal konfiguriert wurde:

```sh
# Da ein lokales Environment etwas hässlich in der Kommandozeile angezeigt wird, bietet sich noch folgender Befehl an, der den Root-Folder (hier: env) des Environments als Namen anzeigt:
> conda config --set env_prompt '({name}) '
```

Dieser Schritt ist **IMMER AUSZUFÜHREN**:

```sh
# Aktivieren des Environments
> conda activate ./env

# SpaCy installieren
(env)> pip install -U spacy==3.2.0

# SpaCy Dateien nachladen
(env)> python -m spacy download de_core_news_md
```

**Optional**, wenn mit Rasa X (Local Mode) gearbeitet wird:

```sh
(env)> pip install -U sanic-jwt==1.6.0
```

## Rasa X 

http://34.159.228.55/login

Rasa X formatiert automatisch die YAML-Files, das ist nicht weiter schlimm und führt nur in Forms zu Problemen. Es werden die Slots von Rasa X alphabetisch sortiert. Das ist ein bekannter Bug bei Rasa, der noch nicht behoben wurde. In diesem Projektfall ist es bspw. so:

Eigentlich werden bei der `informationen_form` die `Slots` in folgender Reihenfolge abgefragt:

```
Alter -> Geschlecht -> Haustiere -> Drogen
```

Nach der Sortierung durch Rasa X wird jedoch folgendermaßen abgefragt:

```
Alter -> Drogen -> Geschlecht -> Haustiere
```

Es ist also notwendig, die `Slots` entsprechend zu ändern, damit sie in der richtigen Reihenfolge abgefragt werden:

```
Alter -> BGeschlecht -> CHaustiere -> Drogen
```

Das ist nur ein unschöner Workaround, aber er funktioniert. 

## Pipeline Deployment

## Probleme mit Timeout-Error

Es kann sein, dass manche Computer zu langsam sind, um entsprechend auf Eingaben zu reagieren. Es kommt dann zu einem `TimeoutError`. Dieser kann folgendermaßen umgangen werden:

```python
# <Projektverzeichnis>/env\Lib\site-packages\rasa\core\channels\console.py

DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 20 # default: 10
```

Das ist ein Workaround und keine richtige Lösung. Damit können aber langsame Maschinen die Anfragen bearbeiten.

## Rasa Befehle 

Um den Chatbot während der Implementierung zu testen, werden einige gängige Befehle für die Konsole benötigt, welche im folgenden aufgelistet sind.

### Environment auswählen

Für das Testen und ausführen des Chatbots muss das entsprechende Environment aktiviert werden.

```sh
conda info --env # anzeige aller möglichen Environments
conda activate ./env # aktivieren des Environments
```
### Chatbot trainieren

```sh
rasa train # Modell trainieren
rasa shell # Chatbot auf der Konsole starten
# oder
rasa interactive # trackt die gespeicherten Daten während der Konversation und ermöglicht einen Export des Dialogs als Stories etc.
```

### Rasa Custom actions
Um die Rasa Custom actions zu aktivieren muss in einem extra Terminal `rasa run actions` ausgeführt werden.

