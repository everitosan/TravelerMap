import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    step: 'ITINERARY_LIST',
    currentItinerary: {}
  },
  mutations: {
    showIntineraryDetail (state) {
      state.step = 'ITINERARY_DETAIL'
    },
    showIntineraryList (state) {
      state.step = 'ITINERARY_LIST'
    },
    showAddItinerary (state) {
      state.step = 'ADD_ITINERARY'
    },
    updateCurrentItinerary (state, payload) {
      state.currentItinerary = payload.itinerary
    }
  }
})

export default store
