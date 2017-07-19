import CONFIG from './config'

export default {

  getGepoints: function() {
      return fetch(CONFIG.apiUrl + 'geoPoint', {
        method:'GET'
      })
      .then((res)=> res.json())
      .catch((err)=> err)
  }

}
