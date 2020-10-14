import os

image_dir=os.getcwd()+'/images'

if not os.path.exists(image_dir):
  print(f'No image directory detected, making directory {image_dir}')
  os.mkdir(image_dir)
