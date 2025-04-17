from ninja import Schema, Field
from typing import List, Optional

class ProdutoIn(Schema):
    externalId: str
    name: str
    description: Optional[str] = None
    quantity: int = Field(gt=0)
    price: int = Field(gt=99)   # em centavos

class CobrançaIn(Schema):
    frequency: str = "ONE_TIME"
    methods: List[str] = ["PIX"]
    products: List[ProdutoIn]
    returnUrl: str
    completionUrl: str
    customerId: Optional[str] = None
