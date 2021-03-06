from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

schema_view = get_schema_view(
    openapi.Info(
        title="Jobs Portal API",
        default_version="v1",
        description="Jobs Portal Api Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

lang_patterns = i18n_patterns(
    path("", include("jobsapp.urls")),
    path("", include("accounts.urls")),
)

urlpatterns = lang_patterns + [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("swagger", schema_view.with_ui("swagger", cache_timeout=0)),
                path("", include("accounts.api.urls")),
                path("", include("jobsapp.api.urls")),
            ]
        ),
    ),
    path("social-auth/", include("social_django.urls", namespace="social")),
]
