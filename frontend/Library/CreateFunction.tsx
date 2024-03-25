export function createProduct(
  product: string = "",
  price: number,
  currency: string = "",
  score: number,
  image: string = ""
): any {
  return { product, price, currency, score, image };
}
