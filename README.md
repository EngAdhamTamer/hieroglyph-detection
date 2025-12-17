# 🏛️ Ancient Egyptian Hieroglyph Detection & Segmentation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)](https://opencv.org/)

An AI-powered computer vision system for detecting and segmenting ancient Egyptian hieroglyphs from archaeological images using YOLOv8 instance segmentation.


## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Future Work](#future-work)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This project implements a deep learning solution for automatically detecting and segmenting individual hieroglyphs from images of ancient Egyptian inscriptions, temple walls, and artifacts. The system uses YOLOv8's instance segmentation architecture to identify hieroglyphs with pixel-level precision.

### Key Highlights
- **235,436 hieroglyph instances** in training dataset
- **70.9% mAP@0.5** on validation set
- **Real-time inference** with user-friendly GUI
- **Advanced preprocessing** pipeline for archaeological images

## ✨ Features

- **Instance Segmentation**: Precise pixel-level masks for each hieroglyph
- **Multi-scale Detection**: Works on hieroglyphs of varying sizes
- **Preprocessing Pipeline**: 
  - CLAHE contrast enhancement
  - Non-local means denoising
  - Image normalization and resizing
- **Interactive GUI**: Tkinter-based interface for easy inference
- **Visualization**: Confidence scores and bounding boxes overlay

## 📊 Model Performance

### Metrics (Validation Set)

| Metric | Score |
|--------|-------|
| **mAP@0.5** | 70.9% |
| **mAP@0.5:0.95** | 42.5% |
| **Precision** | 100% @ conf=1.0 |
| **Recall** | 62% @ conf=0.0 |
| **F1-Score** | 75% @ conf=0.398 |

### Training Configuration
- **Model**: YOLOv8n-seg (nano variant)
- **Epochs**: 25
- **Batch Size**: 8
- **Image Size**: 640×640
- **Optimizer**: SGD (lr=0.01)
- **Device**: CUDA (GPU accelerated)

### Performance Curves

![F1 Curve](results/F1_curve.png)<img width="2250" height="1500" alt="BoxF1_curve" src="https://github.com/user-attachments/assets/06958d87-5d45-49eb-a734-6c7c8bc21e75" />

![Precision-Recall Curve](results/PR_curve.png)<img width="2250" height="1500" alt="MaskF1_curve" src="https://github.com/user-attachments/assets/ba1b3217-6c56-44ba-8eb0-c9840f75296b" />



### Confusion Matrix

![Confusion Matrix](results/confusion_matrix.png)<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/a91e3a56-c55b-486c-afc3-127d1de2c2bf" />


### Training Metrics

![Training Loss](results/results.png)<img width="3600" height="1200" alt="results" src="https://github.com/user-attachments/assets/5b70c653-c726-444a-83b4-0881bfc6582c" />


## 📁 Dataset

The dataset consists of annotated images from various Egyptian archaeological sites including:
- Temple wall inscriptions
- Obelisk carvings
- Papyrus documents
- Stone tablets and stelae

**Dataset Statistics:**
- Total Instances: 235,436 hieroglyphs
- Train/Val/Test Split: Standard YOLO format
- Annotation Format: YOLO segmentation (polygon coordinates)
- Single Class: "hieroglyph" (unified approach)

## 🚀 Installation

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (recommended)
- 8GB+ RAM

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/EngAdhamTamer/hieroglyph-detection.git
cd hieroglyph-detection
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download pre-trained weights**
```bash
# Download from releases
# Place best.pt in runs/segment/hieroglyph_seg/weights/
```

See [DOWNLOAD_MODELS.md](DOWNLOAD_MODELS.md) for detailed instructions.

## 💻 Usage

### GUI Application

Run the interactive GUI for easy image inference:

```bash
python gui2.py
```

**Steps:**
1. Click "Load Image"
2. Select an image with hieroglyphs
3. View detection results with masks and bounding boxes

### Training from Scratch

```bash
python train_yolo.py
```

