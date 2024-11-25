import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

import { MESSAGES } from "../messages";

const Verify = () => {
  const [verificationCode, setVerificationCode] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const verify = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        `${import.meta.env.VITE_SERVER_URL}/api/authenticate/verify/`,
        {
          verification_code: verificationCode,
        },
        { withCredentials: true }
      );
      if (response.status === 200) {
        navigate("/login");
      }
    } catch (error) {
      setErrorMessage(error.response.data.error || "Verification failed.");
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
              <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                {MESSAGES.VERIFY_ACCOUNT}
              </h1>
              <div className="bg-gray-200 bg-opacity-75 text-gray-900 p-3 mb-4 rounded-lg px-5 py-2.5">
                <p className="text-sm">
                  {MESSAGES.CHECK_EMAIL_FOR_VERIFICATION}{" "}
                </p>
              </div>
              {errorMessage && (
                <div className="bg-red-200 bg-opacity-75 text-red-900 p-3 mb-4 rounded-lg px-5 py-2.5">
                  <p className="text-sm">{errorMessage}</p>
                </div>
              )}

              <form
                className="space-y-4 md:space-y-6"
                action="#"
                onSubmit={verify}
              >
                <div>
                  <label
                    htmlFor="verificationCode"
                    className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >
                    {MESSAGES.VERIFICATION_CODE}
                  </label>
                  <input
                    type="text"
                    name="verificationCode"
                    id="verificationCode"
                    className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:border-theme-mantis focus:ring-theme-mantisdark block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder={MESSAGES.ENTER_VERIFICATION_CODE}
                    required
                    value={verificationCode}
                    onChange={(e) => setVerificationCode(e.target.value)}
                  />
                </div>

                <button
                  type="submit"
                  className="w-full text-white bg-sky-500 hover:bg-sky-500/75 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                >
                  {MESSAGES.VERIFY}
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Verify;
