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

