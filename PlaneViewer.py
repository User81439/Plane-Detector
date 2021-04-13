########################################
# Plane Viewer / Capturer / Rectangler #
########################################

import cv2
from time import time


class PlaneViewer:
    def __init__(self, source):
        self.source = source

    def plane_detector(self, enable_img_capture):
        running = True

        if not enable_img_capture:
            cascade_plane = cv2.CascadeClassifier('cascade3/cascade.xml')  # loads plane detector model

        vid = cv2.VideoCapture(self.source)

        while running:
            returned_image, image = vid.read()

            if returned_image:

                if not enable_img_capture:
                    # do object detection
                    rectangles = cascade_plane.detectMultiScale(image)
                    # draw the detection results onto the original image
                    image = self.draw_rectangles(image, rectangles)

                # display the images
                cv2.imshow('Matches', image)

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    print("quitting")
                    running = False
                    break

                if enable_img_capture:
                    loop_time = time()

                    if key == ord('p'):
                        cv2.imwrite('Images/planes4/{}.jpg'.format(loop_time), image)
                        print("Plane Image Taken")

                    elif key == ord('n'):
                        cv2.imwrite('Images/not/{}.jpg'.format(loop_time), image)
                        print("Empty Image Taken")

            if not returned_image:
                vid.release()
                vid = cv2.VideoCapture(self.source)

        vid.release()
        cv2.destroyAllWindows()

    def draw_rectangles(self, image, rectangles):
        # these colors are actually BGR
        # line_color = (231, 0, 155)
        line_color = (0, 255, 0)
        line_type = cv2.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv2.rectangle(image, top_left, bottom_right, line_color, lineType=line_type)

        return image
