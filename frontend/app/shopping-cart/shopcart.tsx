// localhost:3000/shopping-cart/

'use client'
import React, { useState, useEffect, useContext }from 'react';
import Cart from './components/cart';
import Totals from './components/totals';
import api from '../core/baseAPI';
import CartContext from './contexts/CartContext';
import { CartProvider } from './contexts/CartContext';

interface CartItemProps {
    product_id: number;
    product_name: string;
    product_company: string;
    product_price: string;
    quantity: number;
    preview_picture: string;
    url: string;
}

export default function ShoppingCart() {
    const { cart, setCart } = useContext(CartContext);

    useEffect(() => {
        api.get('shopping-list/details/')
            .then(response => {
                setCart(response.data);
            });
    }, []);

    return (
        cart.length !== 0 ?
        (
        <div>
            <h1>Shopping Cart</h1>
            <div 
                style={{
                    display: 'flex',
                    flexWrap: 'wrap',
                    justifyContent: 'space-evenly',
                    gap: '1rem',
                    paddingLeft: '10%',
                    paddingRight: '10%'
                }}>
                <div style={{flex: 2, maxWidth: '66.66%'}}>
                    <Cart />
                </div>
                <div style={{
                    flex: 1,
                    border: '1px solid white',
                    borderRadius: '10px',
                    padding: '1rem',
                    height: 'fit-content',
                    }}>
                    <Totals/>
                </div>
            </div>
        </div>) : (
            <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', width: '90vw', height: 'calc(100vh - 80px)'}}>
                <img src="/cart-empty.png" alt="cart" style={{maxWidth: '100%', maxHeight: '100%'}}/>
            </div>
        )
    );
};

export type { CartItemProps };