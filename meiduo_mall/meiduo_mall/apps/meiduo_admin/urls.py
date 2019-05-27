from django.conf.urls import url
from meiduo_admin.views import users, statistical

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthView.as_view()),

    # 数据统计
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrderView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthIncrementView.as_view()),
]