FROM python:3.11.14

# 2. 在容器内设置一个工作目录
WORKDIR /app

# 3. 将我们本地的依赖文件复制到容器的工作目录中
# (我们只复制 requirements.txt，而不是整个项目，这样可以利用 Docker 的缓存)
COPY requirements.txt .

# 4. 在容器内安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 5. 将项目中的所有文件 (model.py, test_model.py 等) 复制到容器的 /app 目录
COPY . .

# 6. 设置容器启动时要运行的默认命令
# 在这里，我们让它自动运行 pytest
CMD ["pytest"]