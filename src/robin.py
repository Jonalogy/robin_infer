import sys
from pathlib import Path
from utils import check_path_exits
from datetime import datetime
from vison import vision, load_and_resize_image
import tflite_runtime.interpreter as tflite
from inference import infer

project_dir = Path(sys.argv[1])
robin_material_weights = project_dir/'models/ROBinV4.2_materials_model.tflite'
robin_shape_weights = project_dir/'models/ROBinV4.2_shapes_model.tflite'
image_size = (224, 224)
material_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
shape_labels = ['booklet', 'bottle', 'cap_lid', 'cardboard', 'clam_shell', 'crushed', 'document', 'drink_can', 'drinkware', 'envelope', 'food_can', 'jug', 'newspaper_tabloid', 'other', 'printed_media', 'trash', 'tub_jar']

img_name=f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg'
new_img_path=project_dir/'images'/img_name
check_path_exits(robin_material_weights)
vision(new_img_path)

print("Resizing Image")
image=load_and_resize_image(new_img_path, image_size)

material_interpreter = tflite.Interpreter(model_path=str(robin_material_weights))
material_interpreter.allocate_tensors()
print("Inferring material...")
material_prediction = infer(
  material_interpreter,
  labels=material_labels,
  image=image
)

# print(f'ROBin suggests {img_name} is made of {material_prediction}')

shape_interpreter = tflite.Interpreter(model_path=str(robin_shape_weights))
shape_interpreter.allocate_tensors()
print("Inferring shape...")
shape_prediction = infer(
  shape_interpreter,
  labels=shape_labels,
  image=image
)

print(f'ROBin suggests {img_name} is a {material_prediction} {shape_prediction}')