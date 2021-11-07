FROM node:16-buster

RUN npm install -g npm

RUN install -d -m 0700 -o node -g node  /app

USER node
WORKDIR /app

RUN npm install

CMD [ "npm", "run", "dev" ]
