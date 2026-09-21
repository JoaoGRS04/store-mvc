from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SKU:
    code: str

    def __post_init__(self):
        if not self.code or not self.code.strip():
            raise ValueError("SKU não pode ser vazio.")


@dataclass
class Price:
    amount: float

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("O preço deve ser maior que zero.")


class Product:

    def __init__(
        self,
        sku: SKU,
        name: str,
        price: Price,
        category: Optional[str] = None,
        policy=None,
    ):
        self._sku = sku
        self._name = name
        self._price = price
        self._category = category
        self._policy = policy

    @property
    def sku(self) -> SKU:
        return self._sku

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> Price:
        return self._price

    @property
    def category(self):
        return self._category

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, p):
        self._policy = p

    def final_price(self) -> float:
        if self._policy and hasattr(self._policy, "factor"):
            return self._price.amount + self._policy.factor()
        return self._price.amount

    def __repr__(self):
        cat_name = (
            self._category.name
            if hasattr(self._category, "name")
            else self._category
        )
        return (
            f"Product(sku={self._sku!r}, name={self._name!r}, "
            f"price={self._price!r}, category={cat_name!r})"
        )

    def __str__(self):
        cat_name = (
            self._category.name
            if hasattr(self._category, "name")
            else self._category
        )
        return (
            f"[{self._sku.code}] {self._name} "
            f"({cat_name}) - R$ {self._price.amount:.2f} "
            f"\nFinal price: R$ {self.final_price():.2f}"
        )

    def __eq__(self, other):
        if isinstance(other, Product):
            return self._sku.code == other._sku.code
        return False