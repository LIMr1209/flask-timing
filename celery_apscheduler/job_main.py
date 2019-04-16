
from app import celery1
from celery_apscheduler.task import scheduler
from celery_tasks.main_task import main1


@celery1.task
def main(cycle=None, start_time=None, id=None, ):
    if cycle == None or start_time == None or id == None:
        print("参数不正确")
    elif cycle == '0':
        # 是否立即开始
        print("开始执行单次任务")
        #add_job添加方法 注意参数格式
        scheduler.add_job(id=id, func=main1, args=(id,), trigger='date', next_run_time=start_time, jobstore='redis',
                              replace_existing=True)

    elif cycle == '1':
        # 周期性任务
        # trigger='interval'采用循环执行
        # 五秒循环一次
        scheduler.add_job(id=id, func=main1, args=(id,), trigger='interval', seconds=5, jobstore='redis',
                          replace_existing=True, max_instances=1)
