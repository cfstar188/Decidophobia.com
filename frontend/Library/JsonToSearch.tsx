import { createProduct } from "./CreateFunction";

/**
 *
 * @param json The json read from directus. Currently read from data base but can be converted easily.
 * @returns: rowMapPrice -> Returns the all materials into an array
 */
export default function JsonToAtom(jsonList: any): any[] {
  let array: any[] = [];
  const json: any = jsonList.products;
  for (let i: number = 0; i < json.length; i++) {
    const name: string = json[i].name;
    const price: number = Number(json[i].price);
    const currency: string = json[i].currency;
    const score: string = json[i].metrics.normalized_value.toFixed(2);
    const image: any = json[i].image;
    const link: any = json[i].link;
    array.push(createProduct(image, name, price, currency, score, link, i));
  }

  return array;
}
