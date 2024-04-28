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
  const [lastSearchParams, checkSearchQ] = useAtom(prevSearchParams);
  console.log("productName", productName);
  console.log("priceFactor", priceFactor);
  console.log("customerReview", customerReview);
  console.log("shipping", shipping);
  console.log("returnPolicy", returnPolicy);
  console.log("brandReputation", brandReputation);

  useEffect(() => {
    if (productName !== lastSearchParams) {
      api.get(`/questionnaire/?searchQ=${productName}&priceFactor=${priceFactor}&customerReview=${customerReview}&shipping=${shipping}&returnPolicy=${returnPolicy}&brandReputation=${brandReputation}`)
        // fetch(`http://localhost:8000/questionnaire/?searchQ=${newParams}`)
        .then((response) => response.data)
        .then((data) => {
          console.log(data);
          console.log(productName, lastSearchParams);
          const transformedData = JsonToAtom(data);
          setAllProduct(transformedData);
          checkSearchQ(productName);
        })
        .catch((error) => {
          console.error("Error fetching questions:", error);
        });
    }
  }, [productName, lastSearchParams]);

  return (
    <>
      <SearchTable />
      <div className="fixed bottom-0 left-0 w-full">
        <HorizontalSelectBar />
      </div>
    </>
  );
}
