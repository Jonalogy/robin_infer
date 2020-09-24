#!/usr/bin/env bash

if [[ $PATH == `pwd`* ]];
then
  echo "Installing ROBin's dependencies"
  pip install --upgrade pip setuptools -i https://pypi.org/simple
  pip install numpy Pillow picamera -i https://piwheels.org/simple
  pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
  pip list
else
  echo "Please create or activate ROBin's virtual environment"
fi
