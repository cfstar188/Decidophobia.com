"use client";
import React, { useEffect, useState } from "react";
import { useAtom } from "jotai";
import HorizontalSelectBar from "@/app/components/HorizontalSelectBar";
import SquareCheckbox from "@/app/components/Button/SquareButton";
import { allProductAtom } from "@/Library/SelectedAtom";
import api from "../core/baseAPI";
import Alerts from "./alerts";
import { authAtom } from "@/Library/AuthAtom";

interface Product {
  name: string;
  company: string;
  price: number;
  picture: string;
  // other properties...
}

export function SearchTable() {
  const [auth] = useAtom(authAtom);
  const [products] = useAtom(allProductAtom);
  const [tester, setTester] = useState();
  // I have set the buy button to this state, but I think you might need a state that updates inside a useeffect that calls your api.
  // This is just I thought since I have been doing a lot of react learning for this project. So you might know a better way.
  const [buy, setBuyState] = useState(0);
  const [notLoggedInAlertOpen, setNotLoggedInAlert] = useState(false);
  const [showAddedToCartAlert, setShowAddedToCartAlert] = useState(false);
  const [itemAlreadyInCartAlert, setitemAlreadyInCartAlert] = useState(false);

  useEffect(() => {}, [products]);

  function handleBuy(product: Product) {
    console.log('auth', auth)
    if (!auth.isAuthenticated) {
      setNotLoggedInAlert(true);
    }
    else {
      api.post("/products/create-product/", {
        name: product.name,
        company: product.company,
        price: product.price,
        preview_picture: product.picture,
      }, {
        headers: {
          'Key': 'decidophobiaAdmin'
        }
      })
      .then((response) => {
        console.log(response.data.id);
        api.post("/shopping-list/add-item/", {
          product_id: response.data.id,
          quantity: 1,
        })
          .then((response) => {
            setBuyState(1);
            setShowAddedToCartAlert(true);
          })
          .catch((error) => {
            setitemAlreadyInCartAlert(true)
          });
      });
    }
  }

  return (
    <>
      <button
        className="bg-blue-700"
        onClick={(e: any) => {
          console.log(products);
        }}
      >
        CLICK ON ME
      </button>
      <div className="grid grid-cols-4 min-w-[500px] gap-4 p-4">
        {products.map((product: any, index) => (
          <div
            key={index}
            className="border border-gray-300 rounded-lg py-4 px-10 flex flex-col items-center justify-between"
          >
            <div className="grid-cols-2 gird-rows-auto w-full">
              <img
                src={product.image}
                alt={product.image}
                className="max-w-full max-h-[200px] object-contain col-span-2 m-auto"
              />
              <div />
              <div className="text-white col-span-2">{product.product}</div>
              <div className="text-white col-span-2">{product.company}</div>
              <div className="text-white col-span-1">Price: ${product.price}</div>
              <SquareCheckbox id={index} label="Compare" onChange={setTester} />
              <button
                className="bg-blue-700"
                onClick={(e: any) => {
                  handleBuy(product);
                }}
              >
                Add to Cart!
              </button>
            </div>
          </div>
        ))}
      </div>
      <Alerts message="Login to add to cart!" severity="error"
              isOpen={notLoggedInAlertOpen}
              onClose={() => setNotLoggedInAlert(false)} />
      <Alerts message="Added to cart!" severity="success"
              isOpen={showAddedToCartAlert}
              onClose={() => setShowAddedToCartAlert(false)} />
      <Alerts message="Product already in cart!" severity="error"
              isOpen={itemAlreadyInCartAlert}
              onClose={() => setitemAlreadyInCartAlert(false)} />
    </>
  );
}

export default SearchTable;
