import os


def check_path_exits(path):
    if not os.path.exists(path):
      raise Exception("Path does not exist: " + path)