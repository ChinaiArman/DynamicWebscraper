import React, { useState } from "react";
import axios from "axios";
import { MESSAGES } from "../messages";

const StatsTable = ({
  columnNames,
  data = [],
  deleteUser,
  showDeleteButton = false,
}) => {
  return (
    <div className="overflow-x-auto shadow-md items-center justify-center mt-2">
      <table className="text-sm text-left text-black dark:text-gray-400 bg-gray-50">
        <thead className="text-xs text-black dark:bg-gray-700 dark:text-gray-400 text-center uppercase">
          <tr>
            {columnNames.map((col, index) => (
              <th key={index} className="px-6 py-3 border-b border-gray-500">
                {col}
              </th>
            ))}
            {showDeleteButton && (
              <th className="px-6 py-3 border-b border-gray-500">
                {MESSAGES.ADMIN.ACTIONS}
              </th>
            )}
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr
              key={index}
              className="border-b border-gray-500 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-600 text-center"
            >
              {columnNames.map((col, colIndex) => (
                <td key={colIndex} className="px-6 py-4">
                  {row[col] || "N/A"}
                </td>
              ))}
              {showDeleteButton && (
                <td className="px-6 py-4">
                  <button
                    onClick={() => deleteUser(row.userId)}
                    className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700"
                  >
                    {MESSAGES.ADMIN.DELETE}
                  </button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StatsTable;
