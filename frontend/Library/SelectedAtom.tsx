import { atom } from "jotai";
import { Product } from "./Type";

const users: Product[] = [];

export const allProductAtom = atom(users);
export const selectedListAtom = atom<number[]>([]);
export const selectedProductAtom = atom((get) => {
  const allProducts = get(allProductAtom);
  const selectList = get(selectedListAtom);

  const returnList = allProducts.filter((_, index) =>
    selectList.includes(index)
  );

  return returnList;
});
export const prevSearchParams = atom("");
