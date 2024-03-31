import { selectedListAtom, selectedProductAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React, { useState } from "react";
import Link from "next/link";
import { PictureComp } from "./PictureComp";

function truncateString(str: string, num: number) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

function displayProduct(array: any, scrollIndex: number, fixedLength: number) {
  let arraySlice = array.slice(
    scrollIndex * fixedLength,
    (scrollIndex + 1) * fixedLength
  );
  while (arraySlice.length < 6) {
    arraySlice.push({
      product: "",
      company: "",
      price: "",
    });
  }
  return arraySlice;
}

export function HorizontalSelectBar() {
  const [selectedProducts] = useAtom(selectedProductAtom);
  const [, setSelectedAtom] = useAtom(selectedListAtom);
  const fixedLength = 6;

  const [scrollIndex, setScrollIndex] = useState(0);

  const scrollRight = () => {
    console.log(selectedProducts.length);
    if ((scrollIndex + 1) * fixedLength < selectedProducts.length + 1) {
      setScrollIndex(scrollIndex + 1);
    }
  };

  const scrollLeft = () => {
    if (scrollIndex > 0) {
      setScrollIndex(scrollIndex - 1);
    }
  };

  //Display the content from the scroll*amount of items(6) to the scroll+1*6
  const displayedProducts = displayProduct(
    selectedProducts,
    scrollIndex,
    fixedLength
  );

  const clearAll = () => {
    setSelectedAtom(() => {
      return [];
    });
  };

  return (
    <div className="w-full flex bg-gray-200 h-30 overflow-hidden p-2">
      <button
        onClick={scrollLeft}
        aria-label="Scroll Left"
        className="flex justify-center items-center bg-tab rounded-full w-5 h-5 my-auto"
        disabled={scrollIndex === 0}
      >
        {"<"}
      </button>
      <div className="basis-11/12 grid grid-cols-6 justify-start items-center gap-2 px-2">
        {displayedProducts.map((product: any, index: any) => (
          <div
            key={index}
            className="bg-tab min-w-[200px] min-h-24 max-h-24  p-2 rounded flex-1"
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
                    {truncateString(product.name, 33)}
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
      <button
        onClick={scrollRight}
        aria-label="Scroll Right"
        className="flex justify-center items-center bg-tab rounded-full w-5 h-5 my-auto"
      >
        {">"}
      </button>
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
