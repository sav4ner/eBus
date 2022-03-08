
import { createStore } from "vuex";

export default createStore({
  state: {
    token: '',
    username: '',
    isAuthenticated: false, 
  },
  mutations: {
    initizeStore(state) {
      if (localStorage.getItem('token')) {
        state.token= localStorage.getItem('token')
        state.isAuthenticated = true
      }else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token,username) {
      state.token = token
      state.username = username
      state.isAuthenticated = true
    },
    
    removeToken(state){
      state.token= ''
      state.isAuthenticated = false
    }
  },
  actions: {

  },
  modules: {

  },
});
