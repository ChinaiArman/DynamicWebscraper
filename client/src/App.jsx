import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes, createBrowserRouter } from 'react-router-dom'
import { RouterProvider } from 'react-router-dom'
import './App.css'

import Login from './pages/Login'
import Register from './pages/Register'

const router = createBrowserRouter([
  {
    path: "/",
    loader: () => window.location.href = '/login'
  }, 
  {
    path: "/login",
    element: <Login />,
  }, 
  {
    path: "/register",
    element: <Register />,
  }
])

function App() {

  return (
    <div className="App flex flex-col h-screen">
      <RouterProvider router={router} />
    </div>
  )
}

export default App;
