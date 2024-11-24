from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version='v1',
        description="API documentation for the Student Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@local.dev"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/',          admin.site.urls),
    path('auth/',           include('djoser.urls')),
    path('auth/',           include('djoser.urls.jwt')),
    path('api/users/',      include('users.urls')),
    path('api/courses/',    include('courses.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/grades/',     include('grades.urls')),
    path('api/students/',   include('students.urls')),
    path('api/analytics/',  include('analytics.urls')),
    path('swagger/',        schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',          schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]