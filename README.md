# camera recognition AI

Ein kleines progress Repo bei der Erstellung eines eigenen KI-Modells. Später wird das KI-Modell in einem NAO Uni-Projekt weiterverwendet, um dem NAO Fußball spielen beizubringen. 

## Setup

###### bash / macOS
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

###### PowerShell / Windows
```PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Falls es beim SetUp des venv auf Windows zu einem Fehler wegen eingeschränkter Ausführungsrichtlinien kommt, hilft es meistens folgendes mit Administrator Rechten auszuführen:
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Neue Trainingsdaten vorbereiten

Um neue Traingsdaten vorzubereiten kann man einige Bilder oder ein Video verwenden. 
Mit der Datei `dataprep`/`video_slicing.py` kann ein Video in verschiedene Bilder umgewandelt und automatisch in die `train/` und `val/` Verzeichnisse soritert werden (80% `train/` und 20% `val/`).
Sonst die Bilder einzeln im `dataset` Ordner einsortieren und vernünftig in dem Format `train_XXXX.jpg` mit dem passenden Label `train_XXXX.txt` speichern. Dabei kommen die `*.jpg` Dateien in den `images/` Ordner und die `*.txt` in den Labels Ordner. 

-
Zum Labeln der Bilder empfehle ich dieses [Repository](https://github.com/HumanSignal/labelImg). Folge der Installation in dem Repository.

Danach öffne den Ordner mit den neuen Trainingsbildern und makiere in jedem Bild das gebrauchte Objekt. Nachdem man alle Bilder makiert hat liegen alle passenden Label `*.txt` Dateien im selben Verzeichnis. Verschiebe alle Dateien z.B. mit diesem Befehl für macOS:
```bash
mv dataset/images/train/*.txt dataset/labels/train/
```

oder für Windows:
```PowerShell
Move-Item -Path .\dataset\images\train\*.txt -Destination .\dataset\labels\train\
```
Sind nun alle `train_XXXX.jpg` Dateien im `dataset/images/train/`  und alle `val_XXXX.jpg` Dateien im `dataset/images/val/` Ordner, sowie alle Labeldateien `train_XXXX.txt oder val_XXXX.txt` im Ordner `dataset/labels/train/ oder dataset/labels/val/` kann das KI-Modell neu trainiert werden.

## KI trainieren mit trainingsdaten

Vor dem trainiern sollte man sicherstellen, dass ein neuer Name für das Modell ausgesucht wird und die Parameter für das Training angepasst werden.
```python
python train.py   # start a new training
```

## Live KI Kameratest

```python
python cam_detect.py   # standard yolo AI model
python test_model_live.py   # newest trained AI model
```

Drücke **Q**, um das Live-Bild zu beenden.




---


## Entwicklungsfortschritt

👉 [Hier geht's zum Devlog](DEVLOG.md)
