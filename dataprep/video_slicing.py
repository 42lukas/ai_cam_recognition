import cv2
import random

raw_image_array = []
val_array = []
train_array = []

# Load the video
video_path = "dataprep/data.mp4"
vidcap = cv2.VideoCapture(video_path)
success,image = vidcap.read()

frame_interval = 15
count = 0


while success:
  if count % frame_interval == 0:
    raw_image_array.append(image)      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

# split the data into training and validation sets
random.shuffle(raw_image_array)
split_index = int(len(raw_image_array) * 0.8)
train_array = raw_image_array[:split_index]
val_array = raw_image_array[split_index:]

# 568
for i, image in enumerate(train_array):
  cv2.imwrite(f"./dataset/images/train/train_{i+569:04d}.jpg", image)
  print(f"Saved train image {i}.jpg")

# 145
for i, image in enumerate(val_array):
  cv2.imwrite(f"./dataset/images/val/val_{i+146:04d}.jpg", image)
  print(f"Saved val image {i}.jpg")
