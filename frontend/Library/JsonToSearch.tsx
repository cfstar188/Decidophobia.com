import { createProduct } from "./CreateFunction";

/**
 *
 * @param json The json read from directus. Currently read from data base but can be converted easily.
 * @returns: rowMapPrice -> Returns the all materials into an array
 */
export default function JsonToAtom(jsonList: any): any[] {
  let array: any[] = [];
  console.log(jsonList);
  const json: any = jsonList.products;
  for (let i: number = 0; i < json.length; i++) {
    const product: string = json[i].name;
    const price: number = Number(json[i].price);
    const currency: string = json[i].currency;
    const score: number = Number(json[i].score);
    const image: any = json[i].image;
    array.push(createProduct(product, price, currency, score, image));
  }
  console.log("array", array);
  return array;
}
