from django.db import models

# Create your models here.
class Query_table(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()
    is_admission=models.BooleanField("is_admission",default=False)
    is_canteen=models.BooleanField("is_canteen",default=False)
    is_faculty=models.BooleanField("is_faculty",default=False)
    is_infra=models.BooleanField("is_infra",default=False)
    satisfied=models.IntegerField("satisfied",default=0)
    unsatisfied=models.IntegerField("unsat",default=0)
    viewed=models.IntegerField("viewed",default=0)

class admission(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()

class canteen(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()

# class statisticTable(models.Model):
#     questionID=models.IntegerField(11)
#     satisfied=models.IntegerField(11)
#     unsatisfied=models.IntegerField(11)
#     viewed=models.IntegerField(11)
