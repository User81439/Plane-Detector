import cv2
from time import time, sleep
from liveFeedCapture import LiveFeedCapture


class ManualIMGgrab:

    def plane_detector(self, detection_method, use_classifer=False, enable_keyboard=False):  ## WIP to get planes highlighted.
        running = True
        source_input = detection_method

        # load the trained model
        cascade_plane = cv2.CascadeClassifier('cascade2/cascade.xml')  # get plane detector working

        lc = LiveFeedCapture()
        stream_url = lc.get_stream_url()

        if source_input == "live":
            vid = cv2.VideoCapture(stream_url)

        elif source_input == "img":
            vid = cv2.VideoCapture('Images/planes_sorted/plane_10.jpg')

        elif source_input == "ts":
            pass
        else:
            raise Exception("Bad source input")

        while running:
            print("starting")

            if source_input == "ts":
                ts_url = lc.get_ts_file(stream_url)
                vid = cv2.VideoCapture(ts_url)

            returned_image, image = vid.read()

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
                    cv2.destroyAllWindows()
                    running = False
                    print("in not")
                    break

                print("running again?")
                # running = False

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
                    break
                elif key == ord('p'):
                    cv2.imwrite('Images/planes/{}.jpg'.format(loop_time), image)
                    print("Plane Image Taken")

                elif key == ord('n'):
                    cv2.imwrite('Images/not/{}.jpg'.format(loop_time), image)
                    print("Empty Image Taken")

            if not returned_image:

                vid.release()
                cv2.destroyAllWindows()
                running = False
                print("in not")
                break

            print("running again?")
            running = True

        vid.release()
        cv2.destroyAllWindows()

        return running


    def draw_rectangles(self, image, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv2.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv2.rectangle(image, top_left, bottom_right, line_color, lineType=line_type)

        return image
