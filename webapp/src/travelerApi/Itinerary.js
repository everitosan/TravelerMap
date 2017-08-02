import CONFIG from './config'
import jsonToForm from './jsonToForm'
export default {

  getItineraies () {
    return fetch(CONFIG.apiUrl + 'itinerary', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  },

  getItineraryGeopoints (id) {
    return fetch(CONFIG.apiUrl + 'itinerary/' + id + '/geopoints', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  },

  createItinerary (info) {
    return fetch(CONFIG.apiUrl + 'itinerary/', {
      method: 'post',
      body: jsonToForm(info)
    })
    .then(res => res.json())
    .catch(err => err)
  }

}
