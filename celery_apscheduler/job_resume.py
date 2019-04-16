import datetime

from app import celery1
from celery_apscheduler.task import scheduler


# 恢复任务
def aps_resume(id):
    scheduler.resume_job(id)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '一次性任务,恢复任务')


# 创建恢复
@celery1.task
def resumejob(id):
    # 创建一个一次性的恢复任务
    scheduler.add_job(func=aps_resume, args=(id,),
                      next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=2), id='resume_task',
                      jobstore='redis', replace_existing=True)
