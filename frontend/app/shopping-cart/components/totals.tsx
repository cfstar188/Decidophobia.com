import React, { useState, useContext } from 'react';
import { Button } from '@mui/material';
import { Card, Box, Typography, List, ListItem, ListItemText } from '@mui/material';

import { CartItemProps } from './cartItem';
import PurchasedModal from './confirmModal';
import CartContext from '../contexts/CartContext';

export default function Totals() {
    const { cart } = useContext(CartContext);

    let total = 0;

    for (let i = 0; i < cart.length; i++) {
        total += parseFloat(cart[i].product_price) * cart[i].quantity;
    }

    
    return (
    <Card style={{ display: 'flex', width: '100%' }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
            <Box sx={{ maxHeight: '500px', overflow: 'auto' }}>
                <List>
                    {cart.map((item: CartItemProps, index: number) => (
                        <ListItem key={index}>
                            <ListItemText primary={`${item.product_name}........${item.quantity} x $${item.product_price}`} />
                        </ListItem>
                    ))}
                </List>
            </Box>
            <Typography variant="h6">
                Total: ${total.toFixed(2)}
            </Typography>
            <PurchasedModal />
        </Box>
    </Card>
    );
};
