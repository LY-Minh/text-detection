import os
import shutil
import random

# Paths
images_dir = "dataset/all_images/PNG_Files"
labels_dir = "dataset/all_labels/labels_yolov8_format"

output_base = "dataset"
train_image_dir = os.path.join(output_base, "images/train")
val_image_dir = os.path.join(output_base, "images/val")
train_label_dir = os.path.join(output_base, "labels/train")
val_label_dir = os.path.join(output_base, "labels/val")


# Gather image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(image_files)

# Split
split_index = int(0.8 * len(image_files))
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Helper to copy image and corresponding label
def copy_pair(files, target_image_dir, target_label_dir):
    for file in files:
        img_path = os.path.join(images_dir, file)
        label_file = file.rsplit('.', 1)[0] + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        if not os.path.exists(label_path):
            print(f"Warning: Label not found for {file}, skipping...")
            continue

        shutil.copy2(img_path, os.path.join(target_image_dir, file))
        shutil.copy2(label_path, os.path.join(target_label_dir, label_file))

# Copy files
copy_pair(train_files, train_image_dir, train_label_dir)
copy_pair(val_files, val_image_dir, val_label_dir)

print("✅ Dataset split complete!")
print(f"Training samples: {len(train_files)}")
print(f"Validation samples: {len(val_files)}")
