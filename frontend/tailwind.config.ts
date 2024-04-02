import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        background: "var(--background-color)",
        foreground: "var(--foreground-color)",
        primary: "var(--primary)",
        secondary: "var(--secondary)",
        light: "var(--light)",
        tab: "var(--tab)",
        hover: "var(--hover)",
        colorText: "var(--colorText)",
      },
    },
  },
  plugins: [],
};

export default config;
