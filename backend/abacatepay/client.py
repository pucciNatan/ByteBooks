import httpx
from django.conf import settings

class AbacatePayClient:
    def __init__(self):
        self.base = settings.ABACATEPAY["BASE_URL"]
        self.headers = {
            "Authorization": f"Bearer {settings.ABACATEPAY['TOKEN']}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    async def post(self, path: str, json: dict):
        async with httpx.AsyncClient(base_url=self.base, headers=self.headers, timeout=10) as client:
            r = await client.post(path, json=json)
            r.raise_for_status()
            return r.json()

    async def get(self, path: str, params: dict | None = None):
        async with httpx.AsyncClient(base_url=self.base, headers=self.headers, timeout=10) as client:
            r = await client.get(path, params=params)
            r.raise_for_status()
            return r.json()

client = AbacatePayClient()
