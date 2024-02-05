import React from "react";

export function CircularXButton({ id, setData }: any) {
  const buttonStyle = {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: "50px", // Adjust the size as needed
    height: "50px", // Ensure width and height are the same for a perfect circle
    borderRadius: "50%", // This makes the button circular
    border: "none", // Optional: remove the border for a cleaner look
    backgroundColor: "#212529", // Set your desired background color
    color: "#fff", // Set the color of the "X"
    fontSize: "20px", // Adjust the size of the "X"
    cursor: "pointer", // Changes the cursor on hover to indicate it's clickable
  };

  return (
    <button style={buttonStyle} onClick={() => setData(id)}>
      X
    </button>
  );
}
