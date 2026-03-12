# MinorProject6thSem

## Overview

This repository contains the implementation and experimental workflow for our **6th Semester Minor Project**.
The project includes model development, experimentation through Jupyter notebooks, supporting scripts, and the results generated during the experiments.

Phase 1: It contains the baseline experiments where models are trained and evaluated on clean rgb images without compression.

Phase 2: It contains robustness evaluation under distribution shift caused by JPEG compression.

---

# Repository Structure

```
MinorProject6thSem/
├── notebooks/
│   ├── Phase1/
│   │   ├── DMF-Net_mk1/
│   │   │   └── fusionprototype_mk1.ipynb
│   │   ├── EfficientNet-B0/
│   │   │   └── EfficientNet-B0.ipynb
│   │   ├── EfficientNet-B0_ViT-B16_Hybrid/
│   │   │   └── efficientnet_vitb16_hybrid_train.ipynb
│   │   ├── MobileNetV2/
│   │   │   └── MobileNetV2.ipynb
│   │   ├── ResNet18/
│   │   │   └── ResNet18.ipynb
│   │   └── ViT-B16/
│   │       └── ViT-B16.ipynb
│   ├── Phase2/
│   │   ├── DMF-Net/
│   │   │   └── DMF-NET_p2.ipynb
│   │   ├── EfficientNet-B0/
│   │   │   └── EfficientNet-B0_train_phase2.ipynb
│   │   ├── EfficientNet-B0_ViT-B16_Hybrid/
│   │   │   └── EfficientNet-B0_ViT-B16_Hybrid.ipynb
│   │   ├── MobileNetV2/
│   │   │   └── MobileNetV2_p2.ipynb
│   │   ├── ResNet18/
│   │   │   └── ResNet18_p2.ipynb
│   │   └── ViT-B16/
│   │       └── ViT-B16_train_phase2.ipynb
│   └── Robustness testing on jpeg50 compressed(rgb)/
│       └── robustness_teston_compressed_rgb.ipynb
├── results/
│   ├── Phase1/
│   │   ├── DMF-NET_mk1/
│   │   ├── EfficientNet-B0/
│   │   ├── EfficientNet-B0_ViT-B16_Hybrid/
│   │   ├── MobileNetV2/
│   │   ├── ResNet18/
│   │   └── ViT-B16/
│   ├── Phase2/
│   │   ├── DMF-Net/
│   │   ├── EfficientNet-B0/
│   │   ├── EfficientNet-B0_ViT-B16_Hybrid/
│   │   ├── MobileNetV2/
│   │   ├── ResNet18/
│   │   └── ViT-B16/
│   └── Robustness testing on jpeg50 compressed/
├── scripts/
│   ├── compress_rgb_unseen.py
│   └── generate_highpass_dataset.py
├── Details about our custom innovated models.txt
├── GPU distribution.txt
├── Our project workflow.txt
└── README.md
```

---

# Main Code for Experiments

The **core implementation used to generate the results reported in the project** is located in the following directories:

### Experiment Notebooks

All primary experiments and model implementations are located in:

```
notebooks/
```

These notebooks are separated for Phase 1 and Phase 2 and include:

* Data preprocessing
* Model implementation
* Training pipeline
* Evaluation of results
* Visualization of outputs

---

### Supporting Scripts

Additional scripts used for various tasks in the workflow are located in:
```
scripts/
```

These scripts include utilities for dataset preparation

---

### Results

Outputs produced by running the experiments are stored in:

```
results/
```

This folder includes the following for Phase 1 and Phase 2:

* model outputs and evaluation metrics
* generated AUC curve plots

---

# Project Documentation

Additional documentation about the project is provided in the following files:

* **Details about our custom innovated models.txt**
  Description and explanation of the models designed in this project.

* **Our project workflow.txt**
  Step-by-step explanation of the workflow followed during development.

* **GPU distribution.txt**
  Notes on GPU resource allocation used during experiments.

---

# How to Reproduce the Experiments

1. Clone the repository

```
git clone https://github.com/HarshitVerma04/MinorProject6thSem.git
```

2. Navigate to the repository

```
cd MinorProject6thSem
```

3. Open the notebooks

```
notebooks/
```

4. Run the notebooks sequentially to reproduce the experiment pipeline.

---

# Authors

Minor Project 6th Semester: Robust AI-Generated Face Detection Under Compression-Induced Distribution 
Shift Using CNN, Transformer, and Fusion Architectures

Team Members: Arpan Maitra, Harshit Verma, Devanshu Nath




