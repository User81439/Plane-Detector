from airportSchedulerClass import AirportSchedulerClass
from time import sleep

from datetime import datetime


def test_time():

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)

        AirportSchedulerClass.scheduler(current_time)

        print("1 minute rest")
        sleep(60)


def main():
    test_time()


class Main:

    def __init__(self):
        pass

    if __name__ != '__main__':
        pass
    else:
        main()
