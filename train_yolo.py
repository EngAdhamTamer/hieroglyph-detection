from ultralytics import YOLO

if __name__ == "__main__":
    # Load segmentation model
    model = YOLO("yolov8n-seg.pt")

    model.train(
        data="C:/Users/Compumarts/Desktop/final_cv_project/dataset/data.yaml",
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
