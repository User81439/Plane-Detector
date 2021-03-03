def getStreamID(streamID):
    import json
    import urllib.request
    # URL still works 2 days later..?
    url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?_=1614635705120&token=&alias=5b0f2c342aa3a&targetdomain=canair.captiveye002.com"
    x = urllib.request.urlopen(url)
    raw_data = x.read()
    encoding = x.info().get_content_charset('utf8')  # JSON default
    data = json.loads(raw_data.decode(encoding))
    alias = data["details"]["streamid"]
    print(alias)
    return alias


class liveFeedCap:
    # get data from; https://www.canberraairport.com.au/flights/flightcam/
    #                https://canair.captiveye002.com/stream_scaling/public/stream.asp

    # m3u8 TS URL:  https://s8.ipcamlive.com/streams/08dftlcyxesvwdrh9/stream.m3u8
    #               https://s8.ipcamlive.com/streams/08emxkrvfjq0sgmea/stream.m3u8
    #               https://s8.ipcamlive.com/streams/08emxkrvfjq0sgmea/

    import cv2
    import m3u8
    from time import time, sleep

    while True:

        for i in range(3):
            # need to get stream ID from
            # https://canair.captiveye002.com/stream_scaling/public/stream.asp
            # https://player.ipcamlive.com/player/getcamerastreamstate.php
            # https://s8.ipcamlive.com/streams/08emxkrvfjq0sgmea/stream.m3u8

            baseURL = "https://s8.ipcamlive.com/streams/"
            # streamID = "08tb3u8xo5hycahvn"  # need to get this from getcamerastate URL
            SID = "empty"
            streamID = getStreamID(SID)
            m3u8URL = "/stream.m3u8"

            fullStreamURL = baseURL + streamID + m3u8URL
            print(fullStreamURL)

            # playlist = m3u8.load("https://s8.ipcamlive.com/streams/08emxkrvfjq0sgmea/stream.m3u8") # URL with playlist file
            playlist = m3u8.load(fullStreamURL)  # URL with playlist file
            tsFiles = playlist.files  # gets .ts files from playlist
            tsIsolated = "/" + tsFiles[0]  # gets the first .ts file from array

            # tsURL = "https://s8.ipcamlive.com/streams/08emxkrvfjq0sgmea/" + tsIsolated # URL with ts video file
            tsURL = baseURL + streamID + tsIsolated  # URL with ts video file

            capture = cv2.VideoCapture(tsURL)  # reads .ts file on URL
            return_value, image = capture.read()  # captures img | i dont know what 'return_value' does but program breaks without
            cv2.imwrite('planes/opencv' + str(i) + '.jpg', image)  # writes image to folder

            sleep(10 - time() % 10)  # waits for 10 seconds, make 60 & 60 for 1 min etc.

        exit()
