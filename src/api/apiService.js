import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': ''
  }
});

export function fetchUltimosLancamentos(){
  return apiClient.get('livros/ultimosLancamentosLoja');
}

export function fetchMaisVendidos(){
  return apiClient.get('livros/maisVendidos/');
}

export function fetchPesquisar(pesquisaTexto){
  return apiClient.get('livros/livroPorPesquisa/' + pesquisaTexto);
}

export function fetchTodosCombos(){
  return apiClient.get('combos/todosCombos/');
}

