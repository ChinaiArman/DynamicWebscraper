import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";
import "./App.css";
import { UnverifiedAuthProvider } from './context/UnverifiedAuthContext.jsx';
import { VerifiedAuthProvider } from './context/VerifiedAuthContext.jsx';
import { AdminAuthProvider } from './context/AdminContext.jsx';
import PrivateRoute from './components/PrivateRoute.jsx';
import Login from "./pages/Login";
import Register from "./pages/Register";
import Landing from "./pages/Landing";
import Admin from "./pages/Admin";
import RequestReset from "./pages/RequestReset";
import ResetPassword from "./pages/ResetPassword";
import Verify from "./pages/Verify.jsx";

const App = () => {
  return (
    <UnverifiedAuthProvider>
      <VerifiedAuthProvider>
        <AdminAuthProvider>
          <Router>
            <Routes>
              {/* Public Routes */}
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/request-reset" element={<RequestReset />} />
              <Route path="/reset-password" element={<ResetPassword />} />
              <Route path="/verify" element={<Verify />} />
              
              {/* Private Routes */}
              <Route
                path="/"
                element={<PrivateRoute role="verified"><Landing /></PrivateRoute>}
              />
              <Route
                path="/admin"
                element={<PrivateRoute role="admin"><Admin /></PrivateRoute>}
              />
            </Routes>
          </Router>
        </AdminAuthProvider>
      </VerifiedAuthProvider>
    </UnverifiedAuthProvider>
  )
}

export default App;