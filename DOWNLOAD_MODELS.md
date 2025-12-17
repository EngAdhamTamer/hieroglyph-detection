# 📦 Model Weights Download

The trained model weights are too large to store directly in the repository.

## 🚀 Quick Download

### Option 1: GitHub Release (Recommended)

1. Go to [**Releases**](https://github.com/EngAdhamTamer/hieroglyph-detection/releases)
2. Download `best.pt` from the latest release (v1.0.0)
3. Place the file in your project directory

### Where to Place the Model

After downloading, create this folder structure:
```
hieroglyph-detection/
├── runs/
│   └── segment/
│       └── hieroglyph_seg/
│           └── weights/
│               └── best.pt  ← Place downloaded model here
```

Or simply create the folders and place `best.pt` there:
```bash
mkdir -p runs/segment/hieroglyph_seg/weights
# Move best.pt into runs/segment/hieroglyph_seg/weights/
```

## 🎯 Quick Start After Download
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the GUI application
python gui2.py

# 3. Click "Load Image" and select a hieroglyph image
```

## 📊 Model Information

- **Architecture:** YOLOv8n-seg (nano variant)
- **Task:** Instance Segmentation
- **Input Size:** 640×640 pixels
- **File Size:** ~6 MB
- **Format:** PyTorch (.pt)

### Performance Metrics

| Metric | Value |
|--------|-------|
| mAP@0.5 | 70.9% |
| mAP@0.5:0.95 | 42.5% |
| Precision | 100% @ conf=1.0 |
| Recall | 62% @ conf=0.0 |
| F1-Score | 75% @ conf=0.398 |

## 🔄 Alternative: Train Your Own Model

If you want to train the model from scratch:
```bash
# 1. Prepare your dataset in YOLO format
# 2. Update dataset/data.yaml with your paths
# 3. Run training
python train_yolo.py
```

Training will create the model weights in the same location.

## ❓ Troubleshooting

**Model not loading?**
- Check that `best.pt` is in the correct folder path
- Verify file is not corrupted (re-download if needed)
- Check file permissions

**GPU not detected?**
- The model will automatically use CPU if GPU is unavailable
- Install CUDA-compatible PyTorch for GPU support

**Import errors?**
- Make sure all requirements are installed: `pip install -r requirements.txt`
- Try creating a fresh virtual environment

## 📧 Need Help?

Contact: adhamt864@gmail.com
