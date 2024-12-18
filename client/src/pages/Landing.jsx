import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import { MESSAGES } from "../messages";

const Landing = () => {
  const [userInfo, setUserInfo] = useState(null);
  const [warning, setWarning] = useState("");
  const [url, setUrl] = useState("");
  const [prompt, setPrompt] = useState("");
  const [results, setResults] = useState([]); // New state for storing results
  const [loading, setLoading] = useState(false);
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
    // set loading state to true
    setLoading(true);
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_SERVER_URL}/api/service/query`,
        {
          params: {
            url,
            prompt,
          },
          headers: {
            Authorization: `Bearer ${userInfo.api_key}`,
          },
        }
      );
      setResults(response.data.result); // Set the results from API response
      // if response.data.warning is not empty, set the warning state
      if (response.data.warning) {
        setWarning(response.data.warning);
      }
    } catch (error) {
      console.error("Error querying the service:", error);
    } finally {
      // set loading state to false
      setLoading(false);
      // incremenet the num_requests in userInfo state
      setUserInfo((prev) => ({ ...prev, num_requests: prev.num_requests + 1 }));
    }
  };

  return (
    <div className="px-6 py-8 w-full md:w-3/4 lg:w-2/3 mx-auto">
      <div className="w-full flex justify-between items-center mb-2 md:w-3/4 lg:w-2/3 mx-auto">
        <p>
          {MESSAGES.ACCOUNT} {userInfo?.email}
        </p>
        <button
          onClick={logout}
          className=" text-white bg-gray-600 hover:bg-gray-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
        >
          {MESSAGES.LOGOUT}
        </button>
      </div>
      <div className="mt-4 mb-6">
        <p>
          {MESSAGES.API_KEY} {userInfo?.api_key}
        </p>
      </div>
      {userInfo && (
        <div className="flex items-center justify-center">
          <b className="mr-1">{MESSAGES.USER.API_STATS}</b>
          <p>{userInfo.num_requests}</p>
        </div>
      )}
      <div className="bg-gray-100 rounded-lg p-6 shadow-md mb-6 w-full md:w-3/4 lg:w-2/3 mx-auto">
        <p className="mb-4">{MESSAGES.USER.ENTER_URL_PROMPT}</p>
        <div className="mb-4">
          <input
            type="url"
            placeholder={MESSAGES.USER.ENTER_URL}
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="border-2 border-gray-300 rounded-md px-4 py-2 text-sm focus:outline-none focus:ring-2 w-full"
          />
        </div>
        <div className="mb-4">
          <textarea
            placeholder={MESSAGES.USER.ENTER_PROMPT}
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            className="border-2 border-gray-300 rounded-md px-4 py-2 text-sm focus:outline-none focus:ring-2 w-full"
          />
        </div>
        <button
          onClick={handleUrlSubmit}
          className="text-white bg-sky-600 hover:bg-sky-600/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 w-full sm:w-auto"
        >
          {MESSAGES.USER.ENTER}
        </button>
      </div>
      {loading && <p>{MESSAGES.USER.LOADING}</p>}
      {/* Results Section */}
      {warning && (
        <div className="bg-red-200 bg-opacity-75 text-red-900 p-3 mb-4 rounded-lg px-5 py-2.5">
          <p className="text-sm">{warning}</p>
        </div>
      )}
      {results.length > 0 && (
        <div className="bg-white rounded-lg p-6 shadow-md w-full md:w-3/4 lg:w-2/3 mx-auto">
          <h2 className="text-lg font-bold mb-4">{MESSAGES.USER.RESULTS}</h2>
          <ul>
            {results.map((item, index) => (
              <li key={index} className="mb-2">
                <p>
                  <strong>Answer:</strong> {item.answer || "No answer"}
                </p>
                <p>
                  <strong>Score:</strong> {item.score.toFixed(2)}
                </p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Landing;
