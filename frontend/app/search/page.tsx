// localhost:3000/search/
"use client";
import React, { useEffect, useState } from "react";
import SearchTable from "@/app/components/Table/SearchTable";
import HorizontalSelectBar from "@/app/components/CompareBar";
import { useAtom } from "jotai";
import {
  allProductAtom,
  prevSearchParams,
  selectedProductAtom,
} from "@/Library/SelectedAtom";
import api from "../core/baseAPI";
import JsonToAtom from "@/Library/JsonToSearch";
import { useSearchParams } from "next/navigation";

export default function SearchPage() {
  const [selectedProducts] = useAtom(selectedProductAtom);
  const [products, setAllProduct] = useAtom(allProductAtom);
  const searchParams = useSearchParams();

  const productName = searchParams.get("searchQ");
  const priceFactor = searchParams.get("priceFactor");
  const customerReview = searchParams.get("customerReview");
  const shipping = searchParams.get("shipping");
  const returnPolicy = searchParams.get("returnPolicy");
  const brandReputation = searchParams.get("brandReputation");
  
  console.log("productName", productName);
  console.log("priceFactor", priceFactor);
  console.log("customerReview", customerReview);
  console.log("shipping", shipping);
  console.log("returnPolicy", returnPolicy);
  console.log("brandReputation", brandReputation);

  useEffect(() => {
    fetch(`http://localhost:8000/questionnaire/?searchQ=${productName}&priceFactor=${priceFactor}&customerReview=${customerReview}&shipping=${shipping}&returnPolicy=${returnPolicy}&brandReputation=${brandReputation}`)
      .then((response) => {
        console.log("received response");
        return response.json();
      })
      .then((data) => {
        console.log(data);
        const transformedData = JsonToAtom(data);
        setAllProduct(transformedData);
      })
      .catch((error) => {
        console.error("Error fetching questions:", error);
      });
  }, []);

  return (
    <>
      <SearchTable />
      <div className="fixed bottom-0 left-0 w-full">
        <HorizontalSelectBar />
      </div>
      <button
        className="bg-blue-700"
        onClick={(e: any) => {
          console.log(products);
        }}
      >
        Click
      </button>
      <button
        className="bg-blue-700"
        onClick={(e: any) => {
          console.log(selectedProducts);
        }}
      >
        Click
      </button>
    </>
  );
}
