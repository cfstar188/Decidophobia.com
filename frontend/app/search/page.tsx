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

  const newParams = searchParams.get("searchQ") || "";
  const [lastSearchParams, checkSearchQ] = useAtom(prevSearchParams);

  useEffect(() => {
    if (newParams !== lastSearchParams) {
      api
        .get(`/questionnaire/?searchQ=${newParams}`)
        // fetch(`http://localhost:8000/questionnaire/?searchQ=${newParams}`)
        .then((response) => response.data)
        .then((data) => {
          console.log(data);
          console.log(newParams, lastSearchParams);
          const transformedData = JsonToAtom(data);
          setAllProduct(transformedData);
          checkSearchQ(newParams);
        })
        .catch((error) => {
          console.error("Error fetching questions:", error);
        });
    }
  }, [newParams, lastSearchParams]);

  return (
    <>
      <SearchTable />
      <div className="fixed bottom-0 left-0 w-full">
        <HorizontalSelectBar />
      </div>
    </>
  );
}
