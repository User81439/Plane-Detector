#######################################
# Schedule / Timing for image capture #
#######################################

from liveFeedCapture import LiveFeedCap


def job():
    print("working...")
    LiveFeedCap.liveCapDef()


class AirportSchedulerClass:
    # print("airport shed")

    def __init__(self):
        pass

    def scheduler(self):

        times = ["10:40", "10:45", "10:55", "11:00", "11:05", "11:10"]  # set times to run here

        the_time = self

        for i in times:
            time_to_test = i

            if the_time == time_to_test:
                print("success @ ", time_to_test)
                job()
                print("-----------------------------------------------------------------------------------------------")
                continue
            else:
                print("fail @ ", time_to_test)

        print("-----------------------------------------------------------------------------------------------")
