import tensorflow as tf

model = tf.keras.models.load_model("models/waste_classifier_model.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("models/waste_classifier_model.tflite", "wb") as f:
    f.write(tflite_model)
print("Model converted to TFLite format.")
