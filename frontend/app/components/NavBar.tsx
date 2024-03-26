import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, useContext } from "react";
import Button from '@mui/material/Button';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

import LoginModal from "./loginModal";
import RegisterModal from './registerModal';
import AuthContext from "../contexts/AuthContext";
import UserDropdown from "./userDropdown";
import { Avatar } from "@mui/material";


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
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);
  const [isRegisterModalOpen, setIsRegisterModalOpen] = useState(false);
  const { auth } = useContext(AuthContext);

  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
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
            <Button
              id="demo-customized-button"
              aria-controls={open ? 'demo-customized-menu' : undefined}
              aria-haspopup="true"
              aria-expanded={open ? 'true' : undefined}
              variant="contained"
              disableElevation
              onClick={handleClick}
              endIcon={<KeyboardArrowDownIcon />}
              startIcon={<Avatar src={auth.avatar} alt={auth.username} />}
            >
            Welcome, {auth.username}!
            </Button>
            <UserDropdown anchorEl={anchorEl} open={open} handleClose={handleClose} />
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
