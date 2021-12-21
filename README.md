# IT-Projekt: Schlaue Lise

## Inhaltsverzeichnis

1. [Anaconda Installation](#anaconda-installation)
2. [Rasa X](#rasa-x)
3. [CI / CD Pipeline](#ci--cd-pipeline)
4. [Probleme mit Timeout-Error](#probleme-mit-timeout-error)
5. [Rasa Befehle](#rasa-befehle)
6. [User Manual](#user-manual)
7. [Ausblick](#ausblick)

## Anaconda Installation

Hier die Anleitung zum Installieren von Python und den notwendigen Package Mangern von Herrn Prof. Dr. Albrecht von der TH Nürnberg aus der Vorlesung _Text Analytics_.

### Lokale Installation

Es bietet sich an, mit **virtuellen Environments** zu arbeiten, wenn man mit Python arbeitet,
um (Dependency-) Konflikte mit anderen Projekten zu vermeiden.

Dazu gibt es hier im Verzeichnis die Datei [`environments.yml`](environment.yml). 
Über diese Datei wird automatisch ein Environment für das Projekt angelegt.

Weiterführende Informationen dazu hier:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Zunächst muss allerdings erst Anaconda installiert sein, siehe nächster Schritt [Installation](#installation).

### Installation

[Anaconda](https://www.anaconda.com/) ist eine populäre Python-Distribution ist .
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

## Rasa X 
### Fehlende Dependecy
Wenn mit Rasa X (Local Mode) gearbeitet wird, wird noch folgende Dependency benötigt:

```sh
(env)> pip install -U sanic-jwt==1.6.0
```

Rasa X ist ein Werkzeug, welches auf das Conversational Driven Development (CDD) zugeschnitten ist. 
Es ist eine Web-Anwendung mit einem Adminbereich zum Sichten und Bearbeiten der gesammelten Daten und der Möglichkeit, den Bot frühzeitig an echte Nutzer:innen weiterzugeben, um möglichst realistische Daten zu sammeln. 

![Rasa X CDD Circle](https://rasa.com/docs/rasa-x/img/loop.png "Rasa X CDD Circle")

Rasa X ist im Gegensatz zu Rasa ein Closed Source Tool, welches aber in einer freien Version allen Entwickler:innen zur Verfügung gestellt wird. 

### Installation

Die Installation ist in den [Rasa X Docs](https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode) sehr gut beschrieben. 
Sollte man vorhaben, Rasa X auf einem Server laufen zu lassen, findet man ebenfalls dort einige Installationsanleitungen.

### Bekannter Bug

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

## CI / CD Pipeline

In diesem Projekt wurde eine CI / CD Pipeline (_Continous Integration_ / _Continous Deployment_) eingerichtet. 

Über [Google Cloud](https://cloud.google.com/) läuft aktuell noch ein Rasa X Server, den wir zum Testen des Chatbots verwendet haben. Dieser Server wird nach Beendigung des Projekts nicht mehr weitergeführt werden, weswegen er hier nicht verlinkt wird. 

Die CI/CD läuft über [GitHub Actions](https://docs.github.com/en/actions) (Workflows sind im Verzueichnis `.github` hinterlegt) und nutzt außerdem den [Dockerfile](Dockerfile), um den [Rasa Action Server](https://rasa.com/docs/action-server/) zu aktualisieren. 

Ausgelöst werden die Workflows wenn eines der beiden Ereignisse eintritt: 

- Es wird auf `main` gepushed
- Es wird auf `main` gepushed und es gab Änderungen in `actions`.

Im ersten Fall wird ein aufgrund des veränderten Codes ein neues Model trainiert und auf den Google Cloud Server hochgeladen. Im anderen Fall wird ein neues Image auf [DockerHub](https://hub.docker.com/) gepushed, welches dann vom Rasa Action Server genutzt werden kann. 

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
conda info --env # Anzeige aller möglichen Environments
conda activate ./env # aktivieren des Environments
```
### Chatbot trainieren

```sh
rasa train # Modell trainieren
rasa shell # Chatbot auf der Konsole starten
# oder
rasa interactive # trackt die gespeicherten Daten während der Konversation und ermöglicht einen Export des Dialogs als Stories etc.
# Alternativ Rasa X (Local) starten
rasa x
```

### Rasa Action Server (local)
Um lokal den [Rasa Action Server](https://rasa.com/docs/action-server/) zu aktivieren muss in einem extra Terminal folgender Befehl ausgeführt werden: 

```sh
# Im Projektverzeichnis
(env)> rasa run actions
```

## User Manual

Das User Manual ist nicht im README selbst enthalten und kann [hier](user-manual.md) aufgerufen werden.

## Ausblick
Aktuell kommt es noch zu einigen Fehlern bei der Benutzung der Shortcuts. Das heißt, bei der Verkürzung der Dialoge durch die direkte Eingabe von relevanten Informationen landet man manchmal in falschen Pfaden. Dies liegt an der Komplexität und Ähnlichkeit der einzelnen Themenbereiche. 

Um das zu lösen muss der Chatbot in Zukunft mit echten Nutzer:innen weiterentwickelt werden, die realitätsnahe Beispieleingaben tätigen und diese in das Lernverhalten des Chatbots mit aufgenommen werden können. Hierzu bietet sich Rasa X an.

Weiter mögliche nächste Schritte für die Fortführung der Entwicklung des Chatbots sind:
- Der Bot startet die Konversation, aktuell beginngt eine Unterhaltung immer mit Eingabe des/der Anwender:in
- Implementierung einer Spracheingabe, aktuell ist nur das eintippen von Text umgesetzt
- Entwicklung von Teststories und Einbindung in die CI

