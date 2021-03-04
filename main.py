from self import self
from airportSchedulerClass import AirportSchedulerClass
from testing import Testing
from time import time, sleep

from datetime import datetime


# def runLiveFeed():
#     liveFeedCap()

class Main:

    def main(self):
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print("Current Time =", current_time)

            AirportSchedulerClass.scheduler(self, current_time)

            sleep(60)

        # print("in main")
        # AirportSchedulerClass.runSchedule(self)

    if __name__ == '__main__':
        main(self)
