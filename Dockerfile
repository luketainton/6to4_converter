FROM python:3.14-slim
LABEL maintainer="Luke Tainton <luke@tainton.uk>"
LABEL org.opencontainers.image.source="https://github.com/luketainton/6to4_converter"
USER root

ENV PYTHONPATH="/run:/usr/local/lib/python3.14/lib-dynload:/usr/local/lib/python3.14/site-packages:/usr/local/lib/python3.14"
WORKDIR /run

RUN mkdir -p /.local && \
    chmod -R 777 /.local && \
    pip install -U pip

COPY requirements.txt /run/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "-B", "-m", "app.main"]

COPY app /run/app
