// localhost:3000/shopping-cart/

'use client'
import React, { useState, useEffect }from 'react';
import Cart from './components/cart';
import Totals from './components/totals';
import api from '../core/baseAPI';

interface CartItemProps {
    product_id: number;
    product_name: string;
    product_company: string;
    product_price: string;
    quantity: number;
    preview_picture: string;
    url: string;
}

export default function ShoppingCartPage() {
    const [cart, setCart] = useState([]);

    useEffect(() => {
        api.get('shopping-list/details/')
            .then(response => {
                setCart(response.data);
            });
    }, []);

    return (
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
                <div style={{flex: 2}}>
                    <Cart cart={cart}/>
                </div>
                <div style={{
                    flex: 1,
                    border: '1px solid white',
                    borderRadius: '10px',
                    padding: '1rem',
                    height: 'fit-content',
                    }}>
                    <Totals cart={cart}/>
                </div>
            </div>
        </div>
    );
};

export type { CartItemProps };