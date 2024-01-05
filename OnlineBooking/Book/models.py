from django.db import models

class Customer(models.Model):
    customerid = models.IntegerField()
    customername = models.CharField(max_length=25, default='')
    gender = models.CharField(max_length=6, default='MALE')
    areatype = models.CharField(max_length=5)
    customerphoto = models.ImageField(upload_to='photo/')

    class Meta:
        db_table = 'reading_customer'
