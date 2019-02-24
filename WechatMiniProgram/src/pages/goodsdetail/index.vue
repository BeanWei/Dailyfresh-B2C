<template>
  <div class="goods">
    <div class="swiper">
      <swiper class="swiper-container" indicator-dots="true" autoplay="true" interval="3000" duration="1000">
        <block v-for="(item, index) in goodsinfo.images " :key="index">
          <swiper-item class="swiper-item">
            <image :src="item.image" class="slide-image" />
          </swiper-item>
        </block>
      </swiper>
      <button class="share" hover-class="none" open-type="share" value="">分享商品</button>
    </div>
    <div class="swiper-b">
      <div class="item">30天无忧退货</div>
      <div class="item">48小时快速退款</div>
      <div class="item">满88元免邮费</div>
    </div>
    <div class="goods-info">
      <div class="c">
        <p>{{goodsinfo.name}}</p>
        <p>{{goodsinfo.desc}}</p>
        <p>￥{{goodsinfo.price}}</p>
      </div>
    </div>
    <div @click="showType" class="section-nav">
      <div>请选择规格数量</div>
      <div></div>
    </div>
    <!-- <div @click="showType" class="section-nav">
      <div>用户评价</div>
      <div></div>
    </div> -->

    <div class="attribute">
      <div class="head">
        商品参数
      </div>
      <div class="item">
        <div>{{goodsinfo.unite}}</div>
      </div>
    </div>
    <div class="detail">
      <wxParse :content="goodsinfo.goods.detail" />
    </div>
<!-- 
    <div class="common-problem">
      <div class="h">
        <div class="line"></div>
        <text class="title">大家都在看</text>
        <div class="line"></div>
      </div>
      <div class="sublist">
        <div @click="togoodsDetail(subitem.id)" v-for="(subitem, subindex) in productList" :key="subindex">
          <img :src="subitem.list_pic_url" alt="">
          <p>{{subitem.name}}</p>
          <p>￥{{subitem.retail_price}}</p>
        </div>
      </div>
    </div> -->

    <div class="bottom-fixed">
      <div @click="collect">
        <div class="collect" :class="[collectFlag ? 'active' :'']">

        </div>

      </div>
      <div @click="toCart">
        <div class="car">
          <span>
            666
          </span>
          <img src="/static/images/ic_menu_shoping_nor.png" alt="">
        </div>
      </div>
      <div @click="bug">立即购买</div>
      <div @click="addCart">加入购物车</div>
    </div>

    <!-- 选择规格部分 -->
    <div v-show="showpop" @click="showType" class="pop">

    </div>
    <div class="attr-pop" :class="[showpop ? 'fadeup' : 'fadedown']">
      <div class="top">
        <div class="left">
          <img :src="goodsinfo.image" alt="">
        </div>
        <div class="right">
          <div>
            <p>价格￥{{goodsinfo.price}}</p>
            <p>请选择数量</p>
          </div>
        </div>
        <div @click="showType" class="close">
          X
        </div>
      </div>
      <div class="b">
        <p>数量</p>
        <div class="count">
          <div @click="reduce" class="cut">-</div>
          <input class="number" disabled="" v-model="number" />
          <div @click="add" class="add">+</div>
        </div>
      </div>
    </div>

    <!-- 选择规格部分 -->
  </div>
</template>

<script>
import { GET, POST, toLogin, login, getStorageOpenid } from "../../utils";
import wxParse from "mpvue-wxparse";
export default {
  onShow() {
  },
  mounted() {
    //判断是否登录获取用户信息
    if (login()) {
      this.userInfo = login();
    }
    console.log(this.$root.$mp.query.id);
    this.id = this.$root.$mp.query.id;
    this.openId = getStorageOpenid();
    this.goodsDetail();
  },
  //商品转发
  onShareAppMessage() {
    console.log(this.goodsinfo.name);
    console.log(this.goodsinfo.id);
    console.log(this.gallery[0].img_url);
    return {
      title: this.goodsinfo.name,
      path: "/pages/goods/main?id=" + this.goodsinfo.id,
      imageUrl: this.goodsinfo.image
    };
  },
  data() {
    return {
      openId: "",
      collectFlag: false,
      number: 0,
      showpop: false,
      goodsinfo: {},
      totalprice: ""
    };
  },
  components: {
    wxParse
  },
  methods: {
    togoodsDetail(id) {
      wx.redirectTo({ url: "/pages/goods/main?id=" + id });
    },
    add() {
      this.number = this.number + 1;
    },
    reduce() {
      if (this.number > 1) {
        this.number = this.number - 1;
      } else {
        return false;
      }
    },
    async bug() {
      if (toLogin()) {
        if (this.showpop) {
          if (this.number == 0) {
            wx.showToast({
              title: "请选择商品数量", //提示的内容,
              duration: 2000, //延迟时间,
              icon: "none",
              mask: true, //显示透明蒙层，防止触摸穿透,
              success: res => { }
            });
            return false;
          }
          const data = await POST("/order/submitAction", {
            goodsId: this.goodsId,
            openId: this.openId,
            totalprice: this.totalprice
          });
          if (data) {
            wx.navigateTo({
              url: "/pages/order/main"
            });
          }
        } else {
          this.showpop = true;
        }
      }
    },
    async collect() {
      if (toLogin()) {
        this.collectFlag = !this.collectFlag;
        const data = await POST("/collect/addcollect", {
          openId: this.userInfo.openId,
          goodsId: this.goodsinfo.id
        });
      }
    },
    async addCart() {
      if (toLogin()) {
        if (this.showpop) {
          if (this.number == 0) {
            wx.showToast({
              title: "请选择商品数量", //提示的内容,
              duration: 2000, //延迟时间,
              icon: "none",
              mask: true, //显示透明蒙层，防止触摸穿透,
              success: res => { }
            });
            return false;
          }
          const data = await POST("/cart/addCart", {
            openId: this.userInfo.openId,
            goodsId: this.goodsinfo.id,
            number: this.number
          });
          //添加成功后
          if (data) {
            this.allnumber = this.allnumber + this.number;
            wx.showToast({
              title: "添加购物车成功",
              icon: "success",
              duration: 1500
            });
          }
        } else {
          this.showpop = true;
        }
      }
    },
    toCart() {
      wx.switchTab({
        url: "/pages/cart/main"
      });
      // wx.navigateTo({
      //   url: "/pages/cart/main"
      // });
    },
    async goodsDetail() {
      this.goodsinfo = await GET("/goods/" + this.id + "/");
    },
    showType() {
      this.showpop = !this.showpop;
    }
  },
  computed: {}
};
</script>
<style lang='scss' scoped>
@import url("~mpvue-wxparse/src/wxParse.css");
@import "./style.scss";
</style>