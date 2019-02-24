import axios from 'axios'
import { getStore, removeStore } from '../utils/storage'
import router from '../router/index'

// axios 配置
axios.defaults.timeout = 10000
axios.defaults.headers.post['Content-Type'] = 'application/x-www=form-urlencoded'

// http request 拦截器
axios.interceptors.request.use(
  config => {
    const token = getStore('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  err => {
    console.log('error: ', err)
    return Promise.reject(err)
  },
)

// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 401 清除token信息并跳转到登录页面
          removeStore('token')
          router.replace({path: 'login'})
          // 只有在当前路由不是登录页面才跳转
          router.currentRoute.path !== 'login' &&
            router.replace({
              path: 'login',
              query: { redirect: router.currentRoute.path }
            })
      }
    }
    // console.log(JSON.stringify(error));//console : Error: Request failed with status code 402
    return Promise.reject(error.response.data)
  },
)

export default axios
