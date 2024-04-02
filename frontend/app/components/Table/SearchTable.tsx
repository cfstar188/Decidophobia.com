"use client";
import React, { useEffect, useState, useContext } from "react";
import { useAtom } from "jotai";
import SquareCheckbox from "@/app/components/Button/ItemCheckBox";
import { allProductAtom } from "@/Library/SelectedAtom";
import api from "../../core/baseAPI";
import Alerts from "../alerts";
// import { authAtom } from "@/Library/AuthAtom";
import AuthContext from "@/app/contexts/AuthContext";
import { Product } from "@/Library/Type";

function truncateString(str: string, num: number) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

export function SearchTable() {
  const { auth } = useContext(AuthContext);
  const [products] = useAtom(allProductAtom);

  // I have set the buy button to this state, but I think you might need a state that updates inside a useeffect that calls your api.
  // This is just I thought since I have been doing a lot of react learning for this project. So you might know a better way.
  const [buy, setBuyState] = useState(0);
  const [notLoggedInAlertOpen, setNotLoggedInAlert] = useState(false);
  const [showAddedToCartAlert, setShowAddedToCartAlert] = useState(false);
  const [itemAlreadyInCartAlert, setitemAlreadyInCartAlert] = useState(false);

  useEffect(() => {}, [products]);

  function handleBuy(product: Product) {
    console.log("auth", auth);
    if (!auth.isAuthenticated) {
      setNotLoggedInAlert(true);
    } else {
      console.log("product", product);
      api
        .post(
          "/products/create-product/",
          {
            name: product.name,
            company: product.company,
            price: product.price,
            preview_picture: product.picture,
            url: product.link,
          },
          {
            headers: {
              Key: "decidophobiaAdmin",
            },
          }
        )
        .then((response) => {
          console.log(response.data.id);
          api
            .post("/shopping-list/add-item/", {
              product_id: response.data.id,
              quantity: 1,
            })
            .then((response) => {
              setBuyState(1);
              setShowAddedToCartAlert(true);
            })
            .catch((error) => {
              setitemAlreadyInCartAlert(true);
            });
        });
    }
  }

  return (
    <div
      style={{ paddingLeft: "10%", paddingRight: "10%", paddingBottom: "10%" }}
    >
      <div className="grid grid-cols-4 min-w-[500px] gap-4 p-4">
        {products.map((product: Product, index) => (
          <div
            key={index}
            className="border border-foreground rounded-lg py-4 px-10 flex flex-col items-center justify-between"
          >
            <div className="grid-cols-2 gird-rows-auto w-full">
              <img
                src={product.picture}
                alt={product.picture}
                className="max-w-full max-h-[200px] object-contain col-span-2 m-auto"
              />
              <div />
              <div className="py-3">
                <div className="line-clamp-3 overflow-hidden">
                  {truncateString(product.name, 100)}
                </div>
                <div className="col-span-2">{product.company}</div>
                <div className="col-span-1">Price: {product.price}</div>
                <div className="col-span-1">Score: {product.score}</div>
                <div>
                  <SquareCheckbox id={index} label="Compare" />
                  {auth.isAuthenticated === false ? (
                    <button
                      className="bg-slate-700 text-slate-500 p-1 rounded-xl"
                      onClick={(e: any) => {
                        console.log("is auth", auth.isAuthenticated);
                        handleBuy(product);
                      }}
                    >
                      Add to Cart!
                    </button>
                  ) : (
                    <button
                      className="bg-secondary p-1 rounded-xl"
                      onClick={(e: any) => {
                        handleBuy(product);
                      }}
                    >
                      Add to Cart!
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      <Alerts
        message="Login to add to cart!"
        severity="error"
        isOpen={notLoggedInAlertOpen}
        onClose={() => setNotLoggedInAlert(false)}
      />
      <Alerts
        message="Added to cart!"
        severity="success"
        isOpen={showAddedToCartAlert}
        onClose={() => setShowAddedToCartAlert(false)}
      />
      <Alerts
        message="Product already in cart!"
        severity="error"
        isOpen={itemAlreadyInCartAlert}
        onClose={() => setitemAlreadyInCartAlert(false)}
      />
    </div>
  );
}

export default SearchTable;
