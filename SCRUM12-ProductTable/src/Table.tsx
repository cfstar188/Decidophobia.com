// Table.tsx
import React, { useState } from "react";
import { CircularXButton } from "./setTable";
import { PictureComp } from "./PictureComp";

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

function TableComp() {
  const [user, setUser] = useState<User[]>(users);

  const deleteUser = (userId: number) => {
    setUser(users.filter((user) => user.id !== userId));
  };

  const keys = users.length > 0 ? Object.keys(users[0]) : [];

  return (
    <>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <tbody>
          {keys.map((key, index) => (
            <tr key={key}>
              <th
                style={{
                  padding: "8px",
                  backgroundColor: "#f5f5f5",
                  textAlign: "left",
                }}
              >
                {index === 1 ? <div /> : key.toUpperCase()}
              </th>
              {user.map((user: any, index) => (
                <td
                  key={index}
                  style={{ padding: "8px", borderBottom: "1px solid #ddd" }}
                >
                  {typeof user[key] == typeof 1 ? (
                    <PictureComp
                      id={user[key]}
                      setData={deleteUser}
                      src={user.picture}
                    />
                  ) : (
                    user[key]
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}

export default TableComp;
