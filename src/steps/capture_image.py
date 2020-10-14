from picamera import PiCamera


def capture_image(save_img_to):
  with PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.vflip = True
    camera.capture(str(save_img_to))

