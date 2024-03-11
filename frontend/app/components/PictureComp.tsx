import React from "react";
import { CircularXButton } from "@/app/components/Button/CircularXButton";

export function PictureComp({ id, setData, src }: any) {
  const buttonStyle = {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    width: "50px", // Adjust the size as needed
    height: "50px", // Ensure width and height are the same for a perfect circle
    borderRadius: "50%", // This makes the button circular
    border: "none", // Optional: remove the border for a cleaner look
    backgroundColor: "#f00", // Set your desired background color
    color: "#fff", // Set the color of the "X"
    fontSize: "20px", // Adjust the size of the "X"
    cursor: "pointer", // Changes the cursor on hover to indicate it's clickable
  };

  return (
    <div>
      <CircularXButton id={id} setData={setData} />
      <img className="h-80 w-50" src={src} />
    </div>
  );
}
