## Get Shopping List
Method: GET \
Endpoint: BASE_URL/shopping-list/details \
This endpoint is used to get the details of the shopping list. The response will contain the following fields:
```json
{
    {
        "product_id": 1,
        "product_name": "Product 1",
        "product_company": "Company 1",
        "product_price": 100,
        "quantity": 2

    },
    {
        "product_id": 2,
        "product_name": "Product 2",
        "product_company": "Company 2",
        "product_price": 200,
        "quantity": 3
    }
}
```
Authentication required: Yes


## Add Item
Method: POST \
Endpoint: BASE_URL/shopping-list/add-item/ \
This endpoint is used to add an item to the shopping list. The request body should contain the following fields:
- product_id: The ID of the product to add to the shopping list
- quantity: The quantity of the product to add to the shopping list

Example request body:
```json
{
    "product_id": 1,
    "quantity": 2
}
```
Authentication required: Yes

Example response:
```json
{
    "message": "Product has been added to your shopping cart.",
    "item": {
        "product_id": 1,
        "product_name": "Product 1",
        "product_company": "Company 1",
        "product_price": 100,
        "quantity": 2
    }
}
```

If product already exists in the shopping list, the quantity will be updated and the response will be:
```json
{
    ["Product already in shopping cart!"]

}
```

## Remove Item
Method: DELETE \
Endpoint: BASE_URL/shopping-list/remove-item/ \
This endpoint is used to remove an item from the shopping list. The request body should contain the following fields:
- product_id: The ID of the product to remove from the shopping list

Example request body:
```json
{
    "product_id": 1
}
```
Authentication required: Yes

Example response:
```json
{
    "message": "Removed item from list",
    "item": {
        "removed_id": 1,
        "removed_name": "Product 1",
        "quantity": 4
    }
}
```

## Update Item
Method: PUT \
Endpoint: BASE_URL/shopping-list/change-quantity/ \
This endpoint is used to update the quantity of an item in the shopping list. The request body should contain the following fields:
- product_id: The ID of the product to update
- quantity: The new quantity of the product

Example request body:
```json
{
    "product_id": 1,
    "quantity": 3
}
```
Authentication required: Yes
