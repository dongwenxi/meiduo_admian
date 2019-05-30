from rest_framework import serializers

from goods.models import SKUImage


# sku_image = SKUImage.objects.get(id=1)
# sku_image.sku
class SKUImageSerializer(serializers.ModelSerializer):
    """SKU图片序列化器类"""
    sku_id = serializers.IntegerField(label='SKU商品id')

    # 关联对象嵌套序列化
    sku = serializers.StringRelatedField(label='SKU商品名称')

    class Meta:
        model = SKUImage
        exclude = ('create_time', 'update_time')