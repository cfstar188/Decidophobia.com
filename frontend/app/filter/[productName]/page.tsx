"use client"; // Add this line at the top of the file
import "./questionnaire.css";
import { useRouter, useSearchParams } from "next/navigation";
import React, { useEffect, useState, useRef} from 'react';

export default function DecisionFactors( {
  params,
}: {
  params: { productName: string }
}) {
  const router = useRouter();
  const form = useRef(null);
  const searchParams = useSearchParams();

  // const [productName, setProductName] = useState("");

  // useEffect(() => {
  // const { product_name } = router.query;
  //   if (params.productName) {
  //     setProductName(product_name);
  //   }
  // }, [router.query]);
  const handleSubmit = () => {
    const formElement = form.current;
    const submitEvent = new Event("submit", { cancelable: true, bubbles: true });
    formElement.dispatchEvent(submitEvent);
  };

  const handleForm = (e: any) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const queryParams = new URLSearchParams();
    // const searchQ = router.query.searchQ;
    // const productName = params.productName;

    formData.forEach((value, key) => {
      queryParams.append(key, value);
    });

    // console.log("params productName", searchParams.get("productName"));
    // console.log("params productName 2", params.productName);

    const url = (`/search?searchQ=${params.productName}&${queryParams.toString()}`);
    console.log("url", url);
    router.push(url);
  };

  return (
    <>
    {/* <NavBar /> */}
    <div className="popup">
      <h2>Tell us what is important to you</h2>
      <form ref={form} id="preferencesForm" onSubmit={handleForm}>
      {/* <input type="hidden" name="product_name" value={params.productName} /> */}
        <label htmlFor="priceFactor">Price:</label>
        <select id="priceFactor" name="priceFactor">
          <option value="10000">Bill Gates</option>
          <option value="1000">Rich</option>
          <option value="500">Average salary</option>
          <option value="100">Survivor</option>
          <option value="50">Bankrupt</option>
        </select>
        <label htmlFor="customerReview">Customer reviews:</label>
        <select id="customerReview" name="customerReview">
          <option value="5">5 stars</option>
          <option value="4">4 stars</option>
          <option value="3">3 stars</option>
          <option value="2">2 stars</option>
          <option value="1">1 stars</option>
        </select>
        <label htmlFor="shipping">Shipping and Delivery</label>
        <select id="shipping" name="shipping">
          <option value="Does not matter">Does not matter</option>
          <option value="A couple week">A couple week</option>
          <option value="A week or so">A week or so</option>
          <option value="Amazon speed">Amazon speed</option>
          <option value="Right now">Right now!!!</option>
        </select>
        <label htmlFor="returnPolicy">Return Policy</label>
        <select id="returnPolicy" name="returnPolicy">
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>
        <label htmlFor="brandReputation">Brand Reputation</label>
        <select id="brandReputation" name="brandReputation">
          <option value="Excellent">Excellent</option>
          <option value="Good">Good</option>
          <option value="Ok">Ok</option>
        </select>
        <button id="submit_button" type="submit" onClick={handleSubmit}>Submit</button>
      </form>
    </div>
    </>
  );
};
