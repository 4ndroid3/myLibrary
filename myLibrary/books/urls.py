""" URLs de Libros y sus relaciones directas """
from books.views import (
    BooksRootView,
    GenerosView,
    AutoresView,
    LibrosView,
)
from base_app.routers import CustomRouter

router = CustomRouter()
router.APIRootView = BooksRootView
router.register(r'generos', GenerosView)
router.register(r'autores', AutoresView)
router.register(r'libros', LibrosView)
urlpatterns = router.urls

app_name = 'books-api'