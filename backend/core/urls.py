from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import path
from .api import api
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path("", RedirectView.as_view(url="/admin/", permanent=False)),
    re_path(r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT,
             "show_indexes": False}),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    