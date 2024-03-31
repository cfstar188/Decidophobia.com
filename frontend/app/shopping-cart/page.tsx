// localhost:3000/shopping-cart/

'use client'
import React, { useState, useEffect, useContext }from 'react';
import ShoppingCart from './shopcart';
import { CartProvider } from './contexts/CartContext';

interface CartItemProps {
    product_id: number;
    product_name: string;
    product_company: string;
    product_price: number;
    quantity: number;
    preview_picture: string;
    url: string;
}

export default function ShoppingCartPage() {
    return (
        <CartProvider>
            <ShoppingCart />
        </CartProvider>
    );
};

export type { CartItemProps };