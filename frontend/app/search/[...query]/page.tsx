/*
"use client";
import JsonToAtom from "@/Library/JsonToSearch";
import { allProductAtom } from "@/Library/SelectedAtom";
import HorizontalSelectBar from "@/app/components/CompareBar";
import SearchTable from "@/app/components/Table/SearchTable";
import { useAtom } from "jotai";
import React, { useEffect } from "react";
import { useSearchParams } from "next/navigation";

export default function SearchPageQuery() {
  const [products, setAllProduct] = useAtom(allProductAtom);
  const searchParams = useSearchParams();

  const newParmas = searchParams.get("searchQ");
  const newParmas2 = searchParams.get("new");
  console.log("params", newParmas);
  console.log("params2:", newParmas2);

  useEffect(() => {
    const url = `http://localhost:8000/questionnaire/?searchQ=${newParmas}`;
    console.log(url);

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        const transformedData = JsonToAtom(data);
        setAllProduct(transformedData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <>
      <SearchTable />
      <HorizontalSelectBar />
    </>
  );
}
*/
