from PIL import Image
import numpy as np

def load_and_resize_image(img_path, img_size=(224, 224)):
    img = Image.open(img_path).resize(img_size)
    return np.array(img, np.float32)
