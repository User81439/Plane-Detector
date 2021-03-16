#######################################
# Schedule / Timing for image capture #
#######################################

from datetime import datetime


class AirportSchedulerClass:
    print("airport shed")

    def __init__(self, listOfTimes):
        self.times = listOfTimes

    def get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        # print("Current Time =", current_time)
        return current_time

    # def schedule_instant(self):
    #     current_time = datetime.now()
    #     return current_time

    def validate_time(self, curr_time):
        if curr_time in self.times:
            return True
        else:
            return False

    def validate_time_instant(self, curr_time):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if curr_time == current_time:
            return True
        else:
            return False

    # def schedule_times(self, time):
    #
    #     # times =   # set times to run here
    #     the_time = time
    #
    #     for i in self.times:
    #         time_to_test = i
    #
    #         if the_time == time_to_test:
    #             return True
    #         else:
    #             continue
