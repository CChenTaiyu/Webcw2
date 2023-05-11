from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    deposit = models.FloatField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class payRecord(models.Model):
    time = models.DateTimeField()
    recipient = models.CharField(max_length=45)
    amount = models.IntegerField()
    money = models.FloatField()
    secret_key = models.CharField(max_length=45)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, db_column='userId', null=True)
    airline_order = models.CharField(max_length=45)
    state = models.BooleanField()
