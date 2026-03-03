import os
from PIL import Image
from tqdm import tqdm

# ======================
# PATHS
# ======================
INPUT_DIR = r"D:\Datasets\Phase1_224x224_RGB\test_unseen"

OUTPUT_DIR = r"D:\Datasets\test_unseen_JPEG50compressed"

JPEG_QUALITY = 50
valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".webp")

# ======================
# CREATE OUTPUT STRUCTURE
# ======================
for root, dirs, files in os.walk(INPUT_DIR):
    rel_path = os.path.relpath(root, INPUT_DIR)
    os.makedirs(os.path.join(OUTPUT_DIR, rel_path), exist_ok=True)

# ======================
# COLLECT ALL IMAGES FIRST
# ======================
all_images = []

for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.lower().endswith(valid_ext):
            all_images.append((root, file))

print(f"Total images found: {len(all_images)}")

# ======================
# COMPRESSION LOOP (WITH TQDM)
# ======================
count = 0

for root, file in tqdm(all_images, desc="Compressing images"):

    rel_path = os.path.relpath(root, INPUT_DIR)
    save_root = os.path.join(OUTPUT_DIR, rel_path)

    input_path = os.path.join(root, file)
    output_path = os.path.join(
        save_root,
        os.path.splitext(file)[0] + ".jpg"
    )

    try:
        img = Image.open(input_path).convert("RGB")

        img.save(
            output_path,
            "JPEG",
            quality=JPEG_QUALITY,
            optimize=True
        )

        count += 1

    except Exception as e:
        print("Error:", input_path, e)

print(f"Finished. Compressed {count} images.")