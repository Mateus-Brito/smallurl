from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("smallurl.shortener.urls")),
    path("admin/", admin.site.urls),
]

handler404 = "smallurl.core.views.page_not_found_view"
