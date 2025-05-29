
FROM node:lts-alpine AS build-stage
ENV NODE_OPTIONS=--openssl-legacy-provider
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN yarn build

FROM nginx:stable-alpine

# Копируем собранные файлы Vue.js
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Открываем порты 80
EXPOSE 80 

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]

