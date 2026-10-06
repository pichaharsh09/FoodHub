function FoodCard({ food, onAddToCart }) {
  const foodImages = {
    pizza:
      "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=900&q=85",

    burger:
      "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=900&q=85",

    biryani:
      "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?auto=format&fit=crop&w=900&q=85",

    noodles:
      "https://images.unsplash.com/photo-1552611052-33e04de081de?auto=format&fit=crop&w=900&q=85",
  };

  const getFoodImage = (name) => {
    const foodName = name.toLowerCase();

    if (foodName.includes("pizza")) {
      return foodImages.pizza;
    }

    if (foodName.includes("burger")) {
      return foodImages.burger;
    }

    if (
      foodName.includes("biryani") ||
      foodName.includes("rice")
    ) {
      return foodImages.biryani;
    }

    if (
      foodName.includes("noodle") ||
      foodName.includes("chinese")
    ) {
      return foodImages.noodles;
    }

    return foodImages.pizza;
  };

  return (
    <article className="food-card">

      {/* Food Image */}
      <div className="food-image">

        <img
          src={getFoodImage(food.name)}
          alt={food.name}
        />

        <button
          className="favorite"
          type="button"
        >
          ♡
        </button>

      </div>

      {/* Food Details */}
      <div className="food-info">

        <p className="restaurant-name">
          FoodHub Restaurant
        </p>

        <h3>
          {food.name}
        </h3>

        <div className="food-meta">
          <span>⭐ 4.8</span>
          <span>•</span>
          <span>
            Freshly prepared
          </span>
        </div>

        <div className="food-bottom">

          <span className="price">
            ₹{food.price}
          </span>

          <button
            className="add-btn"
            type="button"
            onClick={() => onAddToCart(food)}
          >
            + Add
          </button>

        </div>

      </div>

    </article>
  );
}

export default FoodCard;