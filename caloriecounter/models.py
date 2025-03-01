from django.db import models

# Create your models here.
class GoalChoices(models.Model):
    goal_choice =models.CharField(max_length=20)

    def __str__(self):
        return self.goal_choice


class ActivityChoices(models.Model):
    activity_choice =models.CharField(max_length=20)

    def __str__(self):
        return self.activity_choice


class Nutrition(models.Model):
    carbs = models.IntegerField(default=40)
    protein =models.IntegerField(default=30)
    fat =models.IntegerField(default=30)



# goal_choices = {

#     ('lose_weight', 'lose_weight'),
#     ('maintain', 'maintain_weight'),
#     ('build_muscle', 'build_muscle')

# }

# activity_choices = {

#     ('low', 'low'),
#     ('moderate', 'moderate'),
#     ('high', 'high'),
#     ('very_high', 'very_high'),
# }

class Profile(models.Model):
    your_goal = models.ForeignKey(GoalChoices, on_delete=models.CASCADE)
    start_weight= models.FloatField()
    goal_weight= models.FloatField()
    week_goal_to_lose_or_gain= models.IntegerField()
    calorie_goal= models.IntegerField()
    activity= models.ForeignKey(ActivityChoices, on_delete=models.CASCADE)
    nutrition_goal= models.ForeignKey(Nutrition, on_delete=models.CASCADE, default=1500)
    # carbs = models.IntegerField(max_length=20, default=40)
    # protein =models.IntegerField(max_length=20, default=30)
    # fat =models.IntegerField(max_length=20, default=30)
    # total =models.IntegerField(max_length=20, default=100)

    def __str__(self):
        return f"{self.your_goal} to {self.calorie_goal}"

class Recipes(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=250)
    image = models.URLField(max_length=2500)

class Groceries(models.Model):
    grocery_name = models.CharField(max_length=30)
    gram = models.IntegerField()
    calorie = models.IntegerField()

