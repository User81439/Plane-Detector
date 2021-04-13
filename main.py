import utils
from PlaneViewer import PlaneViewer


def main():  # take code out of definition for main?

    # run_capture()
    manual_img_grabber()
    #
    # detection_method = "ts"
    # detection_method = "img"
    # detection_method = "live"
    # plane_detector(detection_method)

    # #  be careful when running, only do when needed
    # utils.rename_files()
    # utils.generate_negative_description_file()


def manual_img_grabber():
    grabber = PlaneViewer()
    status = True
    while True:
        status = grabber.img_capture()


def plane_detector(detection_method):
    detector = PlaneViewer()
    detector.plane_detector(detection_method)


if __name__ == '__main__':
    main()
