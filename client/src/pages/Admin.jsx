import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserInfo = () => {
  const [userInfo, setUserInfo] = useState(null);

  useEffect(() => {
    const getUserInfo = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_SERVER_URL}/api/database/get-user-information/`, { withCredentials: true });
        setUserInfo(response.data);
      } catch (error) {
        console.error("Error fetching user information:", error);
      }
    };
    
    getUserInfo();
  }, []);

  return (
    <div>
      <h1>Account: {userInfo?.email}</h1>
      <h3>You are viewing as an Admin.</h3>
      <h3>Below are your API consumption stats</h3>
    </div>
  );
};

export default UserInfo;
