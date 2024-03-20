"use client";
import React, { useState, useEffect } from 'react';

import CartItem from './cartItem';
import { CartItemProps } from '../page';
import api from '../../core/baseAPI';

const Cart: React.FC<{cart: CartItemProps[]}> = ({ cart }) => {
    return (
        <>
          <div 
            className="cart-items" 
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              justifyContent: 'space-evenly',
              gap: '1rem',
            }}
          >
            {cart.map((item, index) => (
              <CartItem key={index} item={item} />
            ))}
          </div>
        </>
      );
}

export default Cart;