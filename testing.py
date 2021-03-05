#################
# Testing Class #
#################

from time import time, sleep


class Testing:

    def shed_test(self, current_time):
        # print("got into test")

        # times = ["13:05", "09:50", "13:50", "14:25", "14:35", "16:50", "17:40", "17:50", "18:15", "18:30", "19:50"]

        times = ["10:16", "10:17", "10:18", "10:19", "10:20"]

        the_time = current_time

        for i in times:
            time_to_test = i

            if the_time == time_to_test:
                print("success @ ", time_to_test)
            else:
                print("fail @ ", time_to_test)

