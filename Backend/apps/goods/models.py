from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


class GoodsType(models.Model):
    '''商品类型模型类'''
    name = models.CharField(max_length=20, verbose_name='种类名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsSKU(models.Model):
    '''商品SKU模型类'''
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )
    type = models.ForeignKey('GoodsType', verbose_name='商品种类', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', verbose_name='商品SPU', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='商品名称')
    desc = models.CharField(max_length=256, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name='商品图片')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_goods_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''商品SPU模型类'''
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    # 富文本类型:带有格式的文本
    detail = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_goods'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name


class GoodsImage(models.Model):
    '''商品图片模型类'''
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品', on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='goods', verbose_name='图片路径')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class IndexGoodsBanner(models.Model):
    '''首页轮播商品展示模型类'''
    sku = models.ForeignKey('GoodsSKU', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name



class IndexPromotionBanner(models.Model):
    '''首页促销活动模型类'''
    name = models.CharField(max_length=20, verbose_name='活动名称')
    url = models.URLField(verbose_name='活动链接')
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = "主页促销活动"
        verbose_name_plural = verbose_name

# todo: 添加广告
#
# class IndexAd(models.Model):
#     """首页商品广告"""
#     category = models.ForeignKey(GoodsSKU, on_delete=models.CASCADE, related_name='category',verbose_name="商品类目")
#     goods =models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods')
#
#     class Meta:
#         verbose_name = '首页广告'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.goods.name