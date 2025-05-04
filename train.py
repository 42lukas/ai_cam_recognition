from ultralytics import YOLO


# 1. Lade vortrainiertes YOLOv8n-Modell
model = YOLO("yolov8n.pt")

# 2. Starte das Training
model.train(
    data="data.yaml",           # <- Pfad zu deiner YAML-Datei
    epochs=75,                  # <- leicht hochsetzen, du hast jetzt mehr Daten
    imgsz=640,                  # <- bleibt Standardgröße
    batch=16,                   # <- gut bei CPU/M1 (RAM checken)
    name="ball_model_v2",       # <- neuer Modellname, um v1 nicht zu überschreiben
    project="runs/train",       # <- Trainings-Output
    verbose=True,               # <- zeigt Trainingsergebnisse pro Epoch
    workers=0,                  # <- wichtig bei M1, um Hänger zu vermeiden
    seed=42,                    # <- für reproduzierbares Training
)