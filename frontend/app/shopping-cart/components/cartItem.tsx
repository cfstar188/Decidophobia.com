import React from 'react';
import { Card, CardBody, CardTitle, CardSubtitle, CardText, Button } from 'reactstrap';

import { CartItemProps } from '../page';

const CartItem: React.FC<{item: CartItemProps}> = ({ item }) => {
  return (
    <Card
      style={{
        width: '15rem',
        border: '1px solid white',
        borderRadius: '10px',
      }}
    >
      <img
        alt="Sample"
        src="https://picsum.photos/300/200"
        style={{borderRadius: '10px 10px 0 0'}}
      />
      <CardBody style={{padding: '0.5rem'}}>
        <CardTitle tag="h5">
          ${item.product_price}
        </CardTitle>
        <CardSubtitle
          className="mb-2 text-muted"
          tag="h6"
        >
          {item.product_name} - {item.product_company}
        </CardSubtitle>
        <div style={{
          display: 'flex',
          justifyContent: 'space-evenly',
          alignItems: 'center',
        }}>
          <Button
            style={{
              backgroundColor: 'rgba(255, 0, 0, 0.4)', // red with 50% opacity
              borderColor: 'rgba(255, 0, 0, 0.5)', // red with 50% opacity
              color: 'white',
              borderRadius: '5px',
              padding: '10px 20px',
              fontSize: '15px',
              fontWeight: 'bold',
              cursor: 'pointer'
            }}
          >
            +
          </Button>
          <CardText>
            Quantity: {item.quantity}
          </CardText>
          <Button
            style={{
              backgroundColor: '#007bff',
              borderColor: '#007bff',
              color: 'white',
              borderRadius: '5px',
              padding: '10px 20px',
              fontSize: '15px',
              fontWeight: 'bold',
              cursor: 'pointer'
            }}
          >
            -
          </Button>
        </div>
      </CardBody>
    </Card>
  );
}

export default CartItem;
export type { CartItemProps };