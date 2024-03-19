import { atom } from "jotai";
import { User } from "./Type";

const users: User[] = [
  {
    picture:
      "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-compare-iphone-15-202309?wid=384&hei=512&fmt=jpeg&qlt=90&.v=1692827832423",
    id: 0,
    name: "macbook",
    company: "Apple",
    price: 1200.00,
    url: (
      <a href="https://www.apple.com/ca/shop/buy-iphone/iphone-15-pro">apple</a>
    ),
  },
  {
    picture:
      "https://img.us.news.samsung.com/us/wp-content/uploads/2023/03/14140259/samsung-galaxy-a54-5g-featured.png",
    id: 1,
    name: "Galaxy",
    company: "Samsung",
    price: 1000.00,
    url: (
      <a href="https://www.samsung.com/ca/smartphones/galaxy-s24-ultra/buy/?modelCode=SM-S928WZTFXAC">
        samsung
      </a>
    ),
  },
  {
    picture:
      "https://img.us.news.samsung.com/us/wp-content/uploads/2023/03/14140259/samsung-galaxy-a54-5g-featured.png",
    id: 2,
    name: "Galaxy",
    company: "Samsung",
    price: 1000.32,
    url: (
      <a href="https://www.samsung.com/ca/smartphones/galaxy-s24-ultra/buy/?modelCode=SM-S928WZTFXAC">
        samsung
      </a>
    ),
  },
];

export const allProductAtom = atom(users);
export const selectedListAtom = atom<number[]>([]);
export const selectedProductAtom = atom(
  (get) => {
    const allProducts = get(allProductAtom);
    const selectList = get(selectedListAtom);

    const returnList: User[] = allProducts.filter((product) =>
      selectList.includes(product.id)
    );

    return returnList;
  },
  (get, set, newPrice) => {}
);
