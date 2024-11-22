import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [url, setUrl] = useState("");
  const [prompt, setPrompt] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    getUserInfo();
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

  const handleUrlSubmit = async () => {
    // api required
    // try {
    //   const response = await axios.get(`${import.meta.env.VITE_SERVER_URL}/api/qna/qna/query`, {
    //     url: url,
    //     prompt: prompt
    //   }, { withCredentials: true });
    //   console.log(response);
    // } catch (error) {
    //   console.error("Error:", error)
    // }
    console.log(url, prompt);
  };

  return (
    <div className="px-6 py-8 w-full md:w-3/4 lg:w-2/3 mx-auto">
      <div className="w-full flex justify-between items-center mb-2 md:w-3/4 lg:w-2/3 mx-auto">
        <p>Account: {userInfo?.email}</p>
        <button
          onClick={logout}
          className=" text-white bg-gray-600 hover:bg-gray-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
        >
          Logout
        </button>
      </div>
      <div className="bg-gray-100 rounded-lg p-6 shadow-md mb-6 w-full md:w-3/4 lg:w-2/3 mx-auto">
        <p className="mb-4">
          Enter a URL and Prompt to use the Dynamic Webscraper!
        </p>
        <div className="mb-4">
          <input
            type="url"
            placeholder="Enter a URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="border-2 border-gray-300 rounded-md px-4 py-2 text-sm focus:outline-none focus:ring-2 w-full"
          />
        </div>
        <div className="mb-4">
          <textarea
            placeholder="Enter a prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="border-2 border-gray-300 rounded-md px-4 py-2 text-sm focus:outline-none focus:ring-2 w-full"
          />
        </div>
        <button
          onClick={handleUrlSubmit}
          className="text-white bg-sky-600 hover:bg-sky-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 w-full sm:w-auto"
        >
          Enter
        </button>
      </div>

      <h3>Below are your API consumption stats</h3>
    </div>
  );
};

export default Landing;
