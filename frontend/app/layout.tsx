"use client";
import { Inter } from "next/font/google";
import { NavBar } from "@/app/components/NavBar";
import "@/app/globals.css";
import { JotaiProvider } from "@/app/components/Providers/JotaiProvider";
import React from "react";
import { useAtom } from "jotai";
import { darkMode } from "./components/Button/DarkButton";
import { AuthProvider } from "./contexts/AuthContext";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [isDarkMode, setIsDarkMode] = useAtom(darkMode);
  return (
    <html lang="en">
      <body className={inter.className + ""}>
        <AuthProvider>
          <JotaiProvider>
            <div data-theme={isDarkMode}>
              <NavBar />
              {children}
            </div>
          </JotaiProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
