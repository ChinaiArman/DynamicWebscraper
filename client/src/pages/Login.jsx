import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

import { MESSAGES } from "../messages";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  let loginUser = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_SERVER_URL}/api/authenticate/login/`,
        {
          email: email,
          password: password,
        },
        { withCredentials: true }
      );
      if (response.status === 200) {
        const userInfoResponse = await axios.get(
          `${
            import.meta.env.VITE_SERVER_URL
          }/api/database/get-user-information/`,
          { withCredentials: true }
        );
        const isAdmin = userInfoResponse.data.is_admin;
        if (isAdmin) {
          navigate("/admin");
        } else {
          navigate("/landing");
        }
      }
    } catch (error) {
      setErrorMessage(error.response.data.error || "Login failed.");
    }
  };

  return (
    <>
      <section className="bg-gray-50 dark:bg-gray-900 blurred-background">
        <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
          <a
            href="#"
            className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
          ></a>
          <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h2 className="text-l font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                {MESSAGES.LOGIN_TITLE}
              </h2>
              {errorMessage && (
                <div className="bg-red-200 bg-opacity-75 text-red-900 p-3 mb-4 rounded-lg px-5 py-2.5">
                  <p className="text-sm">{errorMessage}</p>
                </div>
              )}

              <form
                className="space-y-4 md:space-y-6"
                action="#"
                onSubmit={loginUser}
              >
                <div>
                  <label
                    htmlFor="email"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    {MESSAGES.EMAIL}
                  </label>
                  <input
                    type="text"
                    name="email"
                    id="email"
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:border-theme-mantis focus:ring-theme-mantisdark block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder={MESSAGES.ENTER_EMAIL}
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                <div>
                  <label
                    htmlFor="password"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    {MESSAGES.PASSWORD}
                  </label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder={MESSAGES.ENTER_PASSWORD}
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:border-theme-mantis focus:ring-theme-mantisdark block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
                <button
                  type="submit"
                  className="w-full text-white bg-sky-500 hover:bg-sky-500/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                >
                  {MESSAGES.LOGIN}
                </button>
                <p className="text-sm font-light text-gray-600 dark:text-gray-400">
                  {MESSAGES.DONT_HAVE_ACCOUNT}{" "}
                  <a
                    href="/register"
                    className="font-medium text-sky-500 hover:underline dark:text-primary-500"
                  >
                    {MESSAGES.REGISTER_HERE}
                  </a>
                </p>
              </form>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Login;
