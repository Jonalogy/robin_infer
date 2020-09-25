from picamera import PiCamera
from PIL import Image
import numpy as np


def vision(save_img_to):
  with PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.vflip = True
    camera.capture(str(save_img_to))

def load_and_resize_image(img_path, img_size=(224, 224)):
    img = Image.open(img_path).resize(img_size)
    return np.array(img, np.float32)
