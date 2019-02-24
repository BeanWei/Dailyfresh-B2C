# encoding: utf-8
from django.db.models import Q
from goods.models import Goods, GoodsSKU, GoodsType, GoodsImage, IndexGoodsBanner, IndexPromotionBanner
from rest_framework import serializers


class GoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

class GoodsSKUSerializer(serializers.ModelSerializer):
    type = GoodsTypeSerializer()
    goods = GoodsSerializer()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = GoodsSKU
        fields = "__all__"

class IndexGoodsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexGoodsBanner
        fields = "__all__"

class IndexPromotionBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPromotionBanner
        fields = "__all__"

class IndexTypeSerializer(serializers.ModelSerializer):
    '''首页商品分类入口'''

    # 首页商品自定义methodfield获取相关类匹配
    goods = serializers.SerializerMethodField()

    def get_goods(self, obj):
        all_goods = GoodsSKU.objects.filter(Q(type_id=obj.id))
        goods_serializer = GoodsSKUSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsType
        fields = "__all__"

