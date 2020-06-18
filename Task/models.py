from django.db import models
# Create your models here.
class User_Details(models.Model):
    User_ID=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

    # class Meta:
    #     db_table = "User_Details"
