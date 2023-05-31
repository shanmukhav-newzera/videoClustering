from transformers import AutoImageProcessor, TimesformerForVideoClassification
import numpy as np
import torch

import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

import skvideo.io  
videodata = skvideo.io.vread("/Users/Shanmukha/Desktop/services/videoClustering/kapil1.mp4")  
print(videodata.shape, type(videodata))

# video = list(np.random.randn(8, 3, 224, 224).astype(np.uint8))
video = list(np.array(videodata).astype(np.uint8))

processor = AutoImageProcessor.from_pretrained("facebook/timesformer-base-finetuned-k400")
model = TimesformerForVideoClassification.from_pretrained("facebook/timesformer-base-finetuned-k400")

inputs = processor( video, return_tensors="pt")

with torch.no_grad():
  outputs = model(**inputs)
  logits = outputs.logits

predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])