from ultralytics import YOLO


# 1. Lade vortrainiertes YOLOv8n-Modell
model = YOLO("yolov8n.pt")

# 2. Starte das Training
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="ball_model_v3",
    project="runs/train",
    verbose=True,
    visualize=True,
    workers=0,
    seed=42,
    degrees=10,       # max. Rotation in Grad
    translate=0.1,    # max. Verschiebung
    scale=0.5,        # Zoom-Faktor
    shear=2.0,        # Scherung
    perspective=0.0005,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4
)