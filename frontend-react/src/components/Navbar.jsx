function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">

        {/* Logo */}
        <a href="/" className="brand">
          <div className="brand-icon">F</div>
          <span>Food<span>Hub</span></span>
        </a>

        {/* Navigation */}
        <div className="nav-links">
          <a href="#home" className="active">
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

        {/* Actions */}
        <div className="nav-actions">

          <button className="nav-search">
            <span>⌕</span>
          </button>

          <button className="cart-button">
            <span>🛒</span>
            <span>Cart</span>
            <b>0</b>
          </button>

          <button className="login-button">
            Login
          </button>

        </div>

      </div>
    </nav>
  );
}

export default Navbar;