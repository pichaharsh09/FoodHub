function Hero() {
  return (
    <section className="hero" id="home">
      <div className="hero-container">

        {/* Left Content */}
        <div className="hero-content">

          <div className="hero-label">
            FRESH FOOD • FAST DELIVERY
          </div>

          <h1 className="hero-title">
            Good food.
            <br />
            <span>Good mood.</span>
          </h1>

          <p className="hero-description">
            Discover delicious food from the best restaurants around you.
            Order your favorites and get them delivered straight to your door.
          </p>

          {/* Search */}
          <div className="hero-search">
            <span className="hero-search-icon">⌕</span>

            <input
              type="text"
              placeholder="Search for food or restaurants..."
            />

            <button>
              Search
            </button>
          </div>

          {/* Stats */}
          <div className="hero-stats">

            <div className="stat">
              <strong>500+</strong>
              <span>Food options</span>
            </div>

            <div className="stat">
              <strong>100+</strong>
              <span>Restaurants</span>
            </div>

            <div className="stat">
              <strong>4.8</strong>
              <span>Average rating</span>
            </div>

          </div>

        </div>

        {/* Right Visual */}
        <div className="hero-visual">

          <div className="hero-food-circle">
            🍕
          </div>

          <div className="hero-floating-card hero-rating">
            ⭐ 4.8
            <small> Top rated</small>
          </div>

          <div className="hero-floating-card hero-delivery">
            🚀
            <span> Fast delivery</span>
          </div>

        </div>

      </div>
    </section>
  );
}

export default Hero;