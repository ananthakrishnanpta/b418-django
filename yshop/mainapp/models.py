from django.db import models
# this file decides the schema design of db
# any changes to this file must be followed by the command
# `python manage.py makemigrations` -> to generate required DDL statements to affect the DB
# and then
# `python manage.py migrate` -> to use these statements to migrate changes to the DB

# Create your models here.
class Product(models.Model):
    # providing the object attributes for product 
    name = models.CharField(max_length = 200) # this forms a varchar col in the `Product` table of name `name`
    price = models.PositiveIntegerField() # unsigned integer
    desc = models.TextField() # becomes long or medium text


    def __str__(self):
        return self.name
