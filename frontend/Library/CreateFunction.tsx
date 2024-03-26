import { Product } from "./Type";

export function createProduct(
  image: string = "",
  product: string = "",
  price: number,
  currency: string = "",
  score: string,
  url: string = "",
  id: number
): Product {
  const returnProduct: Product = {
    picture: image,
    name: product,
    price: price,
    currency: currency,
    score: score,
    id: id,
    company: "",
    link: url,
  };

  return returnProduct;
}
