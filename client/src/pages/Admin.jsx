import React, { useState, useEffect } from "react";
import axios from "axios";
import StatsTable from "../components/StatsTable";

const Admin = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [endpointUsage, setEndpointUsage] = useState(null);

  useEffect(() => {
    const getUserInfo = async () => {
      try {
        const response = await axios.get(
          `${
            import.meta.env.VITE_SERVER_URL
          }/api/database/get-user-information/`,
          { withCredentials: true }
        );
        setUserInfo(response.data);
      } catch (error) {
        console.error("Error fetching user information:", error);
      }
    };

    getUserInfo();
    getEnpointUsage();
  }, []);

  const getEnpointUsage = async () => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_SERVER_URL}/api/database/get-endpoint-usage/`,
        { withCredentials: true }
      );
      console.log(response.data);

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

  return (
    <div className="flex flex-col items-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div>
        <p>Account: {userInfo?.email}</p>
        <p className="text-red-400 text-xs">You are viewing as an Admin.</p>
      </div>
      <br></br>
      <b>API Usage Stats</b>
      {endpointUsage && (
        <StatsTable
          columnNames={["Method", "Endpoint", "Requests"]}
          data={endpointUsage}
        />
      )}
      <br></br>
      <b>API Usage for each user</b>
    </div>
  );
};

export default Admin;
