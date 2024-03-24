import { selectedListAtom, selectedProductAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React, { useEffect } from "react";
import Link from "next/link";
import { PictureComp } from "./PictureComp";

function truncateString(str: string, num: number) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

export function HorizontalSelectBar() {
  const [selectedProducts] = useAtom(selectedProductAtom);
  const [, setSelectedAtom] = useAtom(selectedListAtom);
  const fixedLength = 6;

  const displayArray = Array.from({ length: fixedLength }, (_, index) => {
    return (
      selectedProducts[index] || {
        product: "",
        company: "",
        price: "",
      }
    );
  });

  const clearAll = () => {
    setSelectedAtom(() => {
      return [];
    });
  };

  return (
    <div className="w-full flex bg-gray-200 h-30 overflow-hidden p-2">
      <div className="basis-11/12 grid grid-cols-6 justify-start items-center gap-2">
        {displayArray.map((product, index) => (
          <div
            key={index}
            className="bg-tab min-w-[200px] min-h-24 max-h-24 text-white p-2 rounded flex-1"
          >
            <div className="flex">
              <div className="basis-1/3 justify-center items-center h-24">
                <PictureComp
                  id={product.id}
                  src={product.picture}
                  print={product}
                  height={"object-contain h-full m-auto"}
                />
              </div>
              {typeof product.picture === "string" ? (
                <div className="basis-2/3 pl-2">
                  <div className="line-clamp-2 overflow-hidden">
                    {truncateString(product.product, 33)}
                  </div>
                  <div className="">${`${product.price}`}</div>
                </div>
              ) : (
                <></>
              )}
            </div>
          </div>
        ))}
      </div>
      <div className="basis-1/12 flex flex-col justify-between items-center text-center">
        <Link
          className={"bg-tab rounded m-auto w-5/6"}
          href={"/product"}
          key={"compareKey"}
          passHref
          shallow
        >
          Compare
        </Link>
        <button className={"bg-tab rounded m-auto w-5/6"} onClick={clearAll}>
          Delete All
        </button>
      </div>
    </div>
  );
}

export default HorizontalSelectBar;
