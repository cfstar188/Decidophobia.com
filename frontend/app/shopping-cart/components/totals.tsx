import React from 'react';
import { CartItemProps } from './cartItem';

const Totals: React.FC<{cart: CartItemProps[]}> = ({ cart }) => {
    let total = 0;

    for (let i = 0; i < cart.length; i++) {
        total += parseFloat(cart[i].product_price) * cart[i].quantity;
    }

    
    return (
        <div
        style={{
            // display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginTop: '1rem',
        }}
        >
        <ul>
            {cart.map((item, index) => (
            <li key={index}>
                {item.product_name}........................{item.quantity} x ${item.product_price}
            </li>
            ))}
        </ul>
        <div>
            <h4>Total:</h4>
            <h4>${total.toFixed(2)}</h4>
        </div>
        </div>
    );
};

export default Totals;