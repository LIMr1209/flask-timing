import datetime

from app import celery1
from celery_apscheduler.task import scheduler


def aps_pause(id):
    # 暂停的核心方法.pause_job(id)
    scheduler.pause_job(id)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '一次性任务,暂停任务')


# 创建暂停
@celery1.task
def pausejob(id):
    # 创建一个一次性的暂停任务
    scheduler.add_job(func=aps_pause, args=id,
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=2), id='pause_task',
                      jobstore='redis', replace_existing=True)
