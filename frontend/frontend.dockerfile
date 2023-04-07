FROM nginx:stable-alpine

RUN apk add --update npm
RUN npm install typescript@latest -g
COPY app/ /app
WORKDIR /app
RUN npm install
RUN npm run build
RUN mv dist/* /usr/share/nginx/html/
