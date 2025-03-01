from django.contrib import admin
from .models import Profile, GoalChoices, ActivityChoices, Recipes, Groceries, Nutrition

# Register your models here.
 
admin.site.register(Profile)
admin.site.register(GoalChoices)
admin.site.register(ActivityChoices)
admin.site.register(Recipes)
admin.site.register(Groceries)
admin.site.register(Nutrition)