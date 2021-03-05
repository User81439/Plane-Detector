##################################
# Live feed read / capture class #
##################################

import cv2
import m3u8
from time import time, sleep
import json
import urllib.request

from Global import Global

class LiveFeedCap:

    print("live feed")

    def liveCapDef(self):

        running = True

        while running:

            SID = "empty"

            # print(fullStreamURL)

            for i in range(3):

                Global.imgCounter += 1

                baseURL = "https://s8.ipcamlive.com/streams/"
                m3u8URL = "/stream.m3u8"
                streamID = LiveFeedCap.getStreamID(SID)
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
                if returned_image:  # catches error
                    cv2.imwrite('planes/plane-not-' + str(Global.imgCounter) + '.jpg', image)  # writes image to folder

                    capture.release()

                # print("img counter: ", imgCounter)

                    print("image taken! ", Global.imgCounter)  # debug

                # if imgCounter < 3:  # make 1 less than for loop range to avoid waiting after last image is captured
                    sleep(15)
                    print("sleep done")

                if not returned_image:
                    i = i - 1
                    Global.imgCounter = Global.imgCounter - 1
                    print("fucked up, retrying")
                    continue

                # print("error grabbing frame")

                # print("i before: ", i)
                # i += 1
                # print("i after: ", i)

            print("Done!")
            running = False


    def getStreamID(streamID):

        url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?_=1614635705120&token=&alias" \
              "=5b0f2c342aa3a&targetdomain=canair.captiveye002.com "

        phpReturn = urllib.request.urlopen(url)
        raw_data = phpReturn.read()
        encoding = phpReturn.info().get_content_charset('utf8')  # JSON default
        data = json.loads(raw_data.decode(encoding))
        alias = data["details"]["streamid"]
        return alias
