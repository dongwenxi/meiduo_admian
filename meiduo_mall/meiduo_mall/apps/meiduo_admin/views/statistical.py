from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from users.models import User


# GET /meiduo_admin/statistical/total_count/
class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取网站总用户数：
        1. 统计网站总用户数量
        2. 返回响应
        """
        # 1. 统计网站总用户数量
        count = User.objects.count()

        # 2. 返回响应
        now_date = timezone.now() # 年-月-日 时:分:秒

        response_data = {
            # 年-月-日
            'date': now_date.date(),
            'count': count
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_increment/
class UserDayIncrementView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取日新增用户数量：
        1. 统计网站日新增用户数量
        2. 返回响应
        """
        # 1. 统计网站日新增用户数量
        # 年-月-日 时:分:秒
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(date_joined__gte=now_date).count()

        # 2. 返回响应
        response_data = {
            # 年-月-日
            'date': now_date.date(),
            'count': count
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_active/
class UserDayActiveView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取日活跃用户数量:
        1. 统计网站当日活跃用户数量
        2. 返回响应
        """
        # 1. 统计网站当日活跃用户数量
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()

        # 2. 返回响应
        response_data = {
            # 年-月-日
            'date': now_date.date(),
            'count': count
        }

        return Response(response_data)