# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#将模块中显式出现的所有字符串转为unicode类型，不过，对于必须使用str字符串的地方要加以注意
from django.apps import AppConfig
#属性表示这个配置类是加载到哪个应用的，每个配置类必须包含此属性，默认自动生成


class AssetsConfig(AppConfig):
    name = 'asset'
