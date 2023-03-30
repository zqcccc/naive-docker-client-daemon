FROM python:3.11-slim-buster
COPY ./src /app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
EXPOSE 1080
CMD ["/bin/sh", "/app/startup.sh"]