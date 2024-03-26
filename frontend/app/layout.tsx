"use client";
import { Inter } from "next/font/google";
import { NavBar } from "@/app/components/NavBar";
import "./globals.css";
import { JotaiProvider } from "@/app/components/Providers/JotaiProvider";
import { AuthProvider } from "./contexts/AuthContext";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className + " text-white"}>
        <AuthProvider>
        <JotaiProvider>
          <NavBar />
          {children}
        </JotaiProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
