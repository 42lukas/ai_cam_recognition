from ultralytics import YOLO

# Modell nach dem Training laden
run_name = "ball_model_v2"
model_path = f"runs/train/{run_name}/weights/best.pt"
trained_model = YOLO(model_path)

# Auf testbuild anwenden
results = trained_model("dataset/images/val/val_0090.jpg")  # Beispielbild aus Val-Set
results[0].show()

# Ausgabe-Infos
for box in results[0].boxes:
    cls_id = int(box.cls[0])
    print(f"Klasse: {trained_model.names[cls_id]}")
    print(f"Position: {box.xywh[0].tolist()}")