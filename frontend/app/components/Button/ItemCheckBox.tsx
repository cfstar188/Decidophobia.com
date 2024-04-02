import { selectedListAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React, { useEffect, useState } from "react";

type squareCheckBox = {
  id: number;
  label: string;
};

function SquareCheckbox({ id, label }: squareCheckBox) {
  const [isChecked, setIsChecked] = useState(false);
  const [selectedList, setCheckedAtom] = useAtom(selectedListAtom);

  useEffect(() => {
    if (selectedList.includes(id)) {
      setIsChecked(true);
    } else {
      setIsChecked(false);
    }
  }, [selectedList]);

  //Updates the checked fuction
  const toggleCheckbox = () => {
    setCheckedAtom((checkedList) => {
      if (checkedList.includes(id)) {
        setIsChecked(false);
        return checkedList.filter((item) => item !== id);
      } else {
        setIsChecked(true);
        return [...checkedList, id];
      }
    });
  };

  return (
    <div className="flex my-auto pb-1">
      <div
        className="items-center cursor-pointer my-auto"
        onClick={toggleCheckbox}
      >
        <div
          className={`col-span-1 w-5 h-5 border-2 border-gray-400 mr-2 ${
            isChecked ? "bg-secondary" : "bg-transparent"
          }`}
        />
      </div>
      <label className="">{label}</label>
    </div>
  );
}

export default SquareCheckbox;
