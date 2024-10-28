export async function getProducts() {
  const response = await fetch("/api/products"); // Replace with your actual API URL
  if (!response.ok) {
    throw new Error("Failed to fetch products");
  }
  const data = await response.json();
  return data;
}
