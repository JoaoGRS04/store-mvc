from enum import Enum
from model.checkout.cart import Cart


class OrderStatus(Enum):
    PENDING = "Pendente"
    PAID = "Pago"
    IN_FULFILLMENT = "Em Processamento"
    SHIPPED = "Enviado"
    CANCELLED = "Cancelado"


class Order:

    def __init__(self, order_id: str, cart: Cart, customer_id: str):
        if not cart.items:
            raise ValueError("O carrinho está vazio.")
        self._order_id = order_id
        self._items = list(cart.items)
        self._total_amount = cart.total()
        self._customer_id = customer_id
        self._status = OrderStatus.PENDING

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def items(self) -> list:
        return self._items

    @property
    def total_amount(self) -> float:
        return self._total_amount

    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def status(self) -> OrderStatus:
        return self._status

    def advance_status(self, new_status: OrderStatus):
        self._status = new_status

    def __str__(self):
        return f"Order[{self._order_id}] - Customer: {self._customer_id} | Total: R$ {self._total_amount:.2f} | Status: {self._status.value}"