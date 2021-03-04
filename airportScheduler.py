import schedule
import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


from liveFeedCapture import liveFeedCap

def capture():
    pass

class RunSchedule:

    # Arrival Schedule
    schedule.every().day.at("12:21").do(capture)
    schedule.every().day.at("09:50").do(capture)
    schedule.every().day.at("13:50").do(capture)
    schedule.every().day.at("14:25").do(capture)
    schedule.every().day.at("14:35").do(capture)
    schedule.every().day.at("16:50").do(capture)
    schedule.every().day.at("17:40").do(capture)
    schedule.every().day.at("17:50").do(capture)
    schedule.every().day.at("18:15").do(capture)
    schedule.every().day.at("18:30").do(capture)
    schedule.every().day.at("19:50").do(capture)
    schedule.every().day.at("22:40").do(capture)

while 1:
    schedule.run_pending()
    time.sleep(1)

def capture():
    print("test")
    cls()
    liveFeedCap()