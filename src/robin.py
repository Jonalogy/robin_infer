import sys
import os
from pathlib import Path
from datetime import datetime
from src.utils import check_path_exists
from src.steps import capture_image, load_and_resize_image, classify
import tflite_runtime.interpreter as tflite

project_dir=Path(os.getcwd())
robin_material_weights = project_dir/'models/ROBinV4.2_materials_model.tflite'
robin_shape_weights = project_dir/'models/ROBinV4.2_shapes_model.tflite'
image_size = (224, 224)
material_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
shape_labels = ['booklet', 'bottle', 'cap_lid', 'cardboard', 'clam_shell', 'crushed', 'document', 'drink_can', 'drinkware', 'envelope', 'food_can', 'jug', 'newspaper_tabloid', 'other', 'printed_media', 'trash', 'tub_jar']

def infer():
  img_name=f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg'
  new_img_path=project_dir/'images'/img_name
  check_path_exists(robin_material_weights)
  capture_image(new_img_path)

  print("Resizing Image")
  image=load_and_resize_image(new_img_path, image_size)

  material_interpreter = tflite.Interpreter(model_path=str(robin_material_weights))
  material_interpreter.allocate_tensors()
  print("Inferring material...")
  material_prediction = classify(
    material_interpreter,
    material_labels,
    image
  )

  shape_interpreter = tflite.Interpreter(model_path=str(robin_shape_weights))
  shape_interpreter.allocate_tensors()
  print("Inferring shape...")
  shape_prediction = classify(
    shape_interpreter,
    shape_labels,
    image
  )

  print(f'ROBin suggests {img_name} is a {material_prediction} {shape_prediction}')