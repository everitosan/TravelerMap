import CONFIG from './config'

export default {
  findAddress: function (addr) {
    return fetch(CONFIG.GEOCODE_URL + addr + '&key=' + CONFIG.KEY, {
      method: 'get'
    })
    .then(res => {
      if (res.status === 200) {
        return res.json()
      } else {
        throw new Error('Not found')
      }
    })
    .catch(err => err)
  },
  getTimeZone (coords, timestamp) {
    return fetch(`${CONFIG.TIMEZONE_URL}${coords}&timestamp=${timestamp}&key=${CONFIG.TIMEZONE_KEY}`, {
      method: 'get'
    })
    .then(res => res.json())
    .catch(err => err)
  }
}
