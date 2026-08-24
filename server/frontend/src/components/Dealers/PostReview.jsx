import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';

const PostReview = () => {
  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [selectedCarIndex, setSelectedCarIndex] = useState("");
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);

  const { id } = useParams();
  const navigate = useNavigate();

  const dealer_url = `/djangoapp/dealer/${id}`;
  const review_url = `/djangoapp/add_review`;
  const carmodels_url = `/djangoapp/get_cars`;

  const postreview = async () => {
    let firstname = sessionStorage.getItem("firstname");
    let lastname = sessionStorage.getItem("lastname");
    let username = sessionStorage.getItem("username");

    let name = `${firstname || ''} ${lastname || ''}`.trim();
    if (!name || name === "null null") {
      name = username || "Anonymous";
    }

    if (selectedCarIndex === "" || !review || !date || !year) {
      alert("All details are mandatory");
      return;
    }

    const chosenCar = carmodels[selectedCarIndex];

    const jsoninput = JSON.stringify({
      name: name,
      dealership: id,
      review: review,
      purchase: true,
      purchase_date: date,
      car_make: chosenCar.CarMake,
      car_model: chosenCar.CarModel,
      car_year: year,
    });

    try {
      const res = await fetch(review_url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: jsoninput,
      });

      const json = await res.json();
      if (json.status === 200 || res.ok) {
        navigate(`/dealer/${id}`);
      } else {
        alert("Failed to post review.");
      }
    } catch (err) {
      console.error("Error posting review:", err);
    }
  };

  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url, { method: "GET" });
      const retobj = await res.json();
      if (retobj.status === 200 && retobj.dealer) {
        let dealerObj = Array.isArray(retobj.dealer) ? retobj.dealer[0] : retobj.dealer;
        setDealer(dealerObj);
      }
    } catch (err) {
      console.error("Error fetching dealer:", err);
    }
  };

  const get_cars = async () => {
    try {
      const res = await fetch(carmodels_url, { method: "GET" });
      const retobj = await res.json();
      if (retobj.CarModels) {
        setCarmodels(Array.from(retobj.CarModels));
      }
    } catch (err) {
      console.error("Error fetching car models:", err);
    }
  };

  useEffect(() => {
    get_dealer();
    get_cars();
  }, [id]);

  return (
    <div>
      <Header />
      <div style={{ margin: "5%" }}>
        <h1 style={{ color: "darkblue" }}>{dealer.full_name}</h1>
        <textarea
          id='review'
          cols='50'
          rows='7'
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
       
        <div className='input_field'>
          Purchase Date{" "}
          <input type="date" onChange={(e) => setDate(e.target.value)} />
        </div>

        <div className='input_field'>
          Car Make & Model{" "}
          <select
            name="cars"
            id="cars"
            value={selectedCarIndex}
            onChange={(e) => setSelectedCarIndex(e.target.value)}
          >
            <option value="" disabled hidden>Choose Car Make and Model</option>
            {carmodels.map((carmodel, idx) => (
              <option key={idx} value={idx}>
                {carmodel.CarMake} {carmodel.CarModel}
              </option>
            ))}
          </select>
        </div>

        <div className='input_field'>
          Car Year{" "}
          <input
            type="number"
            onChange={(e) => setYear(e.target.value)}
            max={2026}
            min={2015}
          />
        </div>

        <div>
          <button className='postreview' onClick={postreview}>
            Post Review
          </button>
        </div>
      </div>
    </div>
  );
};

export default PostReview;
