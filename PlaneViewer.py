import cv2
from time import time, sleep


class PlaneViewer:
    def __init__(self, source):
        self.source = source

    def plane_detector(self, enable_img_capture):
        running = True

        cascade_plane = cv2.CascadeClassifier('cascade3/cascade.xml')  # loads plane detector model

        vid = cv2.VideoCapture(self.source)


        # if source_input == "live":
        #     vid = cv2.VideoCapture(source)
        #
        # elif source_input == "static":
        #     # vid = cv2.VideoCapture('Images/planes3_sorted/plane3_0.jpg')
        #     vid = cv2.VideoCapture(source)

        # else:
        #     raise Exception("Bad source input")

        while running:
            # print("starting")

            returned_image, image = vid.read()
            # print("read vid t or f: ", returned_image)

            if returned_image:

                # do object detection
                rectangles = cascade_plane.detectMultiScale(image)

                # draw the detection results onto the original image
                detection_image = self.draw_rectangles(image, rectangles)

                # display the images
                cv2.imshow('Matches', detection_image)

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    print("quitting")
                    running = False
                    break



            if not returned_image:
                vid.release()
                vid = cv2.VideoCapture(stream_url)
                # print("in not")

            # print("running again?")
            if source_input == "img":
                sleep(25)

        vid.release()
        cv2.destroyAllWindows()

    def img_capture(self):
        running = True
        lc = LiveFeedCapture()

        stream_url = lc.get_stream_url()

        vid = cv2.VideoCapture(stream_url)

        while running:
            print("starting")
            returned_image, image = vid.read()

            if returned_image:

                cv2.imshow('frame', image)

                loop_time = time()

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    print("quitting")
                    running = False
                    break
                elif key == ord('p'):
                    cv2.imwrite('Images/planes4/{}.jpg'.format(loop_time), image)
                    print("Plane Image Taken")

                elif key == ord('n'):
                    cv2.imwrite('Images/not/{}.jpg'.format(loop_time), image)
                    print("Empty Image Taken")

            if not returned_image:
                vid.release()
                vid = cv2.VideoCapture(stream_url)
                print("in not")

            print("running again?")

        vid.release()
        cv2.destroyAllWindows()

        return running

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
