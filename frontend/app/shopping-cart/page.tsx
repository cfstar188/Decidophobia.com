// localhost:3000/search/

'use client'
import React, { useState }from 'react';
import Cart from './components/cart';
import Totals from './components/totals';

interface CartItemProps {
    product_id: number;
    product_name: string;
    product_company: string;
    product_price: string;
    quantity: number;
    preview_picture: string;
}

export default function ShoppingCartPage() {
    const [cart, setCart] = useState([
        {
            "product_id": 1,
            "product_name": "iMac",
            "product_company": "Apple",
            "product_price": "1099.99",
            "quantity": 4,
            "preview_picture": "https://www.bestbuy.ca/en-ca/product/apple-iphone-14-128gb-blue-unlocked/16472785"
        },
        {
            "product_id": 10,
            "product_name": "Apple Watch",
            "product_company": "Apple",
            "product_price": "399.99",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 12,
            "product_name": "Iphone",
            "product_company": "Apple",
            "product_price": "1200.00",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 11,
            "product_name": "iPad",
            "product_company": "Apple",
            "product_price": "1099.99",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 3,
            "product_name": "Galaxy",
            "product_company": "Samsung",
            "product_price": "1000.00",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 3,
            "product_name": "Galaxy",
            "product_company": "Samsung",
            "product_price": "1000.00",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 3,
            "product_name": "Galaxy",
            "product_company": "Samsung",
            "product_price": "1000.00",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 3,
            "product_name": "Galaxy",
            "product_company": "Samsung",
            "product_price": "1000.00",
            "quantity": 4,
            "preview_picture": ""
        },
        {
            "product_id": 3,
            "product_name": "Galaxy",
            "product_company": "Samsung",
            "product_price": "1000.00",
            "quantity": 4,
            "preview_picture": ""
        }
    ]);

    // useEffect(() => {
    //     api.get('shopping-list/details/')
    //         .then(response => {
    //             console.log(response.data);
    //             setCart(response.data);
    //         });
    // }, []);

    return (
        <div>
            <h1>Shopping Cart</h1>
            <div 
                style={{
                    display: 'flex',
                    flexWrap: 'wrap',
                    justifyContent: 'space-evenly',
                    gap: '1rem',
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