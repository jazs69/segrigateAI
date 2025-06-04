from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sys
import os

model = load_model("models/waste_classifier_model.h5")

img_path = sys.argv[1]
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img) / 255.0
x = np.expand_dims(x, axis=0)

pred = model.predict(x)
classes = [d for d in os.listdir("data/train") if not d.startswith('.')]
print("Predicted:", classes[np.argmax(pred)])
