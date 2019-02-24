import http from './public'
// 登陆
export const userLogin = (params) => {
  return http.POST('/login/', params)
}
// 退出登陆
export const loginOut = (params) => {
  return http.GET('/api-auth/logout/', params)
}
// 用户信息
export const userInfo = (params) => {
  return http.GET('/users/1/', params)
}
// 注册账号
export const register = (params) => {
  return http.POST('/users/', params)
}
// 上传图片
export const upload = (params) => {
  return http.POST('/member/imgaeUpload', params)
}
// 修改头像
export const updateheadimage = (params) => {
  return http.POST('/member/updateheadimage', params)
}
// 捐赠列表
export const thanksList = (params) => {
  return http.GET('/member/thanks', params)
}
// 首页接口
export const productHome = (params) => {
  return http.GET('/goods/home', params)
}
// 首页接口
export const navList = (params) => {
  return http.GET('/goods/navList', params)
}
// 推荐板块
export const recommend = (params) => {
  return http.GET('/recommendgoods/', params)
}
// 捐赠板块
export const thank = (params) => {
  return http.GET('/goods/thank', params)
}
// 极验验证码
export const geetest = (params) => {
  return http.GET('/member/geetestInit?t=' + (new Date()).getTime(), params)
}

// 首页商品分类名称
export const categories = (params) => {
  return http.GET('/categories/', params)
}

// 首页轮播
export const indexbanners = (params) => {
  return http.GET('/banners/', params)
}

// 新品
export const newgoods = (params) => {
  return http.GET('/newgoods/', params)
}

// 热卖
export const hotgoods = (params) => {
  return http.GET('/hotgoods/', params)
}

// 推荐
export const recommendgoods = (params) => {
  return http.GET('/recommendgoods/', params)
}

