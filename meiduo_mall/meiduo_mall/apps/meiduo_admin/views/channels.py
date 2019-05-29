from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from goods.models import GoodsChannel, GoodsChannelGroup
from meiduo_admin.serializers.channels import ChannelSerializer, ChannelTypeSerializer


class ChannelViewSet(ModelViewSet):
    # 指定视图所使用的序列化器
    serializer_class = ChannelSerializer
    # 指定视图所使用的查询集
    queryset = GoodsChannel.objects.all()

    # GET /meiduo_admin/goods/channels/ -> list

    # def list(self, request):
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)


# GET /meiduo_admin/goods/channel_types/
# class ChannelTypesView(ListModelMixin, GenericAPIView):
class ChannelTypesView(ListAPIView):
    serializer_class = ChannelTypeSerializer
    queryset = GoodsChannelGroup.objects.all()

    # 注：关闭分页
    pagination_class = None

    # def get(self, request):
    #     """
    #     获取频道组的数据：
    #     1. 查询获取所有频道组的数据
    #     2. 将频道组数据序列化并返回
    #     """
    #     # 1. 查询获取所有频道组的数据
    #     channel_types = self.get_queryset()
    #
    #     # 2. 将频道组数据序列化并返回
    #     serializer = self.get_serializer(channel_types, many=True)
    #     return Response(serializer.data)

    # def get(self, request):
    #     return self.list(request)
