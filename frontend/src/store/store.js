import { createStore } from 'vuex'
import { fetchUltimosLancamentos, fetchMaisVendidos, fetchTodosCombos, fetchPesquisar, fetchRotaProtegida, 
  fetchDetalhesLivro, fetchDetalhesCombo, fetchCarregarCarrinho, fetchAdicionarLivroAoCarrinho, 
  fetchRemoverLivroDoCarrinho, fetchAtualizarQuantidade, fetchComprarLivro, fetchGetCliente, 
  fetchLivroPorCategoria, atualizarInfos} from '../api/apiService.js'
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
    nomeUsuario: '',
    itensCarrinho: [],
    infosUsuario: {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      dataNascimento: '',
      livrosComprados: [],
    }, 
    corAvatar:''
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
    },
    getItensCarrinho(state){
      return state.itensCarrinho
    },
    getQtdCarrinho(state){
      return state.itensCarrinho.length
    },
    getInfosUsuario(state){
      return state.infosUsuario
    },
    getLivrosComprados(state){
      return state.infosUsuario.livrosComprados
    },
    getCorAvatar(state){
      return state.corAvatar
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
    },
    setItensCarrinho(state, itens){
      state.itensCarrinho = itens
    },
    setInfosUsuario(state, infosUsuario){
      state.infosUsuario = infosUsuario
    },
    setCorAvatar(state, corAvatar){
      state.corAvatar = corAvatar
    },
    limparLivrosPesquisados(state) {
      state.livrosPesquisados = [];
    },
    limparUltimosLancamentos(state) {
      state.ultimosLancamentosLoja = [];
    },
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
    async pesquisarLivrosPorCategoria({ commit }, categoria){
      try{
        const res = await fetchLivroPorCategoria(categoria)
        commit('setPesquisarPorLivro', res.data)
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
        //'http://127.0.0.1:8000/api/clientes/login/', dados,
        'https://bytebooks-backend.fly.dev/api/clientes/login/', dados,
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
    },
    async carregarItensCarrinho({ commit }){
      try{
        const res = await fetchCarregarCarrinho()
        commit('setItensCarrinho', res.data.itens)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async adicionarAoCarrinho({ commit }, idLivro){
      try{
        console.log(commit)
        const res = await fetchAdicionarLivroAoCarrinho(idLivro)
        console.log(res.data.msg)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
        localStorage.setItem('token', '')
        localStorage.setItem('nomeUsuario', '')
        window.location.replace('/login')
    }},
    async removerLivroDoCarrinho({ commit }, idLivro){
      try{
        console.log(commit)
        const res = await fetchRemoverLivroDoCarrinho(idLivro)
        console.log(res.data.msg)
      }catch (error){
        console.error('Ocorreu um erro: ' + error)
      }
    },
    async atualizarQuantidade({ commit, dispatch }, { idLivro, adicionar }) {
      try {
        console.log(commit)
        const res = await fetchAtualizarQuantidade(idLivro, adicionar);
        await dispatch('carregarItensCarrinho');
        return res.data;
      } catch (error) {
        console.error("Erro ao atualizar quantidade: " + error);
      }
    },
    async comprarLivro({ commit }, { idLivro, quantidade }) {
      try {
        await fetchComprarLivro(idLivro, quantidade);
        console.log(commit)
      } catch (error) {
        console.error("Erro ao comprar o livro: ", error);
        console.error("status:", error.response?.status);
        console.error("body  :", error.response?.data);
        throw error;
      }
    },
    async getCliente({commit}){
      try{
        const res = await fetchGetCliente()
        commit('setInfosUsuario', res.data)
      }catch(erro){
        console.error("Erro: " + erro)
      } 
    },
    corAvatar({commit}, corAvatar){
      try{
        commit('setCorAvatar', corAvatar)
      }catch(erro){
        console.error("Erro: " + erro)
      } 
    },
    async atualizarInfosUsuario({ commit, dispatch }, payload) {
      try {
        await atualizarInfos(payload);
        commit('setNomeUsuario', payload.username)
        await dispatch('getCliente');
      } catch (error) {
        const msg =
          error.response?.data?.msg ||
          'Não foi possível atualizar os dados.';
        throw new Error(msg);
      }
    },
  }
})
