# camera recognition AI

Ein kleines progress Repo bei der Erstellung eines eigenen KI-Modells. Später wird das KI-Modell in einem NAO Uni-Projekt weiterverwendet, um dem NAO Fußball spielen beizubringen. 

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ausführen

```bash
python cam_detect.py
```

Drücke **Q**, um das Live-Bild zu beenden.

---

> Modell: `yolov8n.pt` wird automatisch von Ultralytics geladen (kleines, schnelles Modell).
> Kann später durch dein eigenes Modell ersetzt werden.


## Entwicklungsfortschritt

👉 [Hier geht's zum Devlog](DEVLOG.md)
