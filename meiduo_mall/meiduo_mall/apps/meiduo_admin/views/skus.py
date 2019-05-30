from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage
from meiduo_admin.serializers.skus import SKUImageSerializer


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
