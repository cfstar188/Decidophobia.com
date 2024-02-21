import { selectedListAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React, { useState } from "react";

type squareCheckBox = {
  id: number;
  label: string;
  onChange: any;
};

function SquareCheckbox({ id, label, onChange }: squareCheckBox) {
  const [isChecked, setIsChecked] = useState(false);
  const [checkedList, setCheckedAtom] = useAtom(selectedListAtom);

  //Updates the checked fuction
  const toggleCheckbox = () => {
    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);
    if (onChange) {
      onChange(newCheckedState);
      setCheckedAtom((checkedList) => {
        if (checkedList.includes(id)) {
          return checkedList.filter((item) => item !== id);
        } else {
          return [...checkedList, id];
        }
      });
    }
  };

  return (
    <div className="flex my-auto">
      <div
        className="items-center cursor-pointer my-auto"
        onClick={toggleCheckbox}
      >
        <div
          className={`col-span-1 w-5 h-5 border-2 border-gray-400 mr-2 ${
            isChecked ? "bg-cyan-500" : "bg-transparent"
          }`}
        />
      </div>
      <label className="text-white">{label}</label>
    </div>
  );
}

export default SquareCheckbox;
