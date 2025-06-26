from ultralytics import YOLO


# 1. Lade vortrainiertes YOLOv8n-Modell
# wenn man basierend auf das alte modell das neue erstellen möchte, muss man einfach nur den pfad des alten modells angeben
# bsp: model = YOLO("runs/train/ball_model_v4/weights/best.pt")
model = YOLO("yolov8m.pt")

# 2. Starte das Training
model.train(
    data="data.yaml",
    epochs=75,
    imgsz=640,
    batch=16,
    name="Model_v6m",
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
    hsv_v=0.4,
    device="cuda:0" # hier wird GPU verwendet
)