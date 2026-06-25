from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # administrative dashboard
    path("admin/", admin.site.urls),
    # Forwards the root ndomain into sticky notes app
    path("", include("notes.urls")),
]
