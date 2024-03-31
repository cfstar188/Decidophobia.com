// localhost:3000
"use client";
import React from "react";
import SearchTable from "@/app/components/Table/SearchTable";
import SearchBar from "@/app/components/SearchBar";

// Unused pages in nextjs, purely testing page
export default function HomePage() {
  return (
    <>
      <SearchBar />
      <SearchTable />
    </>
  );
}
