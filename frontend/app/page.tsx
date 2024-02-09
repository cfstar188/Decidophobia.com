// Table.tsx
"use client";
import React, { useState } from "react";
import { PictureComp } from "./components/PictureComp";
import SearchTable from "./components/SearchTable";

export type User = {
  price: string;
  id: number;
  product: string;
  company: string;
  picture: any;
  url: any;
};

const users: User[] = [
  {
    picture:
      "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-compare-iphone-15-202309?wid=384&hei=512&fmt=jpeg&qlt=90&.v=1692827832423",
    id: 0,
    product: "Iphone",
    company: "Apple",
    price: "1200.0",
    url: (
      <a href="https://www.apple.com/ca/shop/buy-iphone/iphone-15-pro">apple</a>
    ),
  },
  {
    picture:
      "https://img.us.news.samsung.com/us/wp-content/uploads/2023/03/14140259/samsung-galaxy-a54-5g-featured.png",
    id: 1,
    product: "Galaxy",
    company: "Samsung",
    price: "1000.0",
    url: (
      <a href="https://www.samsung.com/ca/smartphones/galaxy-s24-ultra/buy/?modelCode=SM-S928WZTFXAC">
        samsung
      </a>
    ),
  },
];

export default function SearchPage() {
  const [user, setUser] = useState<User[]>(users);

  const deleteUser = (userId: number) => {
    setUser(users.filter((user) => user.id !== userId));
  };

  const keys = users.length > 0 ? Object.keys(users[0]) : [];

  return (
    <>
      <SearchTable />
    </>
  );
}
