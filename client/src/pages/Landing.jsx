import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const [userInfo, setUserInfo] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getUserInfo();
  }, []);

  const getUserInfo = async () => {
    try {
      const response = await axios.get(`${import.meta.env.VITE_SERVER_URL}/api/database/get-user-information/`, { withCredentials: true });
      setUserInfo(response.data);
    } catch (error) {
      console.error("Error fetching user information:", error);
    }
  };

  const logout = async () => {
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_SERVER_URL}/api/authenticate/logout/`, {},
        { withCredentials: true }
      );
        if (response.status === 200) {
            navigate("/login");
        }
    } catch (error) {
        console.error("Error logging out:", error);
    }
  }

  return (
    <div>
      <h1>Account: {userInfo?.email}</h1>
      <h3>Below are your API consumption stats</h3>
      <button
        onClick={logout}
        className=" text-white bg-sky-600 hover:bg-sky-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
      >
        Logout
      </button>
    </div>
  );
};

export default Landing;
