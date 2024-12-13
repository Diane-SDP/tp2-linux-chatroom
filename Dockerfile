FROM python:3

ENV CHAT_PORT=13337
ENV MAX_USERS=4

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY ./server.py .

ENTRYPOINT [ "python", "./server.py" ]