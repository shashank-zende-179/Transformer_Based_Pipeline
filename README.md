# 🌙 Low-Light Image Enhancement and Noise Removal for Lunar Mapping

> A **transformer-based pipeline** that combines **LLFormer** and **Restormer** to enhance low-light lunar images captured from Permanently Shadowed Regions (PSRs). The pipeline first enhances image illumination using LLFormer and then removes residual noise using Restormer, producing high-quality images for lunar surface analysis and mapping.

---

# 📖 Overview

Lunar images captured from Permanently Shadowed Regions (PSRs) often suffer from extremely low illumination, poor contrast, and noise, making scientific analysis difficult. This project proposes a **transformer-based pipeline** where **LLFormer** enhances the low-light image and **Restormer** restores the enhanced image by removing residual noise. The final output provides improved visibility, preserved surface details, and enhanced image quality suitable for lunar mapping and exploration.

---

# ✨ Key Features

* Transformer-based image enhancement pipeline
* Low-light enhancement using **LLFormer**
* Image denoising using **Restormer**
* Image normalization and resizing (256 × 256)
* Enhanced lunar surface visualization
* Preservation of structural details and textures
* High-quality output for lunar mapping

---

# 🏗️ System Architecture

The proposed architecture consists of three major components:

### **Input Layer**

* Accepts low-light lunar images.
* Performs image normalization and resizing to **256 × 256**.

### **Processing Core**

* **LLFormer:** Enhances illumination and image contrast.
* **Restormer:** Removes residual noise while preserving image details.

### **User Application Layer**

* Displays or stores the enhanced image for visualization, 3D mapping, AI-based evaluation, and lunar surface analysis.

## 📌 System Architecture Diagram
---
<p align="center"> 
        <img src="assets/architecture.png" alt="System Architecture" width="900"> 
</p>
---

# 🔄 Pipeline

```text
Input Lunar Image
        │
        ▼
Image Preprocessing
(Normalization & Resize to 256 × 256)
        │
        ▼
LLFormer
(Image Enhancement)
        │
        ▼
Enhanced Image
        │
        ▼
Restormer
(Image Denoising)
        │
        ▼
Final Enhanced Image
        │
        ▼
User Application Layer
```

---

# 📊 Results

The proposed pipeline significantly improves image illumination, removes residual noise, and preserves important lunar surface details. The output demonstrates better visibility and image quality compared to the original low-light image.

## 📌 Output Comparison
---

<table>
<tr>
<td align="center"><b>Original Image</b></td>
<td align="center"><b>Final Output</b></td>
</tr>

<tr>
<td>
<img src="assets/results/input.png" width="400">
</td>

<td>
<img src="assets/results/final_output.png" width="400">
</td>
</tr>
</table>

---

# 🎥 Demonstration Video
---
**[Watch Project Demo](videos/demo.mp4)**

---

# 📁 Repository Structure

```text
Transformer_Based_Pipeline/
│
├── assets/
│   ├── architecture.png
│   └── results/
│       ├── input.png
│       └── final_output.png
│
├── configs/
│   ├── __init__.py
│   ├── config.py
│   └── __pycache__/
│
├── data/
│   ├── train/
│   ├── val/
│   ├── test/
│   └── temp
│
├── models/
│   ├── __init__.py
│   ├── LLFormer.py
│   ├── hybrid_model.py
│   ├── restormer/
│   └── __pycache__/
│
├── outputs3/
│
├── scripts/
│   ├── __init__.py
│   ├── train.py
│   ├── test.py
│   ├── inference.py
│   └── __pycache__/
│
├── utils/
│   ├── __init__.py
│   ├── dataloader.py
│   ├── transforms.py
│   ├── loss.py
│   ├── metrics.py
│   └── __pycache__/
│
├── videos/
│   └── demo.mp4
│
└── README.md
```
---

# ⚙️ Execution Steps

Follow the steps below to set up and execute the Transformer-Based Pipeline.

## Step 1: Clone the Repository

```bash
git clone https://github.com/shashank-zende-179/Transformer_Based_Pipeline.git
cd Transformer_Based_Pipeline
```

---

## Step 2: Create a Virtual Environment (Optional but Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Prepare the Dataset

Organize the dataset in the following directory structure:

```text
data/
├── train/
├── val/
└── test/
```

Place the corresponding training, validation, and testing images into their respective folders.

---

## Step 5: Configure the Project

Modify the configuration file according to your requirements.

```text
configs/config.py
```

Configure the following parameters as needed:

- Dataset paths
- Batch size
- Learning rate
- Number of epochs
- Image size
- Model parameters

---

## Step 6: Train the Transformer-Based Pipeline

Run the following command to train the model:

```bash
python scripts/train.py
```

This script performs the following tasks:

- Loads the dataset
- Applies image preprocessing
- Initializes LLFormer and Restormer
- Trains the hybrid transformer-based pipeline
- Saves the trained model checkpoints

---

## Step 7: Evaluate the Model

After training, evaluate the model using:

```bash
python scripts/test.py
```

This script evaluates the trained model on the test dataset and computes the image restoration performance.

---

## Step 8: Run Inference

To enhance a new low-light image, execute:

```bash
python scripts/inference.py
```
---

# 👨‍💻 Author

**Shashank Zende**

Bachelor of Engineering (B.E.) – Computer Science & Engineering

- 📧 Email: shashankzende179@gmail.com

