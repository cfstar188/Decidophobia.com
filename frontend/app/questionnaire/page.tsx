import React from 'react';

const DecisionFactors = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const queryParams = new URLSearchParams();

    formData.forEach((value, key) => {
      queryParams.append(key, value);
    });

    const url = `/search?${queryParams.toString()}`;
    window.location.href = url;
  };

  return (
    <div className="popup">
      <h2>Tell us what is important to you</h2>
      <form id="preferencesForm" onSubmit={handleSubmit}>
        <input type="hidden" name="product_name" value="{product_name}" />
        <label htmlFor="priceFactor">Price:</label>
        <select id="priceFactor" name="priceFactor">
          <option value=">10000">Bill Gates</option>
          <option value="<=10000">Rich</option>
          <option value="<=3000">Average salary</option>
          <option value="<=1000">Survivor</option>
          <option value="<=500">Bankrupt</option>
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
        <button id="submit_button" type="submit">Submit</button>
      </form>
    </div>
  );
};

export default DecisionFactors;
