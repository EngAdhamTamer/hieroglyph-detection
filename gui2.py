import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from ultralytics import YOLO

# ---------------- CONFIG ----------------
MODEL_PATH = "C:/Users/Compumarts/Desktop/final_cv_project/runs/segment/hieroglyph_seg/weights/best.pt"
IMG_SIZE = 640
# ----------------------------------------

class HieroglyphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hieroglyph Detection & Segmentation")

        # Load model once
        self.model = YOLO(MODEL_PATH)

        # UI Elements
        self.btn_load = tk.Button(root, text="Load Image", command=self.load_image)
        self.btn_load.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.image_path = None

    def load_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.png *.jpeg")]
        )

        if not self.image_path:
            return

        self.run_inference()

    def run_inference(self):
        # Read image
        image = cv2.imread(self.image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Inference
        results = self.model(image, imgsz=IMG_SIZE)[0]

        output = image.copy()

        # Draw masks
        if results.masks is not None:
            masks = results.masks.data.cpu().numpy()
            for mask in masks:
                color = np.array([0, 255, 0], dtype=np.uint8)
                mask = cv2.resize(mask, (output.shape[1], output.shape[0]))
                output[mask > 0.5] = (
                    output[mask > 0.5] * 0.5 + color * 0.5
                )

        # Draw bounding boxes
        if results.boxes is not None:
            for box in results.boxes.xyxy.cpu().numpy():
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(output, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Convert to Tk image
        img = Image.fromarray(output)
        img.thumbnail((800, 800))
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.config(image=self.tk_img)

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = HieroglyphGUI(root)
    root.mainloop()
