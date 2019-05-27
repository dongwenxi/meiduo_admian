from django.conf.urls import url
from meiduo_admin.views import users, statistical

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthView.as_view()),

    # 数据统计
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
]