import CONFIG from './config'

export default {

  getItineraies: function () {
    return fetch(CONFIG.apiUrl + 'itinerary', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  }

}
