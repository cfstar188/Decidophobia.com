// localhost:3000/order-history/

'use client'
import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardMedia, Button, Box, Modal, List, ListItem, ListItemText, Typography, Checkbox, IconButton, Divider, CardHeader } from '@mui/material';
import Link from '@mui/material/Link';

import api from "../core/baseAPI";

export default function OrderHistory() {
    const [orderHistory, setOrderHistory] = useState([]);

    useEffect(() => {
        api.get('accounts/purchase-history/')
            .then(response => {
                setOrderHistory(response.data.purchases);
            })
    }, []);

    useEffect(() => {
        console.log('orderHistory', orderHistory);
    }, [orderHistory]);
    return (
        <div>
            <h1>Order History</h1>
            <div
                style={{display: 'flex',
                        flexWrap: 'wrap',
                        gap: '1.5rem',
                        paddingLeft: '10%',
                        paddingRight: '10%',
                        justifyContent: 'center'}}>
                {orderHistory.map((order: any, index) => {
                    const itemTotal = order.quantity * order.product_price
                    console.log('itemTotal', itemTotal)
                    return (
                        <div key={index} style={{width: 'max-content'}}>
                            <Card sx={{ display: 'flex', width: '440px' }}>
                                <Box sx={{ display: 'flex', flexDirection: 'column', maxWidth: '100%' }}>
                                    <Box sx={{display: 'flex'}}>
                                        <Box sx={{display: 'flex'}}>
                                            <CardHeader
                                                sx={{width: 'fit-content', height: 'min-content'}}
                                                title="Order Placed"
                                                subheader={order.date}
                                                titleTypographyProps={{ fontSize: '1rem'}}
                                                subheaderTypographyProps={{ fontSize: '0.85rem' }}/>
                                            <CardHeader
                                                sx={{width: 'fit-content', height: 'min-content'}}
                                                title="Total"
                                                subheader={`$${itemTotal.toFixed(2)}`}
                                                titleTypographyProps={{ fontSize: '1rem'}}
                                                subheaderTypographyProps={{ fontSize: '0.85rem' }}/>
                                        </Box>
                                        <Box sx={{display: 'flex', flexGrow: 1, justifyContent: 'flex-end' }}>
                                            <CardHeader
                                                sx={{width: 'fit-content', height: 'min-content'}}
                                                title="Order Number"
                                                subheader={order.order_id}
                                                titleTypographyProps={{ fontSize: '1rem'}}
                                                subheaderTypographyProps={{ fontSize: '0.85rem' }}/>
                                        </Box>
                                    </Box>
                                    <Divider />
                                    <CardContent sx={{ flex: '1 0 auto' }}>
                                        <Box sx={{display: 'flex'}}>
                                            <CardMedia
                                                component="img"
                                                sx={{ width: 100, objectFit: 'contain' }}
                                                src={order.preview_picture ? order.preview_picture : "/no_product_image.png"}
                                            />
                                            <Box sx={{display: 'flex', flexDirection: 'column', gap: '0.5rem', pl: 1, maxWidth: 'fit-content'}}>
                                                <Typography
                                                    variant="subtitle1"
                                                    color="text.secondary"
                                                    component="div">
                                                    {`${order.product} ${(order.company != '') ? `-${order.company}` : ''}`}
                                                </Typography>
                                                <Button variant="contained" color="primary" href={order.url ? order.url : 'https://www.google.com/'} target='_blank'>Buy Again</Button>
                                            </Box>
                                        </Box>
                                    </CardContent>
                                </Box>
                            </Card>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}