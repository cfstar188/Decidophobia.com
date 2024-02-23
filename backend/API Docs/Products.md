## Create Product
Method: POST \
Endpoint: BASE_URL/products/create-product/ \
This endpoint is used to create a new product. The request body should contain the following fields:
- name: The name of the product
- company: The company that produces the product
- price: The price of the product
- preview_picture: The URL of the product's preview picture (optional)

Example request body:
```json
{
    "name": "Product 1",
    "company": "Company 1",
    "price": 100.32,
    "preview_picture": "https://example.com/product1.jpg"
}
```
Authentication required: No \
**Include Key in headers**

Example response:
```json
{
    "id": 1,
    "created_at": "2024-02-23T00:56:39.157067Z",
    "updated_at": "2024-02-23T00:56:39.157067Z",
    "name": "Product 1",
    "price": 1099.99,
    "company": "Company 1",
    "preview_picture": "https://example.com/product1.jpg"
}
```
