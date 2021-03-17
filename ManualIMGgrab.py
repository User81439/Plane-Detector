import cv2
from time import time


class ManualIMGgrab:

    def img_capture(self):

        stream_url = self.url_builder()

        vid = cv2.VideoCapture(stream_url)

        loop_time = time()

        while True:

            returned_image, image = vid.read()

            if returned_image:
                cv2.imshow('frame', image)

                # print('FPS {}'.format(1 / (time() - loop_time)))
                loop_time = time()

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                elif key == ord('p'):
                    cv2.imwrite('Images/planes/{}.jpg'.format(loop_time), image)
                    print("Plane Image Taken")

                elif key == ord('n'):
                    cv2.imwrite('Images/not/{}.jpg'.format(loop_time), image)
                    print("Empty Image Taken")
            else:
                continue  # might need to be pass? idk, program somtimes crashes due to .ts from .m3u8 not being avaliable for window

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
