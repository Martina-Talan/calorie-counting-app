
from django.shortcuts import render
from django.http import HttpResponse
from caloriecounter.models import Profile, Recipes, Groceries, Nutrition
from django.db.models import F,Sum
from .forms import ProfileForm
# Create your views here.

def index(request):
    return render(request, 'caloriecounter/template/layout.html')

def profile(request):
       if request.method == "GET":

        total_percentage = Nutrition.objects.aggregate(
        total_percentage=Sum(F('carbs') + F('protein') + F('fat'))
       )['total_percentage']

        return render(request, "caloriecounter/profile.html",{
           "total_percentage": total_percentage,
        })
       else:
        # form = NewForm(request.POST)
        # user = request.user
        # if form.is_valid():
        #    listing = form.save()
        #    listing.listed_by = user
        #    listing.save()
    
        return HttpResponseRedirect(reverse("index"))


def diary(request):
    if request.method == "GET":
        return render(request, "caloriecounter/profile.html")
    else:
        profile= Profile.objects.all()
        calorie_goal = int(request.POST.get('calorie_goal'))
        carbs_percentage = int(request.POST.get('carbs')) * 0.01
        protein_percentage = int(request.POST.get('protein')) * 0.01
        fat_percentage = int(request.POST.get('fat')) * 0.01
        carbs_calories = carbs_percentage * calorie_goal
        protein_calories = protein_percentage * calorie_goal
        fat_calories = fat_percentage * calorie_goal
        gram_of_carb = round(carbs_calories / 4, 0)
        gram_of_protein = round(protein_calories / 4, 0)
        gram_of_fat = round(fat_calories / 7, 0)
        # carbs = makros.carbs
        # protein = makros.protein
        # fat = makros.fat
    

        return render(request, 'caloriecounter/diary.html', {
            "profiles": profile,

            # "carbs": carbs_calories,
            # "protein":protein_calories,
            # "fat": fat_calories,
            "gram_of_carb": gram_of_carb,
            "gram_of_protein": gram_of_protein,
            "gram_of_fat": gram_of_fat,

        })

def update_nutrition(request):
    if request.method == 'POST':
        carbs = request.POST.get('carbs')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')

        # Update your Nutrition model instance
        # Example:
        nutrition_instance = Nutrition.objects.first()  # You might want to query your specific instance
        nutrition_instance.carbs = carbs
        nutrition_instance.protein = protein
        nutrition_instance.fat = fat
        nutrition_instance.save()

    return render(request, 'template.html', context)