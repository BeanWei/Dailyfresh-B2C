import axios from './http'
axios.defaults.timeout = 10000
axios.defaults.headers.post['Content-Type'] = 'application/x-www=form-urlencoded'

export const host = 'http://127.0.0.1:8000'

export default {
  GET (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.get(host + url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  POST (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.post(host + url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  PUT (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.put(host + url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  DELETE (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.delete(host + url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  PATCH (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.patch(host + url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  }
}