Modify `train_yolo.py` to adjust:
- Number of epochs
- Batch size
- Learning rate
- Data augmentation parameters

### Data Preprocessing

Preprocess your dataset before training:

```bash
python preprocessing.py
```

This applies:
- Resizing to 640×640
- CLAHE contrast enhancement
- Denoising
- Normalization

### Label Conversion

Convert multi-class labels to single class:

```bash
python preprocessing_labels.py
```

## 📂 Project Structure

```
hieroglyph-detection/
├── dataset/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   └── data.yaml
├── runs/
│   └── segment/
│       └── hieroglyph_seg/
│           ├── weights/
│           │   └── best.pt
│           └── results/
├── preprocessing.py
├── preprocessing_labels.py
├── train_yolo.py
├── gui2.py
├── requirements.txt
├── args.yaml
└── README.md
```

## 🎨 Results

### Visual Examples

The model successfully detects and segments hieroglyphs across various conditions:

**Sample Predictions**

![Validation Predictions](results/val_batch0_pred.jpg)![val_batch1_pred](https://github.com/user-attachments/assets/e17c74ae-8e93-4511-bd5d-39cec31c0b28)


**Detection Examples**

![Detection 1](results/val_batch1_pred.jpg)![val_batch2_labels](https://github.com/user-attachments/assets/76253b6b-b1c6-4884-ae7b-f670e6b9a502)![Uploading val_batch2_labels.jpg…]()


![Detection 2](results/val_batch2_pred.jpg)![val_batch2_pred](https://github.com/user-attachments/assets/0c1b17d3-7f5a-4106-9a99-e89a123207af)


### Confusion Matrix Analysis
- True Positives: 59,608 hieroglyphs correctly detected
- False Positives: 1,532 (2.5% error rate)
- Strong background discrimination

## 🔮 Future Work

- [ ] Multi-class classification (different hieroglyph types)
- [ ] Hieroglyph recognition and translation
- [ ] Mobile app deployment
- [ ] Sequence analysis for reading order
- [ ] Integration with archaeological databases
- [ ] 3D surface reconstruction support
- [ ] Real-time video processing

## 👥 Contributors

This project was developed as a university Computer Vision course project by:

- **Adham Tamer** - [LinkedIn](https://www.linkedin.com/in/adhamtamer/) | [GitHub](https://github.com/EngAdhamTamer)
- **Ahmed Sherif** - [LinkedIn](https://www.linkedin.com/in/ahmed-sherif06/)
- **Ahmed Ramadan** - [LinkedIn](https://www.linkedin.com/in/ahmed-ramadan240/)
- **Saif Mohamed** - [LinkedIn](https://www.linkedin.com/in/saif-mohamed-1002a5274/)
- **Muhab Mohamed** - [LinkedIn](https://www.linkedin.com/in/muhab-mohamed-abdelraouf-209814302/)
- **Mohamed Korayem** - [LinkedIn](https://www.linkedin.com/in/mohamed-korayem-b44b5331b/)
- **Nasser Aly** - [LinkedIn](https://www.linkedin.com/in/naser-ali-naser-b78457320/)
- **Ahmed Yahia** - [LinkedIn](https://www.linkedin.com/in/ahmed-yahia-016a0b288/)
- **Mazen Ashraf**
- **Mohamed El-Saeed**

## 🙏 Acknowledgments

- **Ultralytics** for the YOLOv8 framework
- **Computer Vision Course** instructors and teaching assistants
- Egyptian archaeology community for domain expertise
- Open-source computer vision community

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Adham Tamer**
- Email: adhamt864@gmail.com
- LinkedIn: [linkedin.com/in/adhamtamer](https://www.linkedin.com/in/adhamtamer/)
- GitHub: [@EngAdhamTamer](https://github.com/EngAdhamTamer)
- Project Link: [https://github.com/EngAdhamTamer/hieroglyph-detection](https://github.com/EngAdhamTamer/hieroglyph-detection)

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Built with ❤️ for preserving ancient Egyptian heritage through AI**
