"use client";
import React, { useEffect, useState } from "react";
import { useAtom } from "jotai";
import HorizontalSelectBar from "@/app/components/HorizontalSelectBar";
import SquareCheckbox from "@/app/components/Button/SquareButton";
import { allProductAtom } from "@/Library/SelectedAtom";


export function SearchTable() {
  const [users] = useAtom(allProductAtom);
  const [tester, setTester] = useState();
  // I have set the buy button to this state, but I think you might need a state that updates inside a useeffect that calls your api.
  // This is just I thought since I have been doing a lot of react learning for this project. So you might know a better way.
  const [buy, setBuyState] = useState();

  useEffect(() => {}, [users]);

  return (
    <>
      <button
        className="bg-blue-700"
        onClick={(e: any) => {
          console.log(users);
        }}
      >
        CLICK ON ME
      </button>
      <div className="grid grid-cols-4 min-w-[500px] gap-4 p-4">
        {users.map((user: any, index) => (
          <div
            key={index}
            className="border border-gray-300 rounded-lg py-4 px-10 flex flex-col items-center justify-between"
          >
            <div className="grid-cols-2 gird-rows-auto w-full">
              <img
                src={user.image}
                alt={user.image}
                className="max-w-full max-h-[200px] object-contain col-span-2 m-auto"
              />
              <div />
              <div className="text-white col-span-2">{user.product}</div>
              <div className="text-white col-span-2">{user.company}</div>
              <div className="text-white col-span-1">Price: {user.price}</div>
              <SquareCheckbox id={index} label="Compare" onChange={setTester} />
              <button
                className="bg-blue-700"
                onClick={(e: any) => {
                  setBuyState(e);
                }}
              >
                BUY NOW
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

export default SearchTable;
