import CONFIG from './config'
import jsonToForm from './jsonToForm'

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
  },
  getNotes: function (id) {
    return fetch(CONFIG.apiUrl + 'geopoint/' + id + '/notes/', {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  },
  addNote: function (id, note) {
    return fetch(CONFIG.apiUrl + 'geopoint/' + id + '/addNote/', {
      method: 'post',
      body: jsonToForm(note)
    })
    .then(res => {
      if (res.status !== 201) throw new Error(res.statusText)
      return res.json()
    })
  }
}
