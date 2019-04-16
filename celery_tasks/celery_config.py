from kombu import Queue
from kombu import Exchange

# result_serializer = 'json'
BROKER_URL = 'redis://localhost:6379/1'  # 指定中间件 Broker
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'  # 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_tasks.task1',
   'celery_tasks.task2',
    #'celery_tasks.task3',
    # 'celery_tasks.task4',
)

#配置任务队列分布
#该项目暂未用到
CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('priority_high', exchange=Exchange('priority_high'), routing_key='priority_high'),
    Queue('priority_low', exchange=Exchange('priority_low'), routing_key='priority_low'),
)

CELERY_ROUTES = {
    'celery_tasks.task1.t1': {'queue': 'priority_high', 'routing_key': 'priority_high'},
    'celery_tasks.task2.t2': {'queue': 'priority_low', 'routing_key': 'priority_low'},
}