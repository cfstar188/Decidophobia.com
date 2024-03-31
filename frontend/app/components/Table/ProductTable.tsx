// Table.tsx
"use client";
import React from "react";
import { PictureComp } from "@/app/components/PictureComp";
import { useAtom } from "jotai";
import { selectedProductAtom } from "@/Library/SelectedAtom";
import { Product } from "@/Library/Type";

export function ProductTable() {
  const [selectedProducts] = useAtom(selectedProductAtom);

  const keys =
    selectedProducts.length > 0
      ? (Object.keys(selectedProducts[0]) as (keyof Product)[])
      : [];

  return (
    <>
      <table className="w-full border-collapse">
        <tbody>
          {keys.map((key, index) => {
            // Skip the id row
            if (key === "id") {
              return null;
            }

            if (key === "company") {
              return null;
            }

            // This is to make every row the same height except for the picture
            const rowClass = key !== "picture" ? "h-20" : "";

            return (
              <tr key={key} className={rowClass}>
                <th className="bg-tab text-left pl-5 pr-3">
                  {key === "picture" ? "" : <label>{key.toUpperCase()}</label>}
                </th>
                {selectedProducts.map((product, idx) => (
                  <td key={idx} className="p-8 border-b border-gray-300">
                    {key === "picture" ? (
                      <PictureComp
                        id={product["id"]}
                        src={product[key]}
                        print={product}
                        button={true}
                        height={"h-80 w-full object-contain"}
                      />
                    ) : key === "price" ? (
                      <div className="">${product[key]}</div>
                    ) : key === "link" ? (
                      <a
                        href={product[key]}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        Link to Store
                      </a>
                    ) : (
                      <div className="">{product[key]}</div>
                    )}
                  </td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}

export default ProductTable;
