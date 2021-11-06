FROM node:16-buster

RUN install -d -m 0700 /app
COPY . /app

WORKDIR /app

RUN npm install -g npm
RUN npm install

CMD [ "npm", "run", "dev" ]
