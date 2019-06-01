from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import SPU, SPUSpecification
from meiduo_admin.serializers.spus import SPUSimpleSerializer, SPUSpecSerializer


# GET /meiduo_admin/goods/simple/
class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer

    # 注：关闭分页
    pagination_class = None

    # def get(self, request):
    #     # return self.list(request)
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)


# GET /meiduo_admin/goods/(?P<pk>\d+)/specs/
class SPUSpecView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        """
        获取SPU规格选项数据:
        1. 获取和spu对象关联的规格数据
        2. 将获取规格数据序列化并返回
        """
        # 1. 获取和spu对象关联的规格数据
        specs = SPUSpecification.objects.filter(spu_id=pk)

        # 2. 将获取规格数据序列化并返回
        serializer = SPUSpecSerializer(specs, many=True)
        return Response(serializer.data)
