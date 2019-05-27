from django.conf.urls import url
from meiduo_admin.views import users

urlpatterns = [
    url(r'^authrizations/$', users.AdminAuthView.as_view()),
]