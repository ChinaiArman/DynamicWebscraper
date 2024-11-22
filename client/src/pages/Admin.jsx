import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import StatsTable from "../components/StatsTable";

const Admin = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [endpointUsage, setEndpointUsage] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getUserInfo();
    getEnpointUsage();
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
    <div className="flex flex-col items-center px-6 py-8 mx-auto md:h-screen lg:py-0">
    <div className="w-full flex justify-between items-center">
      <div>
        <p>Account: {userInfo?.email}</p>
        <p className="text-red-400 text-xs">You are viewing as an Admin.</p>
      </div>
      <button
        onClick={logout}
        className="text-white bg-gray-600 hover:bg-gray-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
      >
        Logout
      </button>
    </div>
    <br />
    <b>API Usage Stats</b>
    {endpointUsage && (
      <StatsTable
        columnNames={["Method", "Endpoint", "Requests"]}
        data={endpointUsage}
      />
    )}
    <br />
    <b>API Usage for each user</b>
  </div>
  );
};

export default Admin;
