
# Project: https://gitlab.com/ablebadger/plane

from liveFeedCapture import liveFeedCap

# def runLiveFeed():
#     liveFeedCap()

# import cv2
# import m3u8
# from time import time, sleep
# # import numpy as np
#
import json
import requests
import urllib.request
url = "https://player.ipcamlive.com/player/getcamerastreamstate.php?_=1614635705120&token=&alias=5b0f2c342aa3a&targetdomain=canair.captiveye002.com"
x = urllib.request.urlopen(url)
raw_data = x.read()
encoding = x.info().get_content_charset('utf8')  # JSON default
print(raw_data)   #this is data in string format
data = json.loads(raw_data.decode(encoding))
print(data)   #this would be your json data

