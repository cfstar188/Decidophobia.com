
import React, { useState } from 'react';
import { Button, Box, Modal, List, ListItem, ListItemText, Typography, Checkbox, IconButton, Divider } from '@mui/material';
import { CloseButton } from 'reactstrap';
import Fade from '@mui/material/Fade';

import api from '@/app/core/baseAPI';
import { CartItemProps } from './cartItem';


const PurchasedModal: React.FC<{cart: CartItemProps[]}> = ({ cart }) => {
    const [open, setOpen] = useState(false);
    const [checkedItems, setCheckedItems] = useState([]);

    const modalStyle = {
        position: 'absolute' as 'absolute',
        top: '30%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 600,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    };

    const toggle = () => setOpen(!open);

    const handleSubmit = () => {
        api.post('shopping-list/checkout/', cart);
        toggle();
    }

    return (
        <>
            <div>
                <Button variant="contained" color="primary" onClick={toggle}>
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
                        <CloseButton style={{color: 'black'}}/>
                    </IconButton>
                        <Typography id="modal-modal-title" variant="h5" component="h2" style={{color: 'black'}}>
                            Please Select All Items That You Purchased
                        </Typography>
                        <Typography id="modal-modal-description" style={{color: 'black'}}>
                            This helps us provide you with better reccomendations!
                        </Typography>
                        <Divider />
                        <List>
                        {cart.map((item, index) => (
                            <ListItem disablePadding>
                                <Checkbox
                                    onChange={(event) => {
                                        if (event.target.checked) {
                                            checkedItems.push(item.product_id);
                                            setCheckedItems(checkedItems);
                                        } else {
                                            setCheckedItems(checkedItems.filter((id) => id !== item.product_id));
                                        }
                                    }}
                                />
                                <ListItemText style={{color: 'black'}} primary={`${item.product_name}-${item.product_company}`} />
                            </ListItem>
                        ))}
                        </List>
                        <Button variant="contained" color="primary" onClick={toggle}>
                            Confirm
                        </Button>
                    </Box>
                </Fade>
            </Modal>
        </>
    )
}

export default PurchasedModal;