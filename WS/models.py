from django.db import models


class Bikes(models.Model):
    bike_types = [
        (1, "Sport"),
        (2, "Mountain"),
        (3, "Town"),
        (4, "Light"),
        
    ]

    # count = [
    #     (1, "-"),
    #     (2, "-"),
    #     (3, "-"),
    # ]

    bike_type = models.IntegerField(choices=bike_types, default=4)
    
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=1024)
    price = models.IntegerField(max_length=6, default=None)
    is_there_any = models.BooleanField(default=False)
    bike_amount = models.IntegerField()











# class Product_type(models.Model):
#     Ready_to_sell_Bikes = models.CharField(max_length=15)
#     Wheels = models.CharField(max_length=20)
#     Bike_gear = models.CharField(max_length=20)
#     Accessories = models.CharField(max_length=20)
    # x = models.CharField()
    # x = models.CharField()


# class Bike_Type(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField(max_length=1024)
#     Mountain_bikes = models.CharField(50)
#     City_bikes = models.CharField(50)
#     Light_bikes = models.CharField(50)
#     Sport_bikes = models.CharField(50)
#     Price = models.IntegerField(10)
#     x = models.CharField()
    

    
# class Wheel_type(models.Model):
#     Mountain = models.CharField(50)
#     City = models.CharField(50)
#     Light = models.CharField(50)
#     Sport = models.CharField(50)
    # x = models.CharField()
    # x = models.CharField()



    
# class Wheel_size(models.Model):
#     twenty_d = models.IntegerField(5)
#     twenty_four_d = models.IntegerField(5)
#     twenty_six_d = models.IntegerField(5)
#     twenty_eight_d = models.IntegerField(5)
#     twenty_nine_d = models.IntegerField(5)

    
