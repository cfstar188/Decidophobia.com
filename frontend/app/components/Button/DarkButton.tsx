import React, { useEffect } from "react";
import { atom, useAtom } from "jotai";

export const darkMode = atom(
  typeof window !== "undefined"
    ? localStorage.getItem("theme") || "light"
    : "light"
);

function DarkButton() {
  const [isDarkMode, setIsDarkMode] = useAtom(darkMode);

  useEffect(() => {
    const initialTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", initialTheme);
    console.log("Initial theme applied:", initialTheme);
  }, []);

  const toggleTheme = () => {
    const newTheme = isDarkMode === "light" ? "dark" : "light";
    setIsDarkMode(newTheme);

    localStorage.setItem("theme", newTheme);
    document.documentElement.setAttribute("data-theme", newTheme);

    console.log("Theme toggled to:", newTheme);
  };

  return (
    <button onClick={toggleTheme} className="p-2 bg-primary rounded">
      Toggle Theme
    </button>
  );
}

export default DarkButton;
