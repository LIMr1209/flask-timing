import time

from celery_tasks.main_task import celery2

@celery2.task
def t1(id):
    print("当前时间：", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("我是task1方法1","id:"+id)
