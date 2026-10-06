const API_URL = "http://127.0.0.1:8000";

let cart = [];


// =========================
// Load Restaurants
// =========================

async function loadRestaurants() {
    try {
        const response = await fetch(`${API_URL}/restaurants`);

        if (!response.ok) {
            throw new Error("Failed to fetch restaurants");
        }

        const restaurants = await response.json();

        const restaurantList = document.getElementById("restaurant-list");

        restaurantList.innerHTML = "";

        restaurants.forEach(restaurant => {

            const card = document.createElement("div");

            card.className = "card";

            card.innerHTML = `
                <h3>${restaurant.name}</h3>
                <p>Restaurant ID: ${restaurant.id}</p>

                <button onclick="viewRestaurant(${restaurant.id})">
                    View Menu
                </button>
            `;

            restaurantList.appendChild(card);
        });

    } catch (error) {
        console.error("Error loading restaurants:", error);
    }
}


// =========================
// View Restaurant Menu
// =========================

async function viewRestaurant(restaurantId) {

    try {

        const response = await fetch(
            `${API_URL}/restaurants/${restaurantId}/foods`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch foods");
        }

        const foods = await response.json();

        console.log("Foods received:", foods);

        const menuList = document.getElementById("menu-list");

        menuList.innerHTML = "";

        foods.forEach(food => {

            const card = document.createElement("div");

            card.className = "card";

            card.innerHTML = `
                <h3>${food.name}</h3>

                <p>Price: ₹${food.price}</p>

                <button onclick="addToCart(${food.id}, '${food.name}', ${food.price})">
                    Add to Cart
                </button>
            `;

            menuList.appendChild(card);
        });

    } catch (error) {

        console.error("Error loading menu:", error);

    }
}


// =========================
// Add Food To Cart
// =========================

function addToCart(id, name, price) {

    const food = {
        id: id,
        name: name,
        price: price
    };

    cart.push(food);

    console.log("Cart:", cart);

    displayCart();
}

// =========================
// Display to  Cart
// =========================
function displayCart() {

    const cartList = document.getElementById("cart-list");

    const cartTotal = document.getElementById("cart-total");

    cartList.innerHTML = "";

    let total = 0;

    cart.forEach((food, index) => {

        total += food.price;

        const item = document.createElement("div");

        item.className = "card";

        item.innerHTML = `
            <h3>${food.name}</h3>
            <p>Price: ₹${food.price}</p>

            <button onclick="removeFromCart(${index})">
                Remove
            </button>
        `;

        cartList.appendChild(item);
    });

    cartTotal.textContent = `Total: ₹${total}`;
}

function removeFromCart(index) {

    cart.splice(index, 1);

    displayCart();
}


// =========================
// Start Application
// =========================

loadRestaurants();