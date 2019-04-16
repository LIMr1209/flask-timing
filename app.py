from config import Config
from flask import Flask, render_template, request
from celery import Celery

# celery与flask实例化并配置
flask_app = Flask(__name__)
flask_app.config.from_object(Config)
celery1 = Celery(flask_app.name)
celery1.conf.update(flask_app.config)


# 举例的视图函数 模拟前台用户输入的数据
# 该视图暂时只简单实现功能具体根据项目要求完成
@flask_app.route('/1', methods=["POST", "GET"])
def test1():
    # 暂定接收用户输入的信息
    if request.values.get('input1'):
        #任务执行
        cycle = request.values.get('input1')
        #任务开始时间
        start_time = request.values.get('input2')
        #任务id
        id = request.values.get('input3')

        # 调用定时函数mian() ，调用结果该项目未写

        from celery_apscheduler.job_main import main
        # 注意由celery装饰的函数调用要用如下方式，具体含义自行搜索，传入参数需为元组类型
        main.apply_async((cycle, start_time,id))

    from celery_apscheduler import job_pause, job_remove, job_resume
    # 调用暂停功能
    if request.values.get('input4') == '0':
        id = request.values.get('input3')
        job_pause.pausejob.apply_async((id,))
    # 调用恢复功能
    if request.values.get('input5') == '1':
        id = request.values.get('input3')
        job_resume.resumejob.apply_async((id,))
    # 调用删除功能
    if request.values.get('input6') == '2':
        id = request.values.get('input3')
        job_remove.removejob.apply_async((id,))

    if request.method == 'GET':
        return render_template("test.html")


# 模拟主页面
@flask_app.route('/')
def main1():
    return render_template("test.html")


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=5000,debug=True)
