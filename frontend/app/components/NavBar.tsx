import { useAtom } from "jotai";
import { authAtom } from "@/Library/AuthAtom";
// import AuthContext from "@/app/contexts/AuthContext";

/*
export function NavBar() {
  const [auth, setAuth] = useAtom(authAtom);

  const logout = () => {
    setAuth({ isAuthenticated: false, username: "" });
    localStorage.removeItem("token");
  };

  return (
    <nav style={{ display: "flex" }}>
      <div>
        <Link href="/">Home</Link>
        <Link href="#">Discussion Board</Link>
        {auth.isAuthenticated && <Link href="/cart">Shopping Cart</Link>}
      </div>
      {!auth.isAuthenticated ? (
        <div style={{ marginLeft: "auto", display: "flex" }}>
          <p>Welcome, {auth.username}!</p>
          <Link href="/logout" onClick={logout}>
            Logout
          </Link>
        </div>
      ) : (
        <div style={{ marginLeft: "auto" }}>
          <Link href="/login">Login/Signup</Link>
        </div>
      )}
    </nav>
  );
}

*/

import Link from "next/link";
import { usePathname } from "next/navigation";

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

  const logout = () => {
    setAuth({ isAuthenticated: false, username: "" });
    localStorage.removeItem("token");
  };

  const currentRoute: string = usePathname();
  const newRoute: string = currentTab(currentRoute);

  const mainLinks: LinkProps[] = [
    { link: "/", label: "Home" },
    { link: "/login", label: <>Welcome, {auth.username}!</> },
    { link: "/logout", label: "logout" },
    { link: "/#", label: "Discussion" },
    { link: "/shopping-cart", label: "Cart" },
  ];

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
    </nav>
  );
}
