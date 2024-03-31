"use client";
import React, { useContext } from 'react';

import CartItem from './cartItem';
import { CartItemProps } from '../page';
import CartContext from '../contexts/CartContext';

export default function Cart() {
  const { cart } = useContext(CartContext);
  console.log('cart cart.tsx:', cart);
  return (
      <>
        <div 
          className="cart-items" 
          style={{
            width: '100%',
            display: 'flex',
            flexDirection: 'column',
            flexWrap: 'wrap',
            justifyContent: 'space-evenly',
            gap: '1rem',
          }}
        >
          {cart.map((item: CartItemProps, index: number) => (
            <CartItem key={index} {...item} />
          ))}
        </div>
      </>
    );
}
