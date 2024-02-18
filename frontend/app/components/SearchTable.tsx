"use client";
import React, { useState } from "react";
import { PictureComp } from "../components/PictureComp";
import SquareCheckbox from "./SquareButton";
import HorizontalSelectBar from "./HorizontalSelectBar";
import { User } from "../../Library/Type";
import { useAtom } from "jotai";
import { allProductAtom } from "@/Library/SelectedAtom";

export function SearchTable() {
  const [users] = useAtom(allProductAtom);
  console.log(users);
  const [user, setUser] = useState<User[]>(users);

  return (
    <>
      <div className="grid grid-cols-4 min-w-[500px] gap-4 p-4">
        {user.map((user, index) => (
          <div
            key={index}
            className="border border-gray-300 rounded-lg py-4 px-10 flex flex-col items-center justify-between"
          >
            <div className="grid-cols-2 gird-rows-auto w-full">
              <img
                src={user.picture}
                alt={user.product}
                className="max-w-full max-h-[200px] object-contain col-span-2 m-auto"
              />
              <div />
              <div className="text-white col-span-2">{user.product}</div>
              <div className="text-white col-span-2">{user.company}</div>
              <div className="text-white col-span-1">{user.price}</div>
              <div className="flex">
                <SquareCheckbox className="col-span-1 py-auto" />
                <div className="text-white col-span-1 my-auto">Compare</div>
              </div>
            </div>
            {user.url}
          </div>
        ))}
      </div>
      <HorizontalSelectBar />
    </>
  );
}

export default SearchTable;
