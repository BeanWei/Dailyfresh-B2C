<template>
  <div class="index">
    <div class="search">
      <div>
        <h1 style="color: transparent;-webkit-text-stroke: 1px black;letter-spacing: 0.2em;">
        「天天生鲜」
        </h1>
      </div>
      <div @click="toSearch">
        <input type="text" placeholder="搜索商品">
        <span class="icon"></span>
      </div>
    </div>
    <div class="swiper">
      <swiper class="swiper-container" indicator-dots="true" autoplay="true" interval="3000" circular="true" duration="500">
        <block v-for="(item, index) in banners " :key="index">
          <swiper-item class="swiper-item">
            <image :src="item.image" class="slide-image" />
          </swiper-item>
        </block>
      </swiper>
    </div>
    <div class="channel">
      <div @click="categoryGoodsList(item.id)" v-for="(item, index) in categoryList" :key="index">
        <img src="/static/images/icon-category.png" alt="">
        <p style="font-size: 12px;">{{item.name}}</p>
      </div>
    </div>
    <div class="newgoods hotgoods">
      <div @click="goodsList('new')" class="newgoods-top">
        <div class="top">
          <p>新品开售</p>
          <p>查看全部</p>
        </div>
      </div>
      <div class="list">
        <ul>
          <scroll-view class="scroll-view" :scroll-x="true">
            <li @click="goodsDetail(item.id)" v-for="(item, index) in newGoods" :key="index">
              <img :src="item.image" alt="">
              <p>{{item.name}}</p>
              <p>{{item.desc}}</p>
              <p>￥{{item.price}}</p>
            </li>
          </scroll-view>
        </ul>
      </div>
    </div>
    <div class="newgoods hotgoods">
      <div @click="goodsList('hot')" class="newgoods-top">
        <div class="top">
          <p>热销商品</p>
          <p>查看全部</p>
        </div>
      </div>
      <div class="list">
        <ul>
          <scroll-view class="scroll-view" :scroll-x="true">
            <li @click="goodsDetail(item.id)" v-for="(item, index) in hotGoods" :key="index">
              <img :src="item.image" alt="">
              <p>{{item.name}}</p>
              <p>{{item.desc}}</p>
              <p>￥{{item.price}}</p>
            </li>
          </scroll-view>
        </ul>
      </div>
    </div>
    <div class="newgoods hotgoods">
      <div @click="goodsList('recommend')" class="newgoods-top">
        <div class="top">
          <p>官方推荐</p>
          <p>查看全部</p>
        </div>
      </div>
      <div class="list">
        <ul>
          <scroll-view class="scroll-view" :scroll-x="true">
            <li @click="goodsDetail(item.id)" v-for="(item, index) in recommendGoods" :key="index">
              <img :src="item.image" alt="">
              <p>{{item.name}}</p>
              <p>{{item.desc}}</p>
              <p>￥{{item.price}}</p>
            </li>
          </scroll-view>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { GET } from "../../utils";
export default {
  onShow() {
  },
  computed: {
  },
  mounted() {
    this.getData();
    console.log(this.banners);
  },
  data() {
    return {
      banners: [],
      categoryList: [],
      newGoods: [],
      hotGoods: [],
      recommendGoods: []
    };
  },
  components: {},
  methods: {
    toSearch() {
      wx.navigateTo({
        url: "/"
      });
    },
    async getData() {
      this.banners = await GET("/banners/");
      this.categoryList = await GET("/categories/");
      this.newGoods = await GET("/newgoods/");
      this.hotGoods = await GET("/hotgoods/");
      this.recommendGoods = await GET("/recommendgoods/");
    },
    goodsDetail(id) {
      wx.navigateTo({
        url: "/pages/goodsdetail/main?id=" + id
      });
    },
    categoryGoodsList(id) {
      wx.navigateTo({
        url: "/pages/categorygoodslist/main?id=" + id
      });
    },
    goodsList(info) {
      if (info == "hot") {
        wx.navigateTo({
          url: "/pages/newgoods/main?isHot=" + 1
        });
      } else {
        wx.navigateTo({
          url: "/pages/newgoods/main?isNew=" + 1
        });
      }
    },
    topicdetail(id) {
      wx.navigateTo({
        url: "/pages/topicdetail/main?id=" + id
      });
    },
    totopic() {
      wx.navigateTo({
        url: "/pages/topic/main"
      });
    },
  },
  created() { }
};
</script>

<style lang='scss' scoped>
@import "./style.scss";
</style>