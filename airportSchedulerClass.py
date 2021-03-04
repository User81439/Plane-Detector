#######################################
# Schedule / Timing for image capture #
#######################################

from liveFeedCapture import LiveFeedCap
from time import time, sleep
import datetime
import schedule


class AirportSchedulerClass:

    print("airport shed")

    def scheduler(self, current_time):

        # times = ["13:05", "09:50", "13:50", "14:25", "14:35", "16:50", "17:40", "17:50", "18:15", "18:30", "19:50"] #?

        times = ["10:28", "10:30", "10:33", "10:36", "10:39"]

        the_time = current_time

        for i in times:
            time_to_test = i

            if the_time == time_to_test:
                print("success @ ", time_to_test)
                AirportSchedulerClass.job(self)
                print("-----------------------------------------------------------------------------------------------")
                continue
            else:
                print("fail @ ", time_to_test)
                print("-----------------------------------------------------------------------------------------------")


















    # def setFalse(state):
    #     state = False

    # def getTime(self):
    #     now = datetime.now()
    #     current_time = now.strftime("%H:%M")
    #     print("Current Time =", current_time)

    def runSchedule(self):
        while True:
            schedule.run_pending()
            print("waiting for job")
            schedule.every().day.at("08:20").do(AirportSchedulerClass.job(self))

            schedule.run_pending()
            print("waiting for job")
            schedule.every().day.at("08:21").do(AirportSchedulerClass.job(self))

            # self.setFalse(state)
            # exit()

    def job(self):
        print("working...")
        LiveFeedCap.liveCapDef(self)
        #
        #     # Arrival Schedule
        #     # schedule.every().day.at("13:05").do(liveFeedCap)
        #     # schedule.every().day.at("09:50").do(liveFeedCap)
        #     # schedule.every().day.at("13:50").do(liveFeedCap)
        #     # schedule.every().day.at("14:25").do(liveFeedCap)
        #     # schedule.every().day.at("14:35").do(liveFeedCap)
        #     # schedule.every().day.at("16:50").do(liveFeedCap)
        #     # schedule.every().day.at("17:40").do(liveFeedCap)
        #     # schedule.every().day.at("17:50").do(liveFeedCap)
        #     # schedule.every().day.at("18:15").do(liveFeedCap)
        #     # schedule.every().day.at("18:30").do(liveFeedCap)
        #     # schedule.every().day.at("19:50").do(liveFeedCap)
        #     # schedule.every().day.at("22:40").do(liveFeedCap)
