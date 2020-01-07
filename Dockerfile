FROM node:12.13-alpine

LABEL version="1.0" maintainer="colinchang<zhangcheng5468@gmail.com>"

COPY src /app
WORKDIR /app
ENV input=input output=output

RUN npm install && apk add python3
ENTRYPOINT python3 app.py ${input} ${output}