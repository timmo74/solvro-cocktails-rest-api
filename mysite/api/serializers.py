from rest_framework import serializers
from .models import Ingredient, Cocktail, CocktailIngredient, Rating
from django.contrib.auth.models import User

from django.db.models import Avg


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'  



class CocktailIngredientSerializer(serializers.ModelSerializer):

    ingredient_name = serializers.CharField(source='ingredient.name')

    class Meta:
        model = CocktailIngredient
        fields = ['id','ingredient','ingredient_name','amount']


    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        #aut szyfrowanie hasla
        user = User.objects.create_user(**validated_data)
        return user
    

class CocktailSerializer(serializers.ModelSerializer):
    ingredients_list = CocktailIngredientSerializer(source='cocktailingredient_set', many=True, read_only=True)
    author_name = serializers.ReadOnlyField(source='author.username')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'instructions', 'author', 'author_name', 'ingredients_list', 'average_rating']
        extra_kwargs = {'author': {'read_only': True}}

    def get_average_rating(self, obj):
        avg = obj.ratings.aggregate(Avg('score'))['score__avg']
        return round(avg, 1) if avg is not None else 0.0
    

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['score']

        