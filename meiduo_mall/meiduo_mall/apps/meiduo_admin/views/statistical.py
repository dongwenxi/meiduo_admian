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
