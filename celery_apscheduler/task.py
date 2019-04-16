

# 异步执行调用函数

from apscheduler.schedulers.background import BackgroundScheduler
from config import jobstores,executors
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors)
scheduler.daemonic=False
scheduler.start()


