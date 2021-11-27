# IT-Projekt: Schlaue Lise

## Inhaltsverzeichnis

1. [Anaconda Installation](#anaconda-installation)
2. [Lokale Installation](#Probleme-mit-Timeout-Error)

## Anaconda Installation

Eine benutzerfreundliche Python-Distribution ist Anaconda.
Hier die Anleitung dazu von Herrn Prof. Dr.
Albrecht von der TH Nürnberg aus der Vorlesung _Text Analytics_.

### Lokale Installation

Es bietet sich an, mit **virtuellen Environments** zu arbeiten, wenn man mit Python arbeitet,
um (Dependency-) Konflikte mit anderen Projekten zu vermeiden.

Dazu gibt es hier im Verzeichnis die Datei `environment.yml`. 
Über diese Datei wird automatisch ein Environment für das Projekt angelegt.

Weiterführende Informationen dazu hier:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Hierzu muss allerdings erst Anaconda installiert sein, siehe nächster Schritt [Installation](#installation).

### Installation

Eine populäre Python-Distribution ist [Anaconda](https://www.anaconda.com/).
Wenn diese Distribution installiert wird, werden automatisch eine Vielzahl an Werkzeugen und Bibliotheken für Data Science mit installiert.
Entweder installiert man Anaconda (inklusive GUI für die Verwaltung), oder wenn man volle Kontrolle über alles haben will und sich auf der Kommandozeile zu Hause fühlt, kann man stattdessen [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installieren.

Weblinks zu den Installationsanleitungen:

- <https://docs.anaconda.com/anaconda/install>
- <https://docs.conda.io/en/latest/miniconda.html>

Darüber hinaus brauchen wir noch weitere Libraries.
Für die Installation gibt es bei Anaconda den Kommandozeilen-Befehl `conda`,
der ein sauberes Paket-Management beinhaltet. Er ist für das Basis-Setup dem Standard-Installer `pip`
für Python vorzuziehen. Allerdings sind nicht alle Pakte über `conda` verfügbar,
sodass gelegentlich auf `pip` ausgewichen werden muss. Die notwendigen Pakete stehen in der Datei [`environments.yml`](environment.yml).

Nach der Anaconda-Installation könnt ihr das "Anaconda Prompt" (z.B. in Windows aus dem Startmenü erreichbar).

Führt dann folgende Kommandos auf der Kommandozeile aus:

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
# Da ein lokales Environment etwas hässlich in der Kommandozeile
# angezeigt wird, bietet sich noch folgender Befehl an, der den
# Root-Folder (hier: env) des Environments als Namen anzeigt:
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

**Optional**, wenn ihr mit Rasa X (Local Mode) arbeitet:

```sh
(env)> pip install -U sanic-jwt==1.6.0
```

### Hinweise zu Rasa X 
Rasa X formatiert automatisch eure YAML-Files, das ist nicht weiter schlimm und führt nur in Forms zu Problemen. Da werden nämlich die Slots von Rasa X alphabetisch sortiert. Das ist ein bekannter Bug, der noch nicht behoben wurde. In unserem Fall ist es bspw. so:

Eigentlich werden bei der `informationen_form` die `Slots` in folgender Reihenfolge abgefragt:

```
Alter -> Geschlecht -> Haustiere -> Drogen
```

Nach der Sortierung durch Rasa X wird dann aber folgendermaßen abgefragt:

```
Alter -> Drogen -> Geschlecht -> Haustiere
```

Es ist also notwendig, die `Slots` entsprechend zu ändern, damit sie in der richtigen Reihenfolge abgefragt werden:

```
Alter -> BGeschlecht -> CHaustiere -> Drogen
```

Das ist nur ein unschöner Workaround, aber er funktioniert. 

## Probleme mit Timeout-Error

Es kann sein, dass manche Computer zu langsam sind, um die entsprechend auf Eingaben zu reagieren. Es kommt dann zu einem `TimeoutError`. Dieser kann folgendermaßen umgangen werden:

```python
# <Projektverzeichnis>/env\Lib\site-packages\rasa\core\channels\console.py

DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS = 20 # default: 10
```

Das ist ein Workaround und keine richtige Lösung. Damit können aber langsame Maschinen die Anfragen bearbeiten.

## Rasa Befehle

```sh
conda info --env
conda activate
rasa train
rasa shell
conda deactivate
```

## Um Rasa Custom actions zum laufen zu bringen
1. in endpoints.yml müssen Zeile 13 und 14 entkommentiert werden
2. in einem extra Terminal muss "rasa run actions" eingegeben werden 

am besten mit rasa interactive die Funktionalität der slots überprüfen.