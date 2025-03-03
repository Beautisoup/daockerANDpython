# 使用 Python 3.9 轻量级镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量，提高 pip 安装速度
ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目依赖文件
COPY requirements.txt .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 暴露端口
EXPOSE 6666

# 启动应用
CMD ["python", "Serve.py"]