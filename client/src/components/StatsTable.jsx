import React, { useState } from "react";
import axios from "axios";

const StatsTable = ({ columnNames, data=[] }) => {
  return (

    <div className="overflow-x-auto shadow-md items-center justify-center">
    <table className="text-sm text-left text-black dark:text-gray-400">
      <thead className="text-xs text-black dark:bg-gray-700 dark:text-gray-400 text-center">
        <tr>
          {columnNames.map((col, index) => (
            <th key={index} className="px-6 py-3 border-b border-gray-500">
              {col}
            </th>
          ))}
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
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  );
};

export default StatsTable;
