#######################################
# Schedule / Timing for image capture #
#######################################

from datetime import datetime


class AirportSchedulerClass:
    print("airport shed")

    def __init__(self):
        pass

    @staticmethod # get rid of if cant loop, just to appease error
    def get_time(current_time):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        # print("Current Time =", current_time)
        return current_time

    @staticmethod # get rid of if cant loop, just to appease error
    def schedule_instant(current_time):
        current_time = datetime.now()
        return current_time

    def schedule_times(self):

        times = ["11:15", "11:16", "11:22", "11:14", "11:05", "11:10"]  # set times to run here
        the_time = self

        for i in times:
            time_to_test = i

            if the_time == time_to_test:
                return True
            else:
                continue
