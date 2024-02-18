import React, { useState } from "react";

function SquareCheckbox({ label, onChange }: any) {
  const [isChecked, setIsChecked] = useState(false);

  const toggleCheckbox = () => {
    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);
    if (onChange) {
      onChange(newCheckedState);
    }
  };

  return (
    <div
      className="col-span-1 items-center cursor-pointer"
      onClick={toggleCheckbox}
    >
      <div
        className={`w-5 h-5 border-2 border-gray-400 mr-2 ${
          isChecked ? "bg-cyan-500" : "bg-transparent"
        }`}
      ></div>
      {label && <span className="select-none">{label}</span>}
    </div>
  );
}

export default SquareCheckbox;
