import Link from "next/link";
import { useContext } from "react";
import { styled, alpha } from '@mui/material/styles';
import Menu, { MenuProps } from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import EditIcon from '@mui/icons-material/Edit';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import Divider from '@mui/material/Divider';
import LogoutIcon from '@mui/icons-material/Logout';
import { useRouter } from 'next/navigation'

import api from "../core/baseAPI";
import AuthContext from "../contexts/AuthContext";


interface UserDropdownProps {
    anchorEl: any;
    open: boolean;
    handleClose: any;
}

const StyledMenu = styled((props: MenuProps) => (
    <Menu
      elevation={0}
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'right',
      }}
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      {...props}
    />
  ))(({ theme }) => ({
    '& .MuiPaper-root': {
      borderRadius: 6,
      marginTop: theme.spacing(1),
      minWidth: 180,
      color:
        theme.palette.mode === 'light' ? 'rgb(55, 65, 81)' : theme.palette.grey[300],
      boxShadow:
        'rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px',
      '& .MuiMenu-list': {
        padding: '4px 0',
      },
      '& .MuiMenuItem-root': {
        '& .MuiSvgIcon-root': {
          fontSize: 18,
          color: theme.palette.text.secondary,
          marginRight: theme.spacing(1.5),
        },
        '&:active': {
          backgroundColor: alpha(
            theme.palette.primary.main,
            theme.palette.action.selectedOpacity,
          ),
        },
      },
    },
  }));


export default function UserDropdown({ anchorEl, open, handleClose }: UserDropdownProps) {
    const { auth, setIsAuthenticated, setUsername, setAvatar} = useContext(AuthContext);
    const router = useRouter();

    const logout = () => {
        const token: any = JSON.parse(localStorage.getItem("token") || "");
        const refreshToken: string = token.refresh;
    
        api.post("accounts/logout/", {
          refresh_token: refreshToken,
        }, {
          headers: { "Content-Type": "application/json" }
        })
        .then((response: any) => {
            setIsAuthenticated(false);
            setUsername("");
            setAvatar("");
            localStorage.removeItem("token");
            sessionStorage.removeItem("auth");
            handleClose();
            router.push("/");
        })
    };

    return (
    <StyledMenu
        id="demo-customized-menu"
        MenuListProps={{
          'aria-labelledby': 'demo-customized-button',
        }}
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
    >
        <Link passHref href='/profile' onClick={handleClose}>
            <MenuItem disableRipple>
                <EditIcon />
                Edit Profile
            </MenuItem>
        </Link>
        <Link passHref href='/order-history' onClick={handleClose}>
            <MenuItem disableRipple>
                <ReceiptLongIcon />
                Order History
            </MenuItem>
        </Link>
        <Divider sx={{ my: 0.5 }} />
        <MenuItem onClick={logout} disableRipple>
            <LogoutIcon />
            Logout
        </MenuItem>
    </StyledMenu>
    )
}