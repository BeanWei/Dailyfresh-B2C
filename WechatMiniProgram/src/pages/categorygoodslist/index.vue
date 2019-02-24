<template>
  <div class="categoryList">
    <scroll-view scroll-x="true" :scroll-left="scrollLeft" class="head">
      <div @click="changeTab(index,item.id)" :class="[nowIndex==index ?'active':'']" v-for="(item, index) in navData" :key="index">
        {{item.name}}
      </div>
    </scroll-view>
    <div class="list" v-if="goodsList.length!=0">
      <div @click="goodsDetail(item.id)" class="item" v-for="(item, index) in goodsList" :key="index">
        <img :src="item.image" alt="">
        <p class="name">{{item.name}}</p>
        <p class="price">￥{{item.price}}</p>
      </div>
    </div>
    <div v-else class="none">
      <img src="/static/images/no-search.png">
      <br> 抱歉！暂时还没有商品
    </div>
  </div>
</template>

<script>
import {
  GET
} from "../../utils";
export default {
  created() { },
  mounted() {
    //获取页面传的参数
    this.categoryId = this.$root.$mp.query.id;
    this.getAllData();
  },
  data() {
    return {
      categoryId: "",
      nowIndex: 0,
      goodsList: [],
      navData: [],
      currentNav: {},
      scrollLeft: 0
    };
  },
  components: {},
  methods: {
    async changeTab(index, id) {
      this.nowIndex = index;
      const listdata = await GET("/indexgoods/" + id + "/");
      this.goodsList = listdata.goods;
      this.currentNav = listdata;
      //需要让导航滚动到可见区域
      if (this.nowIndex > 2) {
        this.scrollLeft = this.nowIndex * 60;
      }
    },
    async getAllData() {
      this.navData = await GET("/categories/");
      this.currentNavId = this.categoryId;
      for (let i = 0; i < this.navData.length; i++) {
        const id = this.navData[i].id;
        if (id == this.currentNavId) {
          this.nowIndex = i;
        }
      }
      //需要让导航滚动到可见区域
      if (this.nowIndex > 2) {
        this.scrollLeft = this.nowIndex * 60;
      } else {
        this.scrollLeft = 0;
      }
      const listdata = await GET("/indexgoods/" + this.categoryId + "/");
      this.goodsList = listdata.goods;
    },
    goodsDetail(id) {
      console.log(id)
      wx.navigateTo({
        url: "/pages/goods/main?id=" + id
      });
    }
  },
  computed: {}
};
</script>

<style lang='scss' scoped>
@import "./style.scss";
</style>