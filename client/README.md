# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh


## Installation

1. Project Setup
```
cd client
npm install
```

2. Environment variables

- Create a `.env` file in the client directory
- Add the following environment variables to the `.env` file:

```sh
VITE_SERVER_URL=  # The url of the server (localhost for now)
```

3. Compile and run the client
```
npm run dev
```