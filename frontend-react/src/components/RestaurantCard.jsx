function RestaurantCard({ restaurant }) {
  return (
    <article className="restaurant-card">

      <div className="restaurant-image">
        {restaurant.image || "🍽️"}
      </div>

      <div>
        <h3>{restaurant.name}</h3>

        <p>{restaurant.cuisine}</p>

        <span>
          ⭐ {restaurant.rating} • {restaurant.deliveryTime}
        </span>
      </div>

    </article>
  );
}

export default RestaurantCard;