from ultralytics import YOLO

# lädt das vortrainierte YOLOv8n-Modell
model = YOLO("yolov8n.pt")

# 2. Starte das Training
model.train(
    data="data.yaml",       # Pfad zur data.yaml
    epochs=50,              # Anzahl Trainingsdurchläufe
    imgsz=640,              # Bildgröße
    batch=16,               # Batch-Größe
    name="ball_model_v1",   # Name für den Lauf/Ordner
    project="runs/train",   # Projektordner
    verbose=True,           # Trainingsausgabe anzeigen
)