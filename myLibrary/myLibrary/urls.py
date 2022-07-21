""" Base URL of the Project """

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from books import urls
from base_app.views import APIRootView

# router = DefaultRouter()
# router.register(r'books', include(urls))
SchemaView = get_schema_view(
	openapi.Info(
		title="My Own Online Library",
		default_version='v0.1',
		description="API para registrar libros leidos o para leer",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="asj@gmail.com"),
		license=openapi.License(name="Sin licencia"),
	),
	public=True,
	permission_classes=[permissions.AllowAny],
)

urlpatterns = [
	path('api/', APIRootView.as_view(), name='api-root'),
	path('api/books/', include('books.urls')),
	path('api/user-books/', include('user_books.urls')),
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	re_path(
		r'^swagger(?P<format>\.json|\.yaml)$',
		SchemaView.without_ui(cache_timeout=0),
		name='schema-json'
	),
	re_path(
		r'^swagger/$',
		SchemaView.with_ui('swagger', cache_timeout=0),
		name='schema-swagger-ui'
	),
	re_path(
		r'^redoc/$',
		SchemaView.with_ui('redoc', cache_timeout=0),
		name='schema-redoc'
	),

]
# urlpatterns =+ router.urls
