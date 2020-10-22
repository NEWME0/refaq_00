from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('apps.first.urls')),
    path('second/', include('apps.second.urls')),
]


if settings.DEBUG:
    from drf_yasg.openapi import Info
    from drf_yasg.views import get_schema_view
    from rest_framework.permissions import AllowAny

    info = Info(title='Only one', description='...', default_version='v0')
    schema = get_schema_view(info, public=True, permission_classes=(AllowAny,))
    swagger = schema.with_ui('swagger')

    urlpatterns += [
        path('swagger/', swagger)
    ]
