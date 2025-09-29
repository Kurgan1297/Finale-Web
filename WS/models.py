from django.db import models


class User():
    # ???
    pass



class Product_type(models.Model):
    Ready_to_sell_Bikes = models.CharField(max_length=15)
    Wheels = models.CharField(max_length=20)
    Bike_gear = models.CharField(max_length=20)
    Accessories = models.CharField(max_length=20)
    x = models.CharField()
    x = models.CharField()



class Bike_Type(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=1024)
    Mountain_bikes = models.CharField()
    City_bikes = models.CharField()
    Light_bikes = models.CharField()
    Sport_bikes = models.CharField()
    x = models.CharField()
    x = models.CharField()
    


# class Bike_Price(self):
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()


    
class Wheel_type(models.Model):
    Mountain = models.CharField()
    City = models.CharField()
    Light = models.CharField()
    Sport = models.CharField()
    x = models.CharField()
    x = models.CharField()


    
# class Wheel_price(self):
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()
#     x = models.CharField()


    
class Wheel_size(models.Model):
    twenty_d = models.IntegerField()
    twenty_four_d = models.IntegerField()
    twenty_six_d = models.IntegerField()
    twenty_eight_d = models.IntegerField()
    twenty_nine_d = models.IntegerField()

    
class (models.Model):
    x = models.CharField(2)