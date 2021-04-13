##################################
# Live feed read / capture class #
##################################

import json
from urllib import request, error


class LiveFeedCapture:

    def __init__(self):
        self.base_url = "https://s8.ipcamlive.com/streams/"
        self.stream_id = "empty"
        self.set_stream_id()

    def set_stream_id(self):

        url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?alias=5b0f2c342aa3a&targetdomain=canair.captiveye002.com"
        try:
            phpReturn = request.urlopen(url)
        except error.URLError as exception:
            print("No Internet Connection (probably..)")
            exit(1)
        else:
            raw_data = phpReturn.read()
            encoding = phpReturn.info().get_content_charset('utf8')  # JSON default
            data = json.loads(raw_data.decode(encoding))
            stream_id = data["details"]["streamid"]
            self.stream_id = stream_id

    def get_stream_url(self):
        stream_url = self.base_url + self.stream_id + "/stream.m3u8"
        return stream_url
