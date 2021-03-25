import cv2
from time import time
from vision import Vision


class ManualIMGgrab:

    def plane_detector(self):  ## WIP to get planes highlighted.

        # load the trained model
        cascade_plane = cv2.CascadeClassifier('cascade/cascade.xml')  # get plane detector working
        # load an empty Vision class
        vision_limestone = Vision(None)  # what is vision?

        stream_url = self.url_builder()

        vid = cv2.VideoCapture(stream_url)

        while True:

            returned_image, image = vid.read()  # wincap is a Class, we need url feed

            # do object detection
            rectangles = cascade_plane.detectMultiScale(image)

            # draw the detection results onto the original image
            detection_image = vision_limestone.draw_rectangles(image, rectangles)

            # display the images
            cv2.imshow('Matches', detection_image)


        # rectangles = cascade_plane.detectMultiScale(image)  # get plane detector working


            if returned_image:

                cv2.imshow('frame', image)
                rectangles = cascade_plane.detectMultiScale(image)  # get plane detector working

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
                print("in not")
                break

            # else:
            #     running = False

        print("err")

        vid.release()
        cv2.destroyAllWindows()

    def img_capture(self):
        running = True

        stream_url = self.url_builder()

        vid = cv2.VideoCapture(stream_url)

        # cascade_plane = cv2.CascadeClassifier('cascade/cascade.xml')  # get plane detector working
        # rectangles = cascade_plane.detectMultiScale(image)  # get plane detector working

        while running:

            returned_image, image = vid.read()

            if returned_image:

                cv2.imshow('frame', image)
                # rectangles = cascade_plane.detectMultiScale(image)  # get plane detector working

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
                print("in not")
                break

            # else:
            #     running = False

        print("err")

        vid.release()
        cv2.destroyAllWindows()

    def url_builder(self):
        from liveFeedCapture import LiveFeedCapture
        get_SID = LiveFeedCapture()
        stream_id = get_SID.getStreamID()
        base_url = "https://s8.ipcamlive.com/streams/"
        m3u8_url = "/stream.m3u8"
        stream_url = base_url + stream_id + m3u8_url
        return stream_url

