import CONFIG from './config'

export default {
  getBackgroundPhoto: function () {
    return fetch(CONFIG.URL + 'photos/random?query=landscape&&orientation=landscape', {
      method: 'GET',
      headers: new Headers({
        'Authorization': 'Client-ID ' + CONFIG.Application_ID
      })
    })
      .then(res => res.json())
      .then(json => json.urls.regular)
      .catch(err => err)
  }
}
