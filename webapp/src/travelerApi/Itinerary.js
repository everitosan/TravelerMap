import CONFIG from './config'

export default {

  getItineraies: function () {
    return fetch(CONFIG.apiUrl + 'itinerary', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  },

  getItineraryGeopoints: function (id) {
    return fetch(CONFIG.apiUrl + 'itinerary/' + id + '/geopoints', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  }

}
