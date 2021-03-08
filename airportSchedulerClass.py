#######################################
# Schedule / Timing for image capture #
#######################################

from liveFeedCapture import LiveFeedCap


class AirportSchedulerClass:
    print("airport shed")

    def scheduler(self, current_time):

        # times = ["13:05", "09:50", "13:50", "14:25", "14:35", "16:50", "17:40", "17:50", "18:15", "18:30", "19:50"] #?

        times = ["08:15", "08:17", "08:19", "14:45"]  # set times to run here

        the_time = current_time

        for i in times:
            time_to_test = i

            if the_time == time_to_test:
                print("success @ ", time_to_test)
                AirportSchedulerClass.job(self)
                print("-----------------------------------------------------------------------------------------------")
                continue
            else:  # elif? - want to skip if if is true
                print("fail @ ", time_to_test)

        print("-----------------------------------------------------------------------------------------------")

    def job(self):
        print("working...")
        LiveFeedCap.liveCapDef(self)
