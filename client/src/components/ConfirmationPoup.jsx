import React from "react";
import { MESSAGES } from "../messages";

// Some of this code in this page was created with the assistance of previous project as well as copilot.

const ConfirmationPopup = ({ message, onCancel, onConfirm }) => {
  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-sm">
        <h3 className="text-lg font-semibold text-center mb-4">{message}</h3>
        <div className="flex justify-around">
          <button
            onClick={onCancel}
            className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-700"
          >
            {MESSAGES.CANCEL}
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700"
          >
            {MESSAGES.CONFIRM}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ConfirmationPopup;
