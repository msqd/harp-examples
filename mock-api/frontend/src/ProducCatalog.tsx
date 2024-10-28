import "./App.css";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  image: string;
}

function ProductCatalog({ products }: { products: Product[] | undefined }) {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Product Catalog</h1>
      {products && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {products.map(product => (
            <Card key={product.id} className="flex flex-col">
              <CardHeader>
                <img
                  src={product.image}
                  alt={product.name}
                  width={200}
                  height={200}
                  className="w-full h-48 object-cover rounded-t-lg"
                />
              </CardHeader>
              <CardContent className="flex-grow">
                <CardTitle className="text-xl mb-2">{product.name}</CardTitle>
                <Badge variant="secondary" className="mb-2">
                  {product.category}
                </Badge>
                <p className="text-muted-foreground">
                  ${product.price.toFixed(2)}
                </p>
              </CardContent>
              <CardFooter>
                <button className="w-full bg-primary text-primary-foreground hover:bg-primary/90 py-2 rounded-md transition-colors">
                  Add to Cart
                </button>
              </CardFooter>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}

export default ProductCatalog;
