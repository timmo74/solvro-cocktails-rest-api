
from rest_framework import viewsets,filters, generics
from .models import Ingredient, Cocktail, CocktailIngredient    
from .serializers import IngredientSerializer, CocktailSerializer, CocktailIngredientSerializer, RatingSerializer 
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import IngredientSerializer, CocktailSerializer, CocktailIngredientSerializer, UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Rating

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    #wbudowany filtr wyszukiwania
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer  
    #filtrowanie po nazwie i kategorii 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

    #blokada (przeglad dla zalogowanych)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated], serializer_class=RatingSerializer)
    def rate(self, request, pk=None):
        cocktail = self.get_object() 
        serializer = RatingSerializer(data=request.data)
        
        if serializer.is_valid():
            score = serializer.validated_data['score']
            rating, created = Rating.objects.update_or_create(
                user=request.user, cocktail=cocktail,
                defaults={'score': int(score)}
            )
            return Response({'detail': 'Ocena zapisana!', 'score': rating.score}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CocktailIngredientViewSet(viewsets.ModelViewSet):
    queryset = CocktailIngredient.objects.all()
    serializer_class = CocktailIngredientSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    #przypisanie urz-kok
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)