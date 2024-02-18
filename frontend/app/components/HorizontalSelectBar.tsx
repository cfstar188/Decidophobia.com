import { selectedProductAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";
import React from "react";

export function HorizontalSelectBar({ current, total }: any) {
  // Calculate the width percentage of the current progress
  const progressWidth = total > 0 ? `${(current / total) * 100}%` : "0%";
  const [selectedProducts, selectProduct] = useAtom(selectedProductAtom);

  return (
    <div className="w-full">
      <div className="w-full bg-gray-200 h-4 rounded-full overflow-hidden">
        <div className="bg-blue-500 h-full" style={{ width: progressWidth }} />
      </div>
      <table className="w-full mt-2">
        <tbody>
          <tr>
            {selectedProducts.map((product, index) => (
              <td key={index} className="text-center px-3">
                {/* Assuming 'product' is an object with a 'name' property */}
                {product}
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default HorizontalSelectBar;
