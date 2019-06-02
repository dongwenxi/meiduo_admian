from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from users.models import User


class PermissionSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限类型序列化器类"""
    class Meta:
        model = ContentType
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSimpleSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = ('id', 'name')


class AdminSerializer(serializers.ModelSerializer):
    """管理员序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'groups', 'user_permissions')


class GroupSimpleSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = ('id', 'name')









