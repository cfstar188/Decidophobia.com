import { selectedListAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React from "react";

export function PictureComp({ id, src, print, button, height }: any) {
  const [, setCheckedAtom] = useAtom(selectedListAtom);

  const deleteItem = () => {
    setCheckedAtom((checkedList) => {
      console.log(print);
      if (checkedList.includes(id)) {
        return checkedList.filter((item) => item !== id);
      } else {
        return [...checkedList, id];
      }
    });
  };

  return (
    <>
      <div className="flex justify-end">
        {button ? (
          <button
            className="flex items-center justify-center w-5 h-5 rounded-full bg-black text-xl cursor-pointer"
            onClick={() => deleteItem()}
          >
            X
          </button>
        ) : (
          <></>
        )}
      </div>
      {typeof src === "string" ? <img className={height} src={src} /> : <></>}
    </>
  );
}
