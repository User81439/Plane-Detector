from airportScheduler import AirportSchedulerClass
from liveFeedCapture import LiveFeedCapture
from time import sleep
import utils


# class Main:
#
#     def __init__(self):
#         pass


def main():  # take code out of definition for main?

    ##  the img captureres only seem to crash on internal network, no issues at home..

    # run_capture()

    # manual_img_grabber()

    detection_method = "live"
    # detection_method = "img"
    # detection_method = "ts"

    plane_detector(detection_method)

    ##  be careful when running, only do when needed
    # utils.rename_files()
    # utils.generate_negative_description_file()


def run_capture():
    num_img = 4  # number of images to capture each time the program runs
    wait_between = 90  # amount of time between each image thats taken per run
    # time_str = "empty"  # string to pass into get time
    runner = True
    # stream_id = "empty"
    # alias = "5b0f2c342aa3a"
    # targetdomain = "canair.captiveye002.com"

    canberraAirport = AirportSchedulerClass(["14:39", "11:16", "11:22", "11:14", "11:05", "11:10"])
    liveFeedCap = LiveFeedCapture()

    while True:
        # get time
        # sleep(360)  # enable 5 minute wait
        curr_time = canberraAirport.get_time()
        print(curr_time)

        # compare time
        run_def = canberraAirport.validate_time(curr_time)

        # run program
        if run_def:
            print("Running")
            stream_id = liveFeedCap.getStreamID()
            liveFeedCap.get_images(runner, num_img, wait_between, stream_id)
        else:
            print("not time to run")
            sleep(60)
            continue


def manual_img_grabber():
    from ManualIMGgrab import ManualIMGgrab
    grabber = ManualIMGgrab()
    status = True
    while True:
        status = grabber.img_capture()


def plane_detector(detection_method):
    from ManualIMGgrab import ManualIMGgrab
    detector = ManualIMGgrab()
    detector.plane_detector(detection_method)


if __name__ == '__main__':
    main()
