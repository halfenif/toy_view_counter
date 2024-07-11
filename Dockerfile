FROM python:3.12-slim

# Init Package
RUN apt update

#Timezone
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN apt-get install -y tzdata

RUN mkdir /app
RUN mkdir /app/data

COPY app/requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 9050

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9050"]