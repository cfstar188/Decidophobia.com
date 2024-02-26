// localhost:3000
"use client";
<<<<<<< Updated upstream
import React from "react";
import SearchTable from "@/app/components/SearchTable";
import SearchBar from "@/app/components/SearchBar";
=======
import React, { useEffect, useState } from "react";
import SearchTable from "./components/SearchTable";
import { User } from "../Library/Type";
import SearchBar from "./components/SearchBar";
>>>>>>> Stashed changes

// Unused pages in nextjs, purely testing page
export default function HomePage() {
<<<<<<< Updated upstream
=======
  const [query, setQuery] = useState("");
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/questionnaire/")
      .then((response) => response.json())
      .then((data) => setQuestions(data.questions));
  }, []);

  const handleSubmit = async (e: Event) => {
    e.preventDefault();

    const reponse = await fetch(`/api/search?searchQ=${query}`);
    const search = await reponse.json();
  };

>>>>>>> Stashed changes
  return (
    <>
      <SearchBar />
      <SearchTable />
    </>
  );
}
