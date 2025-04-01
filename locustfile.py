from locust import HttpUser, between, task
from time import sleep as slp

class User(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def login(self):
        self.client.get("http://127.0.0.1:8000/api/livros/todosLivrosDisponiveis")
        slp(5)

    @task(1)
    def perfil(self):
        self.client.get("http://127.0.0.1:8000/api/livros/ultimosLancamentosLoja")
        slp(1)