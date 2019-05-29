from rest_framework import serializers

from goods.models import GoodsChannel, GoodsChannelGroup


# channel = GoodsChannel.objects.get(id=1)
# channel.category
# channel.category_id
# channel.group
# channel.group_id
class ChannelSerializer(serializers.ModelSerializer):
    """频道序列化器类"""
    # 关联对象嵌套序列化：将关联对象序列化为关联对象模型类__str__方法的返回值
    category = serializers.StringRelatedField(label='一级分类名称')
    group = serializers.StringRelatedField(label='频道组的名称')

    class Meta:
        model = GoodsChannel
        fields = ('id', 'category', 'category_id', 'group', 'group_id', 'sequence', 'url')


class ChannelTypeSerializer(serializers.ModelSerializer):
    """频道组序列化器类"""
    class Meta:
        model = GoodsChannelGroup
        fields = ('id', 'name')