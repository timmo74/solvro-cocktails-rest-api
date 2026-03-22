from django.urls import path, include
from .views import IngredientViewSet,CocktailViewSet, CocktailIngredientViewSet,RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'cocktails', CocktailViewSet)
router.register(r'cocktail-ingredients', CocktailIngredientViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login',TokenObtainPairView.as_view(), name='token_obtain_pair'),
]



 