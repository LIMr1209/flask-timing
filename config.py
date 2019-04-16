import redis


from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
#celery 配置信息
class Config():
    # 配置信息具体意思请自行搜索，所需额外配置信息都可以写入该类中
    BROKER_URL = 'redis://localhost:6379'  # 指定中间件 Broker
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # 指定 Backend
    CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC

    # 指定导入的任务模块
    CELERY_IMPORTS = (
        #格式 文件夹.文件
        'celery_apscheduler.job_main',#主任务模块
        'celery_apscheduler.job_pause',#暂停模块
        'celery_apscheduler.job_resume',#恢复模块
        'celery_apscheduler.job_remove',#删除模块
    )

#apscheduler 配置信息
pool = redis.ConnectionPool(host='localhost', port=6379)
jobstores = {
    'redis': RedisJobStore(connection_pool=pool),  # 用redis作backend
}
executors = {
    'default': ThreadPoolExecutor(10),  # 默认线程数
    'processpool': ProcessPoolExecutor(3)  # 默认进程
}