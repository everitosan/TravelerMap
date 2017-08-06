import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    step: 'ITINERARY_LIST',
    currentItinerary: {},
    showBottomButtons: true
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
    showAddGeoPoint (state) {
      state.step = 'ADD_GEOPOINT'
    },
    updateCurrentItinerary (state, payload) {
      state.currentItinerary = payload.itinerary
    },
    ShouldShowBottomButtons (state, flag) {
      state.showBottomButtons = flag
    }
  }
})

export default store
