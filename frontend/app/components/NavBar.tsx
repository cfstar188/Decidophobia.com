import { useAtom } from "jotai";
import { authAtom } from "@/Library/AuthAtom";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import api from "../core/baseAPI";
import LoginModal from "./loginModal";
import RegisterModal from './registerModal';

interface LinkProps {
  label: any;
  link: string;
}

const hoverStyle: string = "hover:link link-underline link-underline-black";
const linkStyle: string =
  "flex items-center pl-[30px] pr-[30px] h-full text-xl font-semibold no-underline";
const activeStyle: string = linkStyle + " text-white bg-tab";
const nonActiveStyle: string = linkStyle + " text-white";

function currentTab(currentRoute: string) {
  const newArray: string[] = currentRoute.split("/");
  for (let i: number = 0; i < newArray.length; i++) {
    if (newArray[i] === "Home") {
      return "/";
    } else if (newArray[i] === "login") {
      return "/login";
    } else if (newArray[i] === "Discussion") {
      return "/#";
    }
  }
  return "/";
}

export function NavBar() {
  const [auth, setAuth] = useAtom(authAtom);
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);

  const logout = () => {
    const token: any = JSON.parse(localStorage.getItem("token") || "");
    const refreshToken: string = token.refresh;

    api.post("accounts/logout/", {
      refresh_token: refreshToken,
    }, {
      headers: { "Content-Type": "application/json" }
    });
    setAuth({ isAuthenticated: false, username: "" });
    localStorage.removeItem("token");
  };

  const currentRoute: string = usePathname();
  const newRoute: string = currentTab(currentRoute);

  const mainLinks: LinkProps[] = auth.isAuthenticated ? [
    { link: "/", label: "Home" },
    { link: "/#", label: "Discussion" },
    { link: "/shopping-cart", label: "Cart" },
  ] :
  [
    { link: "/", label: "Home" },
    { link: "/#", label: "Discussion" }
  ]

  const mainItems: JSX.Element[] = mainLinks.map((item: LinkProps, index) => (
    <Link
      className={newRoute === item.link ? activeStyle : nonActiveStyle}
      href={item.link}
      key={item.label + index}
      passHref
      shallow
    >
      <label className={hoverStyle + " w-full"}>{item.label}</label>
    </Link>
  ));

  return (
    <nav className="h-10 flex justify-between items-center bg-primary drop-shadow-lg">
      <div className="flex h-10">{mainItems}</div>
      <div className="flex h-10">
        {auth.isAuthenticated ? (
          <>
            <Link
              className={newRoute === '/logout' ? activeStyle : nonActiveStyle}
              href="/profile"
            >
              <label className={hoverStyle + " w-full"}>Welcome, {auth.username}!</label>
            </Link>
            <Link
              className={newRoute === '/logout' ? activeStyle : nonActiveStyle}
              href="/"
              onClick={logout}
            >
              <label className={hoverStyle + " w-full"}>Logout</label>
            </Link>
          </>
        ) : (
          <>
            <button onClick={() => setIsLoginModalOpen(true)}>Login/Register</button>
            <LoginModal isOpen={isLoginModalOpen} onClose={() => setIsLoginModalOpen(false)} setIsRegisterModalOpen={setIsRegisterModalOpen} />
            <RegisterModal isOpen={isRegisterModalOpen} onClose={() => setIsRegisterModalOpen(false)} setIsLoginModalOpen={setIsLoginModalOpen} />
          </>
        )}
      </div>
    </nav>
  );
}
