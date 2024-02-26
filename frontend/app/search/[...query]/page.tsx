// localhost:3000/search/[anything]
"use client";
import JsonToAtom from "@/Library/JsonToSearch";
import { allProductAtom } from "@/Library/SelectedAtom";
import HorizontalSelectBar from "@/app/components/HorizontalSelectBar";
import SearchTable from "@/app/components/SearchTable";
import { useAtom } from "jotai";
import React, { useEffect, useState } from "react";

export default function SearchPageQuery() {
  const [questions, setQuestions] = useState([]);
  const [products, setAllProduct] = useAtom(allProductAtom);

  useEffect(() => {
    fetch("http://localhost:8000/questionnaire/")
      .then((response) => response.json())
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
      <HorizontalSelectBar />
    </>
  );
}
