import os


def check_path_exists(path):
    if not os.path.exists(path):
      raise Exception("Path does not exist: " + path)