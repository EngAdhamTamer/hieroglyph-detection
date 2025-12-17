from ultralytics import YOLO
import os

   if __name__ == "__main__":
       # Load segmentation model
       model = YOLO("yolov8n-seg.pt")
       
       # Get the base directory
       BASE_DIR = os.path.dirname(os.path.abspath(__file__))
       DATA_PATH = os.path.join(BASE_DIR, "dataset", "data.yaml")

       model.train(
           data=DATA_PATH,
           task="segment",
           epochs=80,
           imgsz=640,
           batch=8,
           device=0,        # GPU | "cpu"
           workers=4,
           project="runs/segment",
           name="hieroglyph_seg",
           save=True
       )
