import { selectedProductAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React from "react";

export function HorizontalSelectBar({ current, total }: any) {
  const [selectedProducts, selectProduct] = useAtom(selectedProductAtom);
  const fixedLength = 4;

  const displayArray = Array.from({ length: fixedLength }, (_, index) => {
    return (
      selectedProducts[index] || {
        product: "",
        company: "",
        price: "",
      }
    );
  });

  return (
    <div className="w-full bg-gray-200 h-25 overflow-hidden p-2">
      <div className="grid grid-cols-4 justify-start items-center gap-2">
        {displayArray.map((product, index) => (
          <div
            key={index}
            className="bg-blue-500 min-w-[200px] min-h-20 text-white p-2 rounded flex-1"
          >
            <div className="">{product.product}</div>
            <div className="">{product.company}</div>
            <div className="">{`${product.price}`}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default HorizontalSelectBar;
