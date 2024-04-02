import React, { useState, useContext } from 'react';
import Button from '@mui/material/Button';
import Menu, { MenuProps } from '@mui/material/Menu';
import { styled, alpha } from '@mui/material/styles';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import MenuItem from '@mui/material/MenuItem';
import { Card,  CardHeader, CardContent, Box, CardMedia, Divider, Typography } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

import Alerts from '@/app/components/alerts';
import api from '@/app/core/baseAPI';
import { CartItemProps } from '../page';
import CartContext from '../contexts/CartContext';

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
}))

export default function CartItem(item: CartItemProps) {
  const {cart, removeFromCart, updateItemQuantity} = useContext(CartContext);
  const [cartItem, setItem] = useState(item);
  const [changeQuantityAlertOpen, setChangeQuantityAlertOpen] = useState(false);
  const [itemRemovedAlertOpen, setItemRemovedAlertOpen] = useState(false);
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  function removeItem(product_id: number) {
    api.delete('shopping-list/remove-item/', {
      data: { product_id: product_id }
    })
      .then((response) => {
        console.log('product_id:', product_id);
        removeFromCart(product_id);
        setItemRemovedAlertOpen(true);
      });
  }

  function updateQuantity(product_id: number, quantity: number) {
    api.patch('shopping-list/change-quantity/', {
      product_id: product_id,
      quantity: quantity
    }, {
      headers: {'Content-Type': 'application/json'}
    })
      .then((response) => {
        setChangeQuantityAlertOpen(true);
        updateItemQuantity(product_id, quantity);
        handleClose();
      });
  }
  console.log('productprice type:', typeof item.product_price)
  return (
    <>
      <Card style={{ display: 'flex', width: '100%' }}>
        <CardContent sx={{ flex: '1 0 auto', width: '100%' }}>
            <Box sx={{display: 'flex'}}>
                <CardMedia
                    component="img"
                    sx={{ width: 125, height: 125, objectFit: 'contain', alignSelf: 'center' }}
                    src={item.preview_picture ? item.preview_picture : '/no_product_image.png'}
                />
                <Box sx={{display: 'flex', flexDirection: 'column', gap: '0.5rem', pl: 1, maxWidth: '100%'}}>
                  <CardHeader
                      sx={{width: '100%', height: '100%', overflow: 'hidden' }}
                      title={`${cartItem.product_name} ${(cartItem.product_company != '') ? `-${cartItem.product_company}` : ''}`}
                      titleTypographyProps={{ fontSize: '1rem'}}
                      subheader={
                        <>
                            {`Item price: $${item.product_price.toFixed(2)}`}
                            <br/>
                            {`Total price: $${(item.product_price * item.quantity).toFixed(2)}`}
                        </>
                    }/>
                  <Box sx={{display: 'flex', gap: '0.5rem', alignItems: 'center'}}>
                    <Button
                      sx={{marginLeft: '1rem', pl: '1rem', pr: '1rem', backgroundColor: 'white', color: 'black', border: '1px solid black'}}
                      id="demo-customized-button"
                      aria-controls={open ? 'demo-customized-menu' : undefined}
                      aria-haspopup="true"
                      aria-expanded={open ? 'true' : undefined}
                      disableElevation
                      onClick={handleClick}
                      endIcon={<KeyboardArrowDownIcon />}
                    >
                      Quantity: {item.quantity}
                    </Button>
                    <IconButton onClick={() => removeItem(item.product_id)}>
                      <DeleteIcon />
                    </IconButton>
                    <StyledMenu
                      id="demo-customized-menu"
                      MenuListProps={{
                        'aria-labelledby': 'demo-customized-button',
                      }}
                      anchorEl={anchorEl}
                      open={open}
                      onClose={handleClose}
                    >
                      {Array.from({ length: 10 }, (_, i) => (
                        <MenuItem
                          key={i}
                          onClick={() => updateQuantity(item.product_id, i + 1)}>
                          {i + 1}
                        </MenuItem>
                      ))}
                    </StyledMenu>
                  </Box>
                </Box>
            </Box>
        </CardContent>
      </Card>
      <Alerts message="Quantity Changed" severity="success"
              isOpen={changeQuantityAlertOpen}
              onClose={() => setChangeQuantityAlertOpen(false)} />
      <Alerts message="Item Removed" severity="success"
              isOpen={itemRemovedAlertOpen}
              onClose={() => setItemRemovedAlertOpen(false)} />
    </>
  );
}

export type { CartItemProps };