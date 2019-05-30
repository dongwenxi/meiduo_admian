from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializers.skus import SKUImageSerializer, SKUSimpleSerializer


class SKUImageViewSet(ModelViewSet):
    """SKU图片视图集"""
    permission_classes = [IsAdminUser]
    # 指定视图所使用的查询集
    queryset = SKUImage.objects.all()
    # 指定视图所使用的序列化器类
    serializer_class = SKUImageSerializer

    # GET /meiduo_admin/skus/images/ -> list

    # def list(self, request):
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)


# GET /meiduo_admin/skus/simple/
class SKUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = SKU.objects.all()
    serializer_class = SKUSimpleSerializer

    # 注：关闭分页
    pagination_class = None

    # def get(self, request):
    #     # return self.list(request)
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)
