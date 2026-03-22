from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_alcoholic = models.BooleanField(default=False)

    img_url = models.URLField(blank=True, null=True)  # Optional field for image URL

    def __str__(self):
        return self.name
    
class Cocktail(models.Model):
    name= models.CharField(max_length=100)  
    category = models.CharField(max_length=100)
    instructions = models.TextField()

    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredient',related_name='cocktails')
    #dodanie autora:
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__ (self):
        return self.name
    
class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)  

    class Meta:
        unique_together = ('cocktail', 'ingredient')

    def __str__(self):
        return f"{self.amount} of {self.ingredient.name} in {self.cocktail.name}"
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        # Jeden użytkownik może ocenić dany koktajl tylko raz....
        unique_together = (('user', 'cocktail'),)

    def __str__(self):
        return f"{self.user.username} - {self.cocktail.name} - {self.score}"
