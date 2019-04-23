from app import celery1
from task import scheduler
import time


def main1(id):
    print("当前时间：", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("我是task1方法1", "id:" + id)


@celery1.task
def addjob(id):
    scheduler.add_job(id=id, func=main1, args=(id,), trigger='interval', seconds=5,
                      replace_existing=True, max_instances=1, jobstore='redis')


# 创建删除
@celery1.task
def removejob(id):
    scheduler.remove_job(id)


# 创建暂停
@celery1.task
def pausejob(id):
    scheduler.pause_job(id)


# 创建恢复
@celery1.task
def resumejob(id):
    scheduler.resume_job(id)
