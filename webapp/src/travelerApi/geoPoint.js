import CONFIG from './config'

export default {

  getGepoints: function () {
    return fetch(CONFIG.apiUrl + 'geopoint', {
      method: 'GET'
    })
    .then((res) => res.json())
    .catch((err) => err)
  },
  removeGeoPoint: function (id) {
    return fetch(CONFIG.apiUrl + 'geopoint/' + id + '/remove/', {
      method: 'POST'
    })
    .then((res) => {
      if (res.status !== 200) throw new Error(res.statusText)
      return res.json()
    })
  }
}
