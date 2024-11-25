import { useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  createBrowserRouter,
} from "react-router-dom";
import { RouterProvider } from "react-router-dom";
import "./App.css";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Landing from "./pages/Landing";
import Admin from "./pages/Admin";
import RequestReset from "./pages/RequestReset";
import ResetPassword from "./pages/ResetPassword";

const router = createBrowserRouter([
  {
    path: "/",
    loader: () => (window.location.href = "/login"),
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },
  {
    path: "/request-reset",
    element: <RequestReset />,
  },
  {
    path: "/reset-password",
    element: <ResetPassword />,
  },
  {
    path: "/landing",
    element: <Landing />,
  },
  {
    path: "/admin",
    element: <Admin />,
  },
]);

function App() {
  return (
    <div className="App flex flex-col h-screen">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
