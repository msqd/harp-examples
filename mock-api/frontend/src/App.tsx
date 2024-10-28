import { useEffect, useState } from "react";
import { getProducts } from "./api/getProducts";
import ProductCatalog from "./ProducCatalog";
import { Product } from "./ProducCatalog";

function App() {
  const [products, setProducts] = useState<Product[] | undefined>();
  const [loading, setLoading] = useState<boolean>(true);
  const [retryCount, setRetryCount] = useState<number>(0);

  useEffect(() => {
    async function fetchProducts() {
      try {
        const productsData = await getProducts();
        if (productsData.length === 0 && retryCount < 3) {
          setRetryCount(retryCount + 1);
          setTimeout(fetchProducts, 1000);
        } else {
          setProducts(productsData);
          setLoading(false);
        }
      } catch (error) {
        if (retryCount < 3) {
          setRetryCount(retryCount + 1);
          setTimeout(fetchProducts, 1000);
        } else {
          console.error("Failed to fetch products after 3 retries:", error);
          setLoading(false);
        }
      }
    }

    fetchProducts();
  }, [retryCount]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return <ProductCatalog products={products} />;
}

export default App;
