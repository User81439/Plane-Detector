def getStreamID(streamID):
    import json
    import urllib.request

    # URL still works 2 days later..? | https://player.ipcamlive.com/player/getcamerastreamstate.php
    url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?_=1614635705120&token=&alias=5b0f2c342aa3a&targetdomain=canair.captiveye002.com"

    x = urllib.request.urlopen(url)
    raw_data = x.read()
    encoding = x.info().get_content_charset('utf8')  # JSON default
    data = json.loads(raw_data.decode(encoding))
    alias = data["details"]["streamid"]
    return alias


class liveFeedCap:
    # get data from; https://www.canberraairport.com.au/flights/flightcam/

    import cv2
    import m3u8
    from time import time, sleep

    SID = "empty"

    while True:

        baseURL = "https://s8.ipcamlive.com/streams/"
        streamID = getStreamID(SID)
        m3u8URL = "/stream.m3u8"
        fullStreamURL = baseURL + streamID + m3u8URL

        for i in range(3):

            playlist = m3u8.load(fullStreamURL)  # URL with playlist file
            tsFiles = playlist.files  # gets .ts files from playlist
            tsIsolated = "/" + tsFiles[0]  # gets the first .ts file from array
            print(tsFiles, tsIsolated) #debug
            tsURL = baseURL + streamID + tsIsolated  # URL with ts video file

            capture = cv2.VideoCapture(tsURL)  # reads .ts file on URL
            returned_image, image = capture.read()  # captures img | i dont know what 'return_value' does but program breaks without
            # print(returned_image) #debug
            # print(image) #debug
            if not returned_image: #catches error
                print("error grabbing frame")
                break
            cv2.imwrite('planes/plane-not-' + str(i) + '.jpg', image)  # writes image to folder

            capture.release()

            print("image taken!") #debug

            if i < 2: # make 1 less than for loop range to avoid waiting after last image is captured
                sleep(60 - time() % 60)  # waits for 60 seconds

            i += 1

        print("Done!")
        exit()