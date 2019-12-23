FROM node:12.13-alpine

LABEL version="1.0" maintainer="colinchang<zhangcheng5468@gmail.com>"

RUN apk add python3

COPY src /app
WORKDIR /app
ENV input=input output=output

ENTRYPOINT python3 app.py ${input} ${output}