##################################
# Live feed read / capture class #
##################################

import cv2
import m3u8
from time import time, sleep
import json
import urllib.request


class LiveFeedCap:

    print("live feed")

    def liveCapDef(self):

        running = True
        imgCounter = 0

        while running:

            SID = "empty"

            # print(fullStreamURL)

            for i in range(3):

                imgCounter += 1

                baseURL = "https://s8.ipcamlive.com/streams/"
                streamID = LiveFeedCap.getStreamID(SID)
                m3u8URL = "/stream.m3u8"
                fullStreamURL = baseURL + streamID + m3u8URL

                playlist = m3u8.load(fullStreamURL)  # URL with playlist file
                tsFiles = playlist.files  # gets .ts files from playlist
                tsIsolated = "/" + tsFiles[4]  # gets the first .ts file from array
                # print(tsFiles, tsIsolated)  # debug
                tsURL = baseURL + streamID + tsIsolated  # URL with ts video file

                capture = cv2.VideoCapture(tsURL)  # reads .ts file on URL

                returned_image, image = capture.read()  # captures img | i dont know what 'return_value' does but program breaks without
                # print(returned_image) #debug
                # print(image) #debug
                # if not returned_image:  # catches error
                #     print("error grabbing frame")
                    # i = imgCounter
                    # pass
                cv2.imwrite('planes/plane-not-' + str(imgCounter) + '.jpg', image)  # writes image to folder

                capture.release()

                # print("img counter: ", imgCounter)

                # print("image taken!")  # debug

                # if imgCounter < 3:  # make 1 less than for loop range to avoid waiting after last image is captured
                sleep(15)

                # print("i before: ", i)
                # i += 1
                # print("i after: ", i)

            print("Done!")
            running = False


    def getStreamID(streamID):

        # URL still works 2 days later..? | https://player.ipcamlive.com/player/getcamerastreamstate.php
        url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?_=1614635705120&token=&alias" \
              "=5b0f2c342aa3a&targetdomain=canair.captiveye002.com "

        x = urllib.request.urlopen(url)
        raw_data = x.read()
        encoding = x.info().get_content_charset('utf8')  # JSON default
        data = json.loads(raw_data.decode(encoding))
        alias = data["details"]["streamid"]
        return alias
