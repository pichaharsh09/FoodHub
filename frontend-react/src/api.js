const API_URL = "http://127.0.0.1:8000";

export async function getRestaurantFoods(restaurantId) {
  const response = await fetch(
    `${API_URL}/restaurants/${restaurantId}/foods`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch foods");
  }

  return response.json();
}