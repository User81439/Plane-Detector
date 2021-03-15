from airportSchedulerClass import AirportSchedulerClass
from liveFeedCapture import LiveFeedCapture
from time import sleep

#######################################################
# Find out how to build OpenCV Annotations with CMake #
#######################################################

class Main:

    def __init__(self):
        pass


def main():  # take code out of definition for main?
    time_getter = AirportSchedulerClass.get_time
    # time_checker = AirportSchedulerClass.schedule_times  # runs on scheduled times
    time_checker = AirportSchedulerClass.schedule_instant  # instantly runs
    def_runner = LiveFeedCapture.get_images

    num_img = 4  # number of images to capture each time the program runs
    wait_between = 90  # amount of time between each image thats taken per run
    time_str = "empty"  # string to pass into get time

    while True:
        # get time
        sleep(360)
        curr_time = time_getter(time_str)
        print(curr_time)

        # compare time
        run_def = time_checker(curr_time)

        # run program
        if run_def:
            print("Running")
            def_runner(True, num_img, wait_between)
        else:
            print("not time to run")
            sleep(60)
            continue


if __name__ == '__main__':
    main()
