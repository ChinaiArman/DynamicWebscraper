import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import StatsTable from "../components/StatsTable";

import { MESSAGES } from "../messages";

const Admin = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [endpointUsage, setEndpointUsage] = useState(null);
  const [userData, setUserData] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getUserInfo();
    getEnpointUsage();
    getAllUsers();
  }, []);

  const getUserInfo = async () => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_SERVER_URL}/api/database/get-user-information/`,
        { withCredentials: true }
      );
      setUserInfo(response.data);
    } catch (error) {
      console.error("Error fetching user information:", error);
    }
  };

  const getEnpointUsage = async () => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_SERVER_URL}/api/database/get-endpoint-usage/`,
        { withCredentials: true }
      );

      const formattedData = response.data.endpoint_usage.map((item) => ({
        Method: item.method,
        Endpoint: item.endpoint,
        Requests: item.count,
      }));

      setEndpointUsage(formattedData);
    } catch (error) {
      console.error("Error fetching endpoint usage", error);
    }
  };

  const getAllUsers = async () => {
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_SERVER_URL}/api/database/get-all-users/`,
        {},
        { withCredentials: true }
      );

      const userData = response.data.users.map((user) => ({
        Email: user.email,
        "API Key": user.api_key,
        Requests: user.num_requests,
      }));

      setUserData(userData);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const logout = async () => {
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_SERVER_URL}/api/authenticate/logout/`,
        {},
        { withCredentials: true }
      );
      if (response.status === 200) {
        navigate("/login");
      }
    } catch (error) {
      console.error("Error logging out:", error);
    }
  };

  return (
    <div className="flex flex-col items-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div className="w-full flex justify-between items-center">
        <div>
          <p>
            {MESSAGES.ACCOUNT} {userInfo?.email}
          </p>
          <p className="text-red-400 text-xs">
            {MESSAGES.ADMIN.VIEWING_AS_ADMIN}
          </p>
        </div>
        <button
          onClick={logout}
          className="text-white bg-gray-600 hover:bg-gray-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
        >
          {MESSAGES.LOGOUT}
        </button>
      </div>
      <br />
      <b>{MESSAGES.ADMIN.API_STATS}</b>
      {endpointUsage && (
        <StatsTable
          columnNames={["Method", "Endpoint", "Requests"]}
          data={endpointUsage}
        />
      )}
      <br />
      <b>{MESSAGES.ADMIN.API_STATS_USER}</b>
      {userData && (
        <StatsTable
          columnNames={["Email", "API Key", "Total Requests"]}
          data={userData}
        />
      )}
    </div>
  );
};

export default Admin;
