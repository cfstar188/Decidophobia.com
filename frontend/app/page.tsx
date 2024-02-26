// Table.tsx
"use client";
import React, { useState } from "react";
import SearchTable from "./components/SearchTable";
import { User } from "../Library/Type";
import SearchBar from "./components/SearchBar";

export default function HomePage() {
  const [query, setQuery] = useState("");

  const handleSubmit = async (e: Event) => {
    e.preventDefault();

    const reponse = await fetch(`/api/search?searchQ=${query}`);
    const search = await reponse.json();
  };

  return (
    <>
      <SearchBar />
      <SearchTable />
    </>
  );
}
