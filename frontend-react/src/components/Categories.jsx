function Categories({ activeCategory, setActiveCategory }) {
  const categories = [
    { name: "All", icon: "🍽️" },
    { name: "Pizza", icon: "🍕" },
    { name: "Burger", icon: "🍔" },
    { name: "Biryani", icon: "🍛" },
    { name: "Chinese", icon: "🍜" },
    { name: "Desserts", icon: "🍰" },
    { name: "Drinks", icon: "🥤" },
  ];

  return (
    <section className="categories-section">
      <div className="categories-container">

        <div className="section-header">
          <div>
            <p className="section-label">
              EXPLORE
            </p>

            <h2 className="section-title">
              What are you craving?
            </h2>
          </div>
        </div>

        <div className="categories">
          {categories.map((category) => (
            <button
              key={category.name}
              className={`category ${
                activeCategory === category.name ? "active" : ""
              }`}
              onClick={() => setActiveCategory(category.name)}
            >
              <span className="category-icon">
                {category.icon}
              </span>

              <span className="category-name">
                {category.name}
              </span>
            </button>
          ))}
        </div>

      </div>
    </section>
  );
}

export default Categories;