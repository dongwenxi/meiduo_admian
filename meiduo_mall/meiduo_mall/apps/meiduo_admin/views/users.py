from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin

from meiduo_admin.serializers.users import AdminAuthSerializer


# POST /meiduo_admin/authrizations/
# class AdminAuthView(CreateModelMixin, GenericAPIView):
class AdminAuthView(CreateAPIView):
    # 指定视图所使用的序列化器类
    serializer_class = AdminAuthSerializer

    # def post(self, request):
    #     """
    #     管理员登录：
    #     1. 获取参数并进行校验(参数完整性，用户名和密码正确)
    #     2. 服务器创建一个jwt token，保存登录用户身份信息
    #     3. 返回响应，登录成功
    #     """
    #     # 1. 获取参数并进行校验(参数完整性，用户名和密码正确)
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 2. 服务器创建一个jwt token，保存登录用户身份信息(create)
    #     serializer.save()
    #
    #     # 3. 返回响应，登录成功
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     return self.create(request)