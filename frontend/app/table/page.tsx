// localhost:3000/table/
"use client";
import React, { useState } from "react";
import { PictureComp } from "@/app/components/PictureComp";
import { allProductAtom } from "@/Library/SelectedAtom";
import { useAtom } from "jotai";

export function TableComp() {
  const [user, setUser] = useAtom(allProductAtom);
  const [deleted, setDeleteUser] = useState<number[]>([]);

  const deleteUser = (userId: number) => {
    setDeleteUser((deleted) => [...deleted, userId]);
    setUser((user) => user.filter((newuser) => !deleted.includes(newuser.id)));
  };

  const keys = user.length > 0 ? Object.keys(user[0]) : [];

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
                  ) : key === "picture" ? (
                    <></>
                  ) : (
                    <div className="text-white">{user[key]}</div>
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
