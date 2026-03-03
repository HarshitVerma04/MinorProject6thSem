# ==========================================
# High-Pass Residual Dataset Generator
# ==========================================

import os
import cv2
import numpy as np
from tqdm import tqdm

# ==========================================
# PATH CONFIGURATION (VERIFY THESE)
# ==========================================

PHASE1_ROOT = r"D:\Datasets\Phase1_224x224_RGB"
PHASE2_ROOT = r"D:\Datasets\Phase2_224x224_HighPass"

# ==========================================
# HIGH-PASS FUNCTION
# ==========================================

def generate_highpass(image, kernel_size=5):
    """
    image: RGB numpy array (H, W, 3)
    kernel_size: Gaussian blur size (must be odd)
    """
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    highpass = cv2.subtract(image, blurred)
    return highpass


# ==========================================
# CREATE MIRRORED DATASET STRUCTURE
# ==========================================

splits = ["train", "val", "test_seen", "test_unseen"]
classes = ["fake", "real"]

print("\n Starting High-Pass Dataset Generation...")

for split in splits:
    for cls in classes:

        input_dir = os.path.join(PHASE1_ROOT, split, cls)
        output_dir = os.path.join(PHASE2_ROOT, split, cls)

        os.makedirs(output_dir, exist_ok=True)

        print(f"\nProcessing: {split}/{cls}")

        for filename in tqdm(os.listdir(input_dir)):

            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Read image (BGR)
            img = cv2.imread(input_path)

            if img is None:
                print(f"Warning: Skipping unreadable file {filename}")
                continue

            # Convert BGR -> RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Generate high-pass residual
            hp_img = generate_highpass(img, kernel_size=5)

            # Convert RGB -> BGR before saving
            hp_img = cv2.cvtColor(hp_img, cv2.COLOR_RGB2BGR)

            # Save as PNG (lossless)
            cv2.imwrite(output_path, hp_img)

print("\n High-pass dataset generation complete.")