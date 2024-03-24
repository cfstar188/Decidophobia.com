import React, { useState } from 'react';
import { CardBody, CardTitle, CardSubtitle, CardText } from 'reactstrap';
import Button from '@mui/material/Button';
import { Card,  CardHeader, CardContent, Box, CardMedia } from '@mui/material';

import Alerts from '@/app/components/alerts';
import api from '@/app/core/baseAPI';
import { CartItemProps } from '../page';
import { set } from 'react-hook-form';
import noImage from '@/public/no_product_image.png';

const CartItem: React.FC<{item: CartItemProps}> = ({ item }) => {
  const [cartItem, setItem] = useState(item);
  // const [showAlert, setShowAlert] = useState(false);
  const [decreaseAlertOpen, setDecreaseAlertOpen] = useState(false);
  const [increaseAlertOpen, setIncreaseAlertOpen] = useState(false);

  function updateQuantity(product_id: number, quantity: number, up_or_down: number) {
    api.patch('shopping-list/change-quantity/', {
      product_id: product_id,
      quantity: quantity
    }, {
      headers: {'Content-Type': 'application/json'}
    })
      .then((response) => {
        if (up_or_down === 1) {
          setIncreaseAlertOpen(true);
        }
        else {
          setDecreaseAlertOpen(true);
        }
        setItem({...cartItem, quantity: quantity});
      });
  }

  return (
    <>
      <Card
        style={{
          width: '15rem',
          border: '1px solid white',
          borderRadius: '10px',
        }}
      >
        <CardMedia
          component='img'
          alt='img'
          src={item.preview_picture ? item.preview_picture : '/no_product_image.png'}
          style={{borderRadius: '10px 10px 0 0', objectFit: 'contain'}}
          sx={{width: '100%', height: '10rem'}}
        />
        <Box style={{padding: '0.5rem'}}>
          <CardHeader 
            style={{margin: '-0.5rem'}}
            title={`$${item.product_price}`}
            titleTypographyProps={{ fontSize: '1rem'}}
            subheader={`${cartItem.product_name} - ${cartItem.product_company}`}
          />
          <Box style={{
            display: 'flex',
            justifyContent: 'space-evenly',
            alignItems: 'center',
          }}>
            <Button
              style={{
                backgroundColor: 'rgba(255, 0, 0, 0.4)',
                borderColor: 'rgba(255, 0, 0, 0.5)',
                color: 'white',
                borderRadius: '5px',
                padding: '10px 20px',
                fontSize: '15px',
                fontWeight: 'bold',
                cursor: 'pointer'
              }}
              onClick={() => {updateQuantity(cartItem.product_id, cartItem.quantity-1, 0)}}
              disabled = {cartItem.quantity === 1}
            >
              -
            </Button>
            <CardText>
              Quantity: {cartItem.quantity}
            </CardText>
            <Button
              style={{
                backgroundColor: '#007bff',
                borderColor: '#007bff',
                color: 'white',
                borderRadius: '5px',
                padding: '10px 20px',
                fontSize: '15px',
                fontWeight: 'bold',
                cursor: 'pointer'
              }}
              onClick={() => {updateQuantity(cartItem.product_id, cartItem.quantity+1, 1)}}
            >
              +
            </Button>
          </Box>
        </Box>
      </Card>
      <Alerts message="Decreased Quantity" severity="success"
              isOpen={decreaseAlertOpen}
              onClose={() => setDecreaseAlertOpen(false)} />
      <Alerts message="Increased Quantity" severity="success"
              isOpen={increaseAlertOpen}
              onClose={() => setIncreaseAlertOpen(false)} />
    </>
  );
}

export default CartItem;
export type { CartItemProps };