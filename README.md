How to Use

Run Main

You may need to install the following;
json
urllib
datetime
time
opencv-contrib-python

media_type | can be 'live' or 'static'

if 'static' you can set the image in the source setter
if live it will capture from the canberra airport livecam

enable_image_capture | True/False
this can only be set when media_type = 'live'
this enable you to capture images from the source via;
  'p' key - captures an image and places in positive/planes folder
  'n' key - captures an image and places in negative/empty  folder
  
enable_demo_mode | True/False
last minute addition, will be removed.
when enabled runs through folder of images and classifies them. used for demonstration purposes if no planes present in live feed.
