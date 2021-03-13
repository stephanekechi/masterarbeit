FROM node:15-alpine as builder
WORKDIR /home/app/client
COPY ./package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:latest
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /home/app/build /usr/share/nginx/html