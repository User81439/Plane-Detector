from airportSchedulerClass import AirportSchedulerClass
from liveFeedCapture import LiveFeedCapture
from time import sleep


class Main:

    def __init__(self):
        pass


def main():
    time_getter = AirportSchedulerClass.get_time
    time_checker = AirportSchedulerClass.scheduler_timed  # remove _timed to run on actual schedule, just runs everytime
    def_runner = LiveFeedCapture.get_images

    num_img = 4  # number of images to capture each time the program runs
    wait_between = 90  # amount of time between each image thats taken per run
    time_str = "empty"  # string to pass into get time

    while True:
        # get time
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
