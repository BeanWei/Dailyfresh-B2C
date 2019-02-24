# encoding: utf-8

import xadmin
from .models import Goods, GoodsSKU, GoodsType, GoodsImage, IndexGoodsBanner, IndexPromotionBanner


class GoodsAdmin(object):
    list_display = ["name", "detail", "add_time"]
    search_fields = ["name", ]
    list_filter = ["name", "add_time"]
    style_fields= {"detail": "ueditor"}


class GoodsSKUAdmin(object):
    list_display = ["name", "desc", "price", "unite", "stock", "sales",
                    "click_num", "fav_num", "status", "is_new", "is_hot", "is_recommend", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_new", "is_hot", "is_recommend"]
    list_filter = ["type__name", "goods__name", "name", "desc", "price", "unite", "stock", "sales",
                    "click_num", "fav_num", "status", "is_new", "is_hot", "is_recommend", "add_time"]

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsTypeAdmin(object):
    list_display = ["name", "add_time"]
    list_filter = ["name", "add_time"]
    search_fields = ['name', ]


class IndexGoodsBannerAdmin(object):
    list_display = ["sku", "image", "index"]


class IndexPromotionBannerAdmin(object):
    list_display = ["name", "url", "image", "index"]



xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsSKU, GoodsSKUAdmin)
xadmin.site.register(GoodsType, GoodsTypeAdmin)
xadmin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
xadmin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)


