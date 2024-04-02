import React, { useState, createContext, useContext, useEffect }from 'react';

const CartContext = createContext();

export function CartProvider({children}) {
    const [cart, setCart] = useState([]);
    const [purchaseModalOpen, setPurchaseModalOpen] = useState(false);
    const [alertOpen, setAlertOpen] = useState(false);

    useEffect(() => {
    }, [cart]);

    const togglePurchaseModal = () => {
        setPurchaseModalOpen((prevState) => !prevState);
    }

    const toggleAlert = () => {
        setAlertOpen((prevState) => !prevState);
    }

    const addToCart = (product) => {
        setCart((prevState) => {
            return [
                ...prevState,
                product
            ]
        });
    }

    const updateItemQuantity = (productId, quantity) => {
        setCart((prevState) => {
            return prevState.map((product) => {
                if (product.product_id === productId) {
                    return {
                        ...product,
                        quantity: quantity
                    }
                }
                return product;
            });
        });
    }

    const removeFromCart = (productId) => {
        setCart((prevState) => {
            return prevState.filter((product) => product.product_id !== productId);;
        });
    }

    return (
        <CartContext.Provider value={{ cart, setCart, addToCart, removeFromCart, togglePurchaseModal, toggleAlert, updateItemQuantity }}>
            {children}
        </CartContext.Provider>
    )
}

export default CartContext;