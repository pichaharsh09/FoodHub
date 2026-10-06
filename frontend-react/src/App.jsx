import { useEffect, useState } from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Categories from "./components/Categories";
import FoodCard from "./components/FoodCard";
import RestaurantCard from "./components/RestaurantCard";

import { getRestaurantFoods } from "./api";

import "./App.css";

function App() {
  // =========================
  // STATE
  // =========================

  const [activeCategory, setActiveCategory] = useState("All");

  const [foods, setFoods] = useState([]);

  const [cart, setCart] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");


  // =========================
  // FETCH FOODS FROM FASTAPI
  // =========================

  useEffect(() => {
    async function loadFoods() {
      try {
        setLoading(true);
        setError("");

        const data = await getRestaurantFoods(1);

        setFoods(data);
      } catch (err) {
        console.error("Food API Error:", err);

        setError(
          "Unable to load food data. Make sure your FastAPI server is running."
        );
      } finally {
        setLoading(false);
      }
    }

    loadFoods();
  }, []);


  // =========================
  // CATEGORY FILTER
  // =========================

 const getFoodCategory = (foodName) => {
  const name = foodName.toLowerCase();

  if (name.includes("pizza")) {
    return "Pizza";
  }

  if (name.includes("burger")) {
    return "Burger";
  }

  if (name.includes("biryani")) {
    return "Biryani";
  }

  if (
    name.includes("noodle") ||
    name.includes("chinese")
  ) {
    return "Chinese";
  }

  if (
    name.includes("cake") ||
    name.includes("dessert") ||
    name.includes("ice cream")
  ) {
    return "Desserts";
  }

  if (
    name.includes("drink") ||
    name.includes("juice") ||
    name.includes("shake")
  ) {
    return "Drinks";
  }

  return "Other";
};

const filteredFoods =
  activeCategory === "All"
    ? foods
    : foods.filter(
        (food) =>
          food.category?.toLowerCase() ===
          activeCategory.toLowerCase()
      );


  // =========================
  // ADD TO CART
  // =========================

  const addToCart = (food) => {
    setCart((currentCart) => [
      ...currentCart,
      food,
    ]);

    console.log("Added to cart:", food);
  };


  // =========================
  // RESTAURANT DATA
  // =========================

  const restaurants = [
    {
      id: 1,
      name: "Food Hub Kitchen",
      cuisine: "Pizza • Italian • Fast Food",
      rating: "4.8",
      deliveryTime: "25 min",
      image: "🍕",
    },

    {
      id: 2,
      name: "Burger House",
      cuisine: "Burgers • Fast Food",
      rating: "4.7",
      deliveryTime: "20 min",
      image: "🍔",
    },

    {
      id: 3,
      name: "Biryani Express",
      cuisine: "Biryani • Indian",
      rating: "4.9",
      deliveryTime: "30 min",
      image: "🍛",
    },
  ];


  // =========================
  // UI
  // =========================

  return (
    <div className="app">

      {/* ================= NAVBAR ================= */}

      <Navbar />


      {/* ================= HERO ================= */}

      <Hero />


      {/* ================= CATEGORIES ================= */}

      <Categories
        activeCategory={activeCategory}
        setActiveCategory={setActiveCategory}
      />


      {/* ================= FOOD SECTION ================= */}

      <section
        className="section food-section"
        id="menu"
      >
        <div className="section-container">

          {/* Section Header */}

          <div className="section-header">

            <div>

              <p className="section-label">
                POPULAR TODAY
              </p>

              <h2 className="section-title">
                Popular dishes
              </h2>

            </div>

            <button
              className="view-all"
              type="button"
            >
              View all →
            </button>

          </div>


          {/* Loading */}

          {loading && (
            <div className="no-results">
              <h3>
                Loading food...
              </h3>

              <p>
                Fetching delicious dishes from FoodHub.
              </p>
            </div>
          )}


          {/* Error */}

          {!loading && error && (
            <div className="no-results">

              <h3>
                Something went wrong
              </h3>

              <p>
                {error}
              </p>

            </div>
          )}


          {/* Food Cards */}

          {!loading &&
            !error &&
            filteredFoods.length > 0 && (

              <div className="food-grid">

                {filteredFoods.map((food) => (

                  <FoodCard
                    key={food.id}
                    food={food}
                    onAddToCart={addToCart}
                  />

                ))}

              </div>

            )}


          {/* No Food */}

          {!loading &&
            !error &&
            filteredFoods.length === 0 && (

              <div className="no-results">

                <h3>
                  No food found
                </h3>

                <p>
                  Try selecting another category.
                </p>

              </div>

            )}

        </div>
      </section>


      {/* ================= RESTAURANTS ================= */}

      <section
        className="section restaurants-section"
        id="restaurants"
      >

        <div className="section-container">

          {/* Section Header */}

          <div className="section-header">

            <div>

              <p className="section-label">
                TOP PICKS
              </p>

              <h2 className="section-title">
                Popular restaurants
              </h2>

            </div>

            <button
              className="view-all"
              type="button"
            >
              Explore all →
            </button>

          </div>


          {/* Restaurant Cards */}

          <div className="restaurant-grid">

            {restaurants.map((restaurant) => (

              <RestaurantCard
                key={restaurant.id}
                restaurant={restaurant}
              />

            ))}

          </div>

        </div>

      </section>


      {/* ================= FOOTER ================= */}

      <footer className="footer">

        <div className="footer-container">

          {/* Brand */}

          <div>

            <div className="footer-brand">
              Food<span>Hub</span>
            </div>

            <p className="footer-description">
              Discover delicious food from your favorite
              restaurants and get it delivered straight to
              your door.
            </p>

          </div>


          {/* Company */}

          <div className="footer-column">

            <h4>
              FoodHub
            </h4>

            <a href="#home">
              Home
            </a>

            <a href="#restaurants">
              Restaurants
            </a>

            <a href="#menu">
              Menu
            </a>

            <a href="#about">
              About
            </a>

          </div>


          {/* Support */}

          <div className="footer-column">

            <h4>
              Support
            </h4>

            <a href="#help">
              Help Center
            </a>

            <a href="#contact">
              Contact Us
            </a>

            <a href="#privacy">
              Privacy
            </a>

            <a href="#terms">
              Terms
            </a>

          </div>


          {/* Account */}

          <div className="footer-column">

            <h4>
              Account
            </h4>

            <a href="#login">
              Login
            </a>

            <a href="#register">
              Register
            </a>

            <a href="#orders">
              My Orders
            </a>

            <a href="#cart">
              Cart
            </a>

          </div>

        </div>


        {/* Footer Bottom */}

        <div className="footer-bottom">

          © 2026 FoodHub. Built with React + FastAPI.

        </div>

      </footer>


    </div>
  );
}

export default App;