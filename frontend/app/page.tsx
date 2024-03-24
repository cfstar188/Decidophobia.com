// localhost:3000
"use client";
import React from "react";
import Image from "next/image";
import SearchBar from "@/app/components/SearchBar";
import Link from "next/link";
import { NavBar } from "@/app/components/NavBar";
import { authAtom } from "@/Library/AuthAtom";
import { useAtom } from "jotai";

// Adjusted HomePage to include content from the provided HTML
export default function HomePage() {

  return (
    <div>

      <div className="divcent">
        <section className="hero-section">
          <h1 style={{ textAlign: "center" }}>Decidophobia.com</h1>
          <SearchBar />
        </section>
      </div>
    </div>
  );
}
