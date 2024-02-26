// localhost:3000/search/
"use client";
import React, { useEffect, useState } from "react";
import SearchTable from "@/app/components/SearchTable";
import HorizontalSelectBar from "@/app/components/HorizontalSelectBar";
import { useAtom } from "jotai";
import { allProductAtom } from "@/Library/SelectedAtom";
import JsonToAtom from "@/Library/JsonToSearch";
import { useSearchParams } from "next/navigation";

export default function SearchPage() {
  const [questions, setQuestions] = useState([]);

  const [products, setAllProduct] = useAtom(allProductAtom);
  const searchParams = useSearchParams();

  const newParmas = searchParams.get("searchQ");
  const newParmas2 = searchParams.get("new");
  console.log(newParmas);
  console.log(newParmas2);

  useEffect(() => {
    fetch(`http://localhost:8000/questionnaire/?searchQ=${newParmas}`)
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
      <button
        className="bg-blue-700"
        onClick={(e: any) => {
          console.log(products);
        }}
      />
    </>
  );
}
