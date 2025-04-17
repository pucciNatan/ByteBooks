from ninja import Router
from .schemas import CobrançaIn
from .client import client

abacatepay_router = Router()

@abacatepay_router.post("/v1/billing/create/", auth=None)  # se não exigir auth interna
async def criar_cobranca(request, payload: CobrançaIn):
    """Cria primeira cobrança AbacatePay e devolve dados essenciais."""
    body = payload.dict()
    data = await client.post("/v1/billing/create", body)  # endpoint oficial :contentReference[oaicite:1]{index=1}
    return {
        "billing_id": data["billing"]["id"],
        "status": data["billing"]["status"],
        "valor": f"R$ {data['billing']['amount']/100:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        "qr_code": data.get("qrCode"),
        "pix_copiaecola": data.get("payload"),
    }

@abacatepay_router.post("webhook", auth=None)
async def webhook(request):
    evento = await request.json()
    # verifique se devMode ou assinatura, depois trate:
    if evento.get("event") == "billing.paid":
        billing = evento["data"]["billing"]
        # atualizar pedido local → status pago
    return {"received": True}
