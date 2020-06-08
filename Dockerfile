FROM python:3.7.7-alpine3.11

RUN adduser -D microblog
WORKDIR /home/microblog

COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip && \
    pip install -U -i https://mirrors.aliyun.com/pypi/simple/ pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000

RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]