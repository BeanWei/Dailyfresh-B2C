import http from './public'
// 商品列表
export const getAllGoods = (params) => {
  return http.GET('/goods/', params)
}
// 分类商品列表
export const getCategoryGoods = (params) => {
  return http.GET('/indexgoods/' + params + '/')
}
// 获取购物车列表
export const getCartList = (params) => {
  return http.GET('/shopcarts/', params)
}
// 加入购物车
export const addCart = (params) => {
  return http.POST('/shopcarts/', params)
}
// 删除购物车勾选商品
export const delCartChecked = (params) => {
  return http.POST('', params)
}
// 编辑购物车
export const cartEdit = (params) => {
  return http.PUT('/shopcarts/' + params.goods + '/', params)
}
// 删除整条购物车
export const cartDel = (params) => {
  return http.DELETE('/shopcarts/' + params.goods_id + '/', params)
}
// 获取用户地址
export const addressList = (params) => {
  return http.POST('/address', params)
}
// 通过id获取地址
export const getAddress = (params) => {
  return http.POST('/member/address', params)
}
// 修改收货地址
export const addressUpdate = (params) => {
  return http.POST('/member/updateAddress', params)
}
// 添加收货地址
export const addressAdd = (params) => {
  return http.POST('/member/addAddress', params)
}
// 删除收货地址
export const addressDel = (params) => {
  return http.POST('/member/delAddress', params)
}
// 生成订单
export const submitOrder = (params) => {
  return http.POST('/member/addOrder', params)
}
// 支付
export const payMent = (params) => {
  return http.POST('/member/payOrder', params)
}
// 获取用户订单
export const orderList = (params) => {
  return http.GET('/member/orderList', params)
}
// 获取单个订单详情
export const getOrderDet = (params) => {
  return http.GET('/member/orderDetail', params)
}
// 取消订单
export const cancelOrder = (params) => {
  return http.POST('/member/cancelOrder', params)
}
// 商品详情
export const productDet = (params) => {
  return http.GET('/goods/' + params)
}
// 删除订单
export const delOrder = (params) => {
  return http.GET('/member/delOrder', params)
}
// 商品列表
export const getSearch = (params) => {
  return http.GET('/goods/search', params)
}
// 快速搜索
export const getQuickSearch = (params) => {
  return http.GET('/goods/quickSearch', params)
}
