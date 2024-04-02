
import React, { useState, useContext } from 'react';
import { Button, Box, Modal, List, ListItem, ListItemText, Typography, Checkbox, IconButton, Divider } from '@mui/material';
import { CloseButton } from 'reactstrap';
import Fade from '@mui/material/Fade';

import api from '@/app/core/baseAPI';
import CartContext from '../contexts/CartContext';
import Alerts from '@/app/components/alerts';

interface PurchasedModalProps {
    isOpen: boolean,
    onClose: () => void,
}

export default function PurchasedModal() {
    const [open, setOpen] = useState(false);
    const [checkedItems, setCheckedItems] = useState<number[]>([]);
    const { cart, setCart } = useContext(CartContext);
    const modalStyle = {
        position: 'absolute' as 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 600,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    };

    const toggle = () => setOpen(!open);

    const handleSubmit = (): void => {
        api.post('shopping-list/update-purchases/', {
            products: checkedItems}, {
                headers: {'Content-Type': 'application/json'}
            })
            .then((response) => {
                console.log('response', response);
                setCart((cart: any) => cart.filter((item: any) => !checkedItems.includes(item.product_id)));
                setOpen(false);
                
            })
    }

    return (
        <>
            <div>
                <Button variant="contained" color='primary' onClick={toggle}>
                    Checkout
                </Button>
            </div>
            <Modal
                open={open}
                onClose={toggle}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
                >
                <Fade in={open} timeout={500}>
                    <Box sx={modalStyle}>
                    <IconButton
                        aria-label="close"
                        onClick={toggle}
                        style={{ position: 'absolute', right: 0, top: 0 }}
                    >
                    </IconButton>
                        <Typography id="modal-modal-title" variant="h5" component="h2" style={{color: 'black'}}>
                            Please Select All Items That You Purchased
                        </Typography>
                        <Typography id="modal-modal-description" style={{color: 'black'}}>
                            This helps us provide you with better reccomendations!
                        </Typography>
                        <Divider />
                        <div style={{ maxHeight: '500px', overflow: 'auto', backgroundColor: '' }}>
                            <List>
                            {cart.map((item: any, index: any) => (
                                <ListItem disablePadding key={index}>
                                    <Checkbox
                                        onChange={(event) => {
                                            if (event.target.checked) {
                                                setCheckedItems(prevItems => [...prevItems, item.product_id]);
                                            } else {
                                                setCheckedItems(prevItems => prevItems.filter((id) => id !== item.product_id));
                                            }
                                            console.log('checkedItems', checkedItems)
                                        }}
                                    />
                                    <ListItemText style={{color: 'black'}} primary={`${item.product_name}-${item.product_company}`} />
                                </ListItem>
                            ))}
                            </List>
                        </div>
                        <Button variant="contained" color="primary" onClick={handleSubmit}>
                            Confirm
                        </Button>
                    </Box>
                </Fade>
            </Modal>
        </>
    )
}
