import React from "react";
import { CircularXButton } from "./CircularXButton";

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
      <img src="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-compare-iphone-15-202309?wid=384&hei=512&fmt=jpeg&qlt=90&.v=1692827832423" />
    </div>
  );
}
