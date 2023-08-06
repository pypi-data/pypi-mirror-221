from django.urls import re_path

from . import logConsumers

websocket_urlPatterns = [ 
    re_path(r'ws/testcaseLogs/$', logConsumers.LogsConsumer.as_asgi()),           
]