# -*- coding: utf-8 -*-
"""
urls config
"""
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from django.conf import settings
# 公共URL配置

from users.views import user_list


urlpatterns = patterns(
    '',
    # Django后台数据库管理
    url(r'^admin/', include(admin.site.urls)),
    # 用户登录鉴权--请勿修改
    url(r'^account/', include('account.urls')),
    # 应用功能开关控制--请勿修改
    url(r'^assets/', include('assets.urls', namespace='assets')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^app_control/', include('app_control.urls')),
    # 在home_application(根应用)里开始开发你的应用的主要功能
    url(r'^', user_list),
)


handler404 = 'error_pages.views.error_404'
handler500 = 'error_pages.views.error_500'
handler403 = 'error_pages.views.error_403'
handler401 = 'error_pages.views.error_401'
