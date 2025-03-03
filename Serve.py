import argparse

from flask import Flask
from flask_restx import Api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

Base = declarative_base()
# 数据库连接配置
db_host = "127.0.0.1"
db_port = "3306"
db_name = "docker"
db_user = "root"
db_pass = "123456"
db_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# 创建引擎
engine = create_engine(db_url, echo=True)

# 创建session对象
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# 定义 app
app = Flask(__name__)
# 注册 restx，路由管理
api = Api(app)
# 注册路由
def register_router():

    from CONTROLLER.plan_controller import plan_ns

    api.add_namespace(plan_ns, "/plan")

if __name__ == "__main__":
    # 注册路由
    register_router()
    # ArgumentParser() 解析命令行参数并生成帮助文档
    parser = argparse.ArgumentParser()
    # ArgumentParser() 解析命令行参数并生成帮助文档
    parser = argparse.ArgumentParser()
    # add_argument() 添加具体的命令行参数和对应的帮助信息
    parser.add_argument("--port", type=int, default=5055, help="服务启动端口")
    # 解析命令行参数并返回一个 Namespace 对象，该对象包含了所有解析出来的参数
    args = parser.parse_args()
    # 启动服务
    app.run(host="0.0.0.0", debug=True, port=args.port)