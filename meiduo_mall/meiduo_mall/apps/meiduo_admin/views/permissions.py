from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from meiduo_admin.serializers.permissions import PermissionSerializer, ContentTypeSerializer, GroupSerializer


class PermissionViewSet(ModelViewSet):
    """权限视图集"""
    permission_classes = [IsAdminUser]
    # 指定视图所使用的查询集
    queryset = Permission.objects.all()
    # 指定视图所使用的序列化器类
    serializer_class = PermissionSerializer

    # GET /meiduo_admin/permission/perms/ -> list
    # POST /meiduo_admin/permission/perms/ -> create
    # GET /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> destroy

    # def list(self, request):
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     serializer.save() # -> create
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # update
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # GET /meiduo_admin/permission/content_types/ -> content_types
    def content_types(self, request):
        """
        获取权限类型数据：
        1. 获取权限类型数据
        2. 将权限类型数据序列化并返回
        """
        # 1. 获取权限类型数据
        c_types = ContentType.objects.all()

        # 2. 将权限类型数据序列化并返回
        serializer = ContentTypeSerializer(c_types, many=True)
        return Response(serializer.data)


class GroupViewSet(ModelViewSet):
    """用户组视图集"""
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # GET /meiduo_admin/permission/groups/ -> list

    # def list(self, request):
    #     qs = self.get_queryset()
    #     serializer = self.get_serializer(qs, many=True)
    #     return Response(serializer.data)


