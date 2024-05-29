import numpy as np
import tensorflow as tf
from picamera2 import Picamera2
from PIL import Image

model = tf.keras.models.load_model(r'sv4a/PAF_99_2.h5', compile=False)

picam = Picamera2()
video_config = picam.create_video_configuration(main={"size": (1640,1232)}, lores={"size":(640,480)},display="lores")
picam.configure(video_config)

picam.start()

try:
    while True:
        image = picam.capture_array()
        #success, image = video.read()
        im = Image.fromarray(image)
        im = im.convert('RGB')
        im = im.resize((224,224))
        #im.save("image.jpg")
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)
        print(predicted_class)

except KeyboardInterrupt:
    im.save("224.png")