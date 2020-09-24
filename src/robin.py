import sys
from pathlib import Path
from utils import check_path_exits
from datetime import datetime
from vison import vision, load_and_resize_image
import tflite_runtime.interpreter as tflite
from inference import infer

project_dir = Path(sys.argv[1])
robin_material = project_dir/'models/ROBinV4.2_materials_model.tflite'
image_size = (224, 224)
material_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

img_name=f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg'
new_img_path=project_dir/'images'/img_name
check_path_exits(robin_material)
vision(new_img_path)

interpreter = tflite.Interpreter(model_path=str(robin_material))
interpreter.allocate_tensors()
prediction = infer(
  interpreter,
  labels=material_labels,
  image=load_and_resize_image(new_img_path, image_size)
)

print(f'ROBin suggests {img_name} is made of {prediction}')
