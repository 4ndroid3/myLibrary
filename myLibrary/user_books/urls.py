""" URLs de Libros leidos y sus relaciones directas """
from user_books.views import (
    UserBooksRootView,
    EstanteriaView,
    LibrosLeidosView,
)
from base_app.routers import CustomRouter

router = CustomRouter()
router.APIRootView = UserBooksRootView
router.register(r'estanterias', EstanteriaView)
router.register(r'libros', LibrosLeidosView)
urlpatterns = router.urls

app_name = 'user_books-api'