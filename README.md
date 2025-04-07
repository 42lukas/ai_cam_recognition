# YOLOv8 Webcam Demo

Ein einfaches Python-Projekt zur Objekterkennung über die Webcam mit einem vortrainierten YOLOv8-Modell.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ausführen

```bash
python webcam_detect.py
```

Drücke **Q**, um das Live-Bild zu beenden.

---

> Modell: `yolov8n.pt` wird automatisch von Ultralytics geladen (kleines, schnelles Modell).
> Kann später durch dein eigenes Modell (`best.pt`) ersetzt werden.

## Ziel
- YOLOv8 verstehen
- Kamerazugriff üben
- Bild-Erkennung lokal testen
- Know-how für dein NAO-Projekt sammeln
