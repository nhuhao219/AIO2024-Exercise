from ultralytics import YOLOv10

MODEL_PATH = "yolov10n.pt"
model = YOLOv10(model=MODEL_PATH)
YAML_PATH = "Safety_Helmet_Dataset/data.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 4
model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)
