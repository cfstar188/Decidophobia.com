"use client";
import SearchTable from "@/app/components/SearchTable";
import React, { useState } from "react";

export default function SearchPageQuery() {
  const [query, setQuery] = useState("");

  const handleSubmit = async (e: Event) => {
    e.preventDefault();

    const reponse = await fetch(`/api/search?searchQ=${query}`);
    const search = await reponse.json();
  };

  return (
    <>
      <SearchTable />
    </>
  );
}
