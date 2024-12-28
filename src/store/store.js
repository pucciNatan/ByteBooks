import { createStore } from 'vuex'
import { fetchUltimosLancamentos, fetchMaisVendidos, fetchTodosCombos, fetchPesquisar, fetchRotaProtegida, fetchDetalhesLivro, fetchDetalhesCombo } from '../api/apiService.js'
import axios from 'axios'

export default createStore({
  state: {
    ultimosLancamentosLoja: [],
    maisVendidos: [],
    todosCombos: [],
    livrosPesquisados: [],
    detalhesLivro: [],
    detalhesCombo: [],
    token: '',
    nomeUsuario: ''
  },
  getters: {
    getStateUltimosLancamentosLoja(state) {
      return state.ultimosLancamentosLoja
    },
    getStateMaisVendidos(state) {
      return state.maisVendidos
    },
    getTodosCombos(state){
      return state.todosCombos
    },
    getLivrosPesquisados(state){
      return state.livrosPesquisados
    },
    getToken(state){
      return state.token
    },
    getNomeUsuario(state) {
      return state.nomeUsuario
    },
    getDetalhesLivro(state){
      return state.detalhesLivro
    },
    getDetalhesCombo(state){
      return state.detalhesCombo
    }
  },
  mutations: {
    setLivrosUltimosLancamentosLoja(state, livros) {
      state.ultimosLancamentosLoja = livros
    },
    setLivrosMaisVendidos(state, livros) {
      state.maisVendidos = livros
    },
    setTodosCombos(state, combos) {
      state.todosCombos = combos
    },
    setPesquisarPorLivro(state, livros){
      state.livrosPesquisados = livros
    },
    setToken(state, token){
      state.token = token
      localStorage.setItem('token', token)
    },
    setNomeUsuario(state, name) {
      state.nomeUsuario = name
      localStorage.setItem('nomeUsuario', name)
    },
    setDetalhesLivro(state, detalhes){
      state.detalhesLivro = detalhes
    },
    setDetalhesCombo(state, detalhes){
      state.detalhesCombo = detalhes
    }
  },
  actions: {
    async buscarUltimosLancamentosLoja({ commit }) {
      try {
        const res = await fetchUltimosLancamentos()
        commit('setLivrosUltimosLancamentosLoja', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async buscarMaisVendidos({ commit }) {
      try {
        const res = await fetchMaisVendidos()
        commit('setLivrosMaisVendidos', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async buscarTodosCombos({ commit }){
      try {
        const res = await fetchTodosCombos()
        commit('setTodosCombos', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async pesquisarPorLivro({ commit }, pesquisa){
      try{
        const res = await fetchPesquisar(pesquisa)
        commit('setPesquisarPorLivro', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
        commit('setPesquisarPorLivro', []);
      }
    },
    async logarUsuario({ commit }, dados){
    try{
      const res = await axios.post(
        'http://127.0.0.1:8000/api/clientes/login/', dados,
        { headers: { 'Content-Type': 'application/json' } }
      );
      commit('setNomeUsuario', res.data.nomeUsuario)
      commit('setToken', res.data.token)
    } catch (error) {
      if (error.response && (error.response.status === 400 || error.response.status === 401)) {
        throw new Error('Email/Username ou senha incorretos.');
      } else {
        throw new Error('Ocorreu um erro ao fazer login.');
      }
    }},
    carregarTokenDoStorage({ commit }) {
      const token = localStorage.getItem('token')
      if (token) {
        commit('setToken', token)
      }
    },
    carregarNomeStorage({ commit }) {
      const nomeUsuario = localStorage.getItem('nomeUsuario')
      if (nomeUsuario) {
        commit('setNomeUsuario', nomeUsuario)
      }
    },
    async visitaRotaProtegida(){
      try{
        const res = await fetchRotaProtegida()
        console.log(res.data.msg)
      }catch (error){
        localStorage.setItem('token', '')
        localStorage.setItem('nomeUsuario', '')
        window.location.replace('/login')
      }
    },
    async carregarDetalhesLivro({ commit }, idLivro){
      try{
        const res = await fetchDetalhesLivro(idLivro)
        commit('setDetalhesLivro', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async carregarDetalhesCombo({ commit }, idCombo){
      try{
        const res = await fetchDetalhesCombo(idCombo)
        commit('setDetalhesCombo', res.data)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    }
  }
})
