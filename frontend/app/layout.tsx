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
  /*
  useEffect(() => {
    const theme = isDarkMode == "dark" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", theme);
    console.log(isDarkMode);
  }, [isDarkMode]);

  const toggleTheme = () => {
    if (isDarkMode == "light") {
      setIsDarkMode("dark");
    } else {
      setIsDarkMode("light");
    }
  };
  */

  return (
    <html lang="en">
      <body className={inter.className + " text-white"}>
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
