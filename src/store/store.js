import { createStore } from 'vuex'
import { fetchUltimosLancamentos, fetchMaisVendidos, fetchTodosCombos, fetchPesquisar } from '../api/apiService.js'

export default createStore({
  state: {
    ultimosLancamentosLoja: [],
    maisVendidos: [],
    todosCombos: [],
    livrosPesquisados: []
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
    }
  },
  actions: {
    async buscarUltimosLancamentosLoja({ commit }) {
      try {
        const res = await fetchUltimosLancamentos()
        commit('setLivrosUltimosLancamentosLoja', res.data)
      } catch (error) {
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async buscarMaisVendidos({ commit }) {
      try {
        const res = await fetchMaisVendidos()
        commit('setLivrosMaisVendidos', res.data)
      } catch (error) {
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async buscarTodosCombos({ commit }){
      try {
        const res = await fetchTodosCombos()
        commit('setTodosCombos', res.data)
      } catch (error) {
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async pesquisarPorLivro({ commit }, pesquisa){
      try{
        const res = await fetchPesquisar(pesquisa)
        commit('setPesquisarPorLivro', res.data)
      } catch (error) {
        console.error('Ocorreu um erro: ' + error)
      }
    }
  }
})
