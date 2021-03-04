import schedule
import time

runShed = True

def job():
    print("I'm working...")
    importLive()

def importLive():
    from liveFeedCapture import liveFeedCap

class RunSchedule:

    while runShed:
        schedule.run_pending()

        schedule.every().day.at("14:40").do(job)

        schedule.every().day.at("14:42").do(job)

        # runShed = False
        # exit()


    #
    #     # Arrival Schedule
    #     schedule.every().day.at("13:05").do(liveFeedCap)
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


