// localhost:3000
"use client";
import React from "react";
import Image from "next/image";
import SearchBar from "@/app/components/SearchBar";
import Link from "next/link";
import { NavBar } from "@/app/components/NavBar";
import AuthContext from "@/app/contexts/AuthContext";
import { useAtom } from "jotai";
import "./globals.css";

// Adjusted HomePage to include content from the provided HTML
export default function HomePage() {
  return (
    <div>
      <div className="divcent">
        <section className="hero-section">
          <h1
            style={{
              textAlign: "center",
              fontFamily: "Roboto",
              fontSize: "3rem",
              margin: "15px 0",
              fontWeight: 700,
              color: "colorText",
              textShadow: "2px 2px 4px rgba(0,0,0,0.2)",
            }}
          >
            Decidophobia.com
          </h1>
          <SearchBar />
        </section>
      </div>
    </div>
  );
}
