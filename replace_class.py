import os

label_dir = "dataset/labels/train/" # or "dataset/labels/val/"

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(label_dir, filename)
        
        with open(filepath, "r") as file:
            lines = file.readlines()
        
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                parts[0] = "0"  # set class to 0 (ball)
                new_lines.append(" ".join(parts) + "\n")
        
        with open(filepath, "w") as file:
            file.writelines(new_lines)