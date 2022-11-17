from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
<<<<<<< HEAD
        return "Name: " + self.name + "," + \
               "Description: " + self.description 
=======
        return self  
>>>>>>> 503844a5246934b36e25e3addf59128248af2c63

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    
    CarMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    year = models.DateField()

    SEDAN = 'Sedan'
    WAGON = 'WAGON'
    SUV = 'SUV'

    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (WAGON, 'WAGON '),
        (SUV, 'SUV')
    ]
    Type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )

    def __str__(self):
<<<<<<< HEAD
        return "Name: " + self.name + "," + \
               "Car Make Name: " + self.CarMake.name + \
               "Car Make Description: " + self.CarMake.description + \
               "Type: " + self.Type + \
               "Year: " + str(self.year.year) + \
               "Dealer ID: " + str(self.dealer_id) 
=======
        return self  
>>>>>>> 503844a5246934b36e25e3addf59128248af2c63

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
