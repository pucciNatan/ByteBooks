from ninja import NinjaAPI
from livros.api.apiLivros import livros_router
from livros.api.apiCombo import combos_router
from clientes.api import clientes_router

api = NinjaAPI()

api.add_router('livros/', livros_router)
api.add_router('combos/', combos_router)
api.add_router('clientes/', clientes_router)