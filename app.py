from config import Config
from flask import Flask, request, jsonify
from celery import Celery

# celery与flask实例化并配置
flask_app = Flask(__name__)
flask_app.config.from_object(Config)
celery1 = Celery(flask_app.name)
celery1.conf.update(flask_app.config)


# 举例的视图函数 模拟前台用户输入的数据
# 该视图暂时只简单实现功能具体根据项目要求完成
@flask_app.route('/task/add')
def test1():
    id = request.args.get('id')
    from job_main import addjob
    addjob.apply_async((id,))
    return jsonify({'success': True})


@flask_app.route('/task/remove')
def test2():
    id = request.args.get('id')
    from job_main import removejob
    removejob.apply_async((id,))
    return jsonify({'success': True})


# 模拟主页面
@flask_app.route('/')
def main1():
    return jsonify({'success': True})


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
