import utils
from PlaneViewer import PlaneViewer
from liveFeedCapture import LiveFeedCapture


def main():  # take code out of definition for main?

    # media_type = "static"
    media_type = "live"
    enable_img_capture = False

    if media_type == "live":
        lc = LiveFeedCapture()
        source = lc.get_stream_url()

    elif media_type == "static":
        source = 'Images/planes3_sorted/plane3_0.jpg'

    else:
        raise Exception("dun did somn wrong")

    pv = PlaneViewer(source)
    pv.plane_detector(enable_img_capture)

    # #  be careful when running, only do when needed
    # utils.rename_files()
    # utils.generate_negative_description_file()

#
# def plane_detector():
#     detector = PlaneViewer()
#     detector.plane_detector()


if __name__ == '__main__':
    main()
