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
    const name: string = json[i].name;
    const price: number = Number(json[i].price);
    const currency: string = json[i].currency;
    const score: string = json[i].score;
    const image: any = json[i].image;
    array.push(createProduct(image, name, price, currency, score, i));
  }

  return array;
}
