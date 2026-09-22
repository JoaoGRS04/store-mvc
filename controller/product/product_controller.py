from model.product.pricing import PricingPolicy
from model.product.product import Price, Product, SKU
from model.product.product_category import ProductType
from view.product.product_view import ProductView


class ProductController:

    def __init__(self, view: ProductView):
        self._products: list[Product] = []
        self._view = view

    def add(self) -> Product:
        data = self._view.prompt_data()
        category_key = data.get("category", "").upper()
        category = (
            ProductType[category_key]
            if category_key in ProductType.__members__
            else None
        )

        product = Product(
            sku=SKU(data["sku"]),
            name=data["name"],
            price=Price(data["price"]),
            category=category,
        )
        self._products.append(product)
        self._view.show(product)
        return product

    def find(self, sku: str) -> Product | None:
        if not self._products:
            return None

        for p in self._products:
            p_sku = p.sku.code if hasattr(p.sku, "code") else str(p.sku)
            if p_sku == sku:
                self._view.show(p)
                return p
        return None

    def apply_policy(self, sku: str, policy: PricingPolicy) -> None:
        product = self.find(sku)
        if product:
            product.policy = policy

    def prompt_choice(self) -> Product | None:
        if not self._products:
            return None
        self._view.show_table(self._products)
        index = self._view.prompt_index(len(self._products))
        return self._products[index]