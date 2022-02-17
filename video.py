import cv2
from matplotlib import pyplot as plt


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_frame_with_box(self, x1, y1, x2, y2):
        success, image = self.video.read()

        image_rect = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        ret, image_rect = cv2.imencode('.jpg', image_rect)

        return image_rect.tobytes()
