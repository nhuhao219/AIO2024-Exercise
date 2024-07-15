from ultralytics import YOLOv10

TRAINDE_MODEL_PATH = "runs/detect/train11/weights/best.pt"
model = YOLOv10(model=TRAINDE_MODEL_PATH)
YAML_PATH = "Safety_Helmet_Dataset/data.yaml"
IMG_SIZE = 640

model.val(data=YAML_PATH,
          imgsz=IMG_SIZE,
          split="test")
