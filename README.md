# IT-Projekt: Schlaue Lise

# Anaconda Installation

Eine benutzerfreundliche Python-Distribution ist Anaconda.
Hier die Anleitung dazu von Herrn Prof. Dr.
Albrecht von der TH Nürnberg aus der Vorlesung _Text Analytics_.

## Lokale Installation

### Virtuelle Environments

Es bietet sich an, mit virtuellen Environments zu arbeiten, wenn man mit Python arbeitet,
um (Dependency-) Konflikte mit anderen Projekten zu vermeiden.

Dazu gibt es hier im Verzeichnis die Datei `environment.yml`.

Über diese Datei wird automatisch ein Environment für das Projekt angelegt.

Weiterführende Informationen dazu hier:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Dazu muss allerdings erst Anaconda installiert sein, was im nächsten Schritt passiert.

### Installation

Eine populäre Python-Distribution ist [Anaconda](https://www.anaconda.com/).
Wenn ihr diese Distribution installiert, dann werden automatisch eine Vielzahl an Werkzeugen und Bibliotheken für Data Science mit installiert.
Installiert Anaconda (inklusive GUI für die Verwaltung). Wenn ihr lieber volle Kontrolle über alles haben wollt und euch auf der Kommandozeile zu Hause fühlt, installiert [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Hier die Installationsanleitungen:

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

DIeser Schritt ist **IMMER AUSZUFÜHREN**:

```sh
# Aktivieren des Environments
> conda activate ./env

# SpaCy installieren
(env)> pip install -U spacy==3.2.0

# SpaCy Dateien nachladen
(env)> python -m spacy download de_core_news_md
```

Ihr habt jetzt ein Python-Environment mit Rasa und allen Dependencies, SpaCy-Dateien, etc. Damit können alle mit demselben Background arbeiten.

## Rasa Befehle

```sh
conda info --env
conda activate
rasa train
rasa shell
conda deactivate
```
