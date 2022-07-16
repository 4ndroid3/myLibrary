from django.urls import include, path, re_path
from books.views import GenerosView
from rest_framework.routers import DefaultRouter
from base_app.routers import CustomRouter
from books.views import CircuitsRootView

router = CustomRouter()
router.APIRootView = CircuitsRootView
router.register(r'generos', GenerosView)
urlpatterns = router.urls

app_name = 'books-api'