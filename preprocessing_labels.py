import os

LABELS_DIRS = [
    r"C:/Users/Compumarts/Desktop/final_cv_project/dataset/train/labels",
    r"C:/Users/Compumarts/Desktop/final_cv_project/dataset/valid/labels",
    r"C:/Users/Compumarts/Desktop/final_cv_project/dataset/test/labels"
]

def convert_to_single_class(labels_dirs):
    for labels_dir in labels_dirs:
        print(f"🔄 Processing: {labels_dir}")

        for root, _, files in os.walk(labels_dir):
            for file in files:
                if not file.endswith(".txt"):
                    continue

                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) < 3:
                        continue

                    # force class id = 0
                    parts[0] = "0"
                    new_lines.append(" ".join(parts))

                with open(file_path, "w") as f:
                    f.write("\n".join(new_lines))

    print("✅ Train / Valid / Test labels converted successfully.")

if __name__ == "__main__":
    convert_to_single_class(LABELS_DIRS)
