from dataclasses import dataclass
from model.checkout.order import Order, OrderStatus


@dataclass(frozen=True)
class Receipt:
    payment_id: str
    amount: float
    status: str


class Payment:

    def __init__(self, payment_id: str, order: Order):
        self._payment_id = payment_id
        self._order = order

    @property
    def payment_id(self) -> str:
        return self._payment_id

    @property
    def order(self) -> Order:
        return self._order

    def process(self) -> Receipt:
        if self._order.total_amount <= 0:
            raise ValueError("Valor do pedido inválido para pagamento.")

        # Transição automática de status do pedido para PAID
        self._order.advance_status(OrderStatus.PAID)

        return Receipt(
            payment_id=self._payment_id,
            amount=self._order.total_amount,
            status="SUCCESS",
        )