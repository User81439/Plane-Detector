##################################
# Live feed read / capture class #
##################################

import cv2
import m3u8
from time import sleep, time
import json
import urllib.request


class LiveFeedCapture:

    def __init__(self, ):
        pass

    def get_images(self, runner, images, wait, SID):

        running = runner
        num_img = images
        wait_between = wait
        stream_id = SID
        # loop_time = time()

        while running:

            # print(fullStreamURL)

            for i in range(num_img):

                loop_time = time()

                base_url = "https://s8.ipcamlive.com/streams/"
                m3u8_url = "/stream.m3u8"
                full_stream_url = base_url + stream_id + m3u8_url

                playlist = m3u8.load(full_stream_url)  # URL with playlist file
                tsFiles = playlist.files  # gets .ts files from playlist
                tsIsolated = "/" + tsFiles[4]  # gets the first .ts file from array
                tsURL = base_url + stream_id + tsIsolated  # URL with ts video file

                capture = cv2.VideoCapture(tsURL)  # reads .ts file on URL

                returned_image, image = capture.read()  # captures img | i dont know what 'return_value' does but program breaks without
                # print(returned_image) #debug
                # print(image) #debug
                if returned_image:  # catches error
                    cv2.imwrite('planes/{}.jpg'.format(loop_time), image)

                    capture.release()

                    sleep(wait_between)
                    print("sleep done")

                if not returned_image:
                    i = i - 1
                    print("retrying")
                    continue

            print("Done!")
            running = False

    def getStreamID(self):

        url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?alias=5b0f2c342aa3a&targetdomain=canair.captiveye002.com"

        phpReturn = urllib.request.urlopen(url)
        raw_data = phpReturn.read()
        encoding = phpReturn.info().get_content_charset('utf8')  # JSON default
        data = json.loads(raw_data.decode(encoding))
        stream_id = data["details"]["streamid"]
        if stream_id != "None":  # all untested error checking
            return stream_id
        else:
            pass
