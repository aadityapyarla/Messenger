import schedule
import time
import main


def job_1():
    main.good_morning()


schedule.every(10).seconds.do(job_1)

while True:
    schedule.run_pending()
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        pass
