# 🚀 Setup Instructions

Complete guide to set up and run the Hieroglyph Detection project.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- (Optional) CUDA-compatible GPU for faster inference

## 🔧 Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/EngAdhamTamer/hieroglyph-detection.git
cd hieroglyph-detection
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- PIL/Pillow
- NumPy
- And other required packages

### 4. Download Model Weights

Follow instructions in [DOWNLOAD_MODELS.md](DOWNLOAD_MODELS.md)

**Quick version:**
1. Go to [Releases](https://github.com/EngAdhamTamer/hieroglyph-detection/releases)
2. Download `best.pt` from latest release
3. Create folder structure and place the file:
```bash
mkdir -p runs/segment/hieroglyph_seg/weights
# Move best.pt into runs/segment/hieroglyph_seg/weights/
```

### 5. Run the Application
```bash
python gui2.py
```

## 🎯 Quick Test

1. Run the GUI: `python gui2.py`
2. Click "📂 Load Image"
3. Select an image with hieroglyphs
4. View detection results!

## 📊 Training Your Own Model (Optional)

If you want to train from scratch:

### 1. Prepare Dataset

Organize your dataset in YOLO format:
```
dataset/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

### 2. Update Configuration

Edit `dataset/data.yaml` with your dataset paths.

### 3. Run Training
```bash
python train_yolo.py
```

Training will take several hours depending on your hardware.

## 🐛 Troubleshooting

### Issue: "Model not found"
**Solution:** Make sure `best.pt` is in `runs/segment/hieroglyph_seg/weights/best.pt`

### Issue: "CUDA out of memory"
**Solution:** Reduce batch size in `train_yolo.py` or use CPU:
```python
device="cpu"  # instead of device=0
```

### Issue: "ModuleNotFoundError"
**Solution:** Install missing packages:
```bash
pip install -r requirements.txt
```

### Issue: "Permission denied"
**Solution:** Run terminal/command prompt as administrator (Windows) or use `sudo` (Linux/Mac)

## 💡 Tips

- **GPU Acceleration:** Install CUDA-compatible PyTorch for faster inference
- **Large Images:** The model automatically resizes images to 640×640
- **Batch Processing:** Modify `gui2.py` to process multiple images
- **Custom Confidence:** Adjust confidence threshold in the code for more/fewer detections

## 📚 Additional Resources

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 📧 Need Help?

If you encounter issues:
1. Check [Issues](https://github.com/EngAdhamTamer/hieroglyph-detection/issues) for similar problems
2. Create a new issue with details
3. Contact: adhamt864@gmail.com

## ✅ Verification

After setup, verify everything works:
```bash
# Check Python version
python --version  # Should be 3.8+

# Check if packages are installed
python -c "import torch; print(torch.__version__)"
python -c "from ultralytics import YOLO; print('YOLOv8 installed!')"

# Run GUI
python gui2.py
```

---

**Happy Detecting! 🏛️**
