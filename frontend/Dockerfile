FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

# Command to start the Vite dev server, listening on all interfaces
CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0"]