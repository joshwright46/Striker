from django.db import models
from apps.login.models import User

class FormManager(models.Manager):
    def form_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters!"
        if len(postData['city']) < 3:
            errors['city'] = "City should be at least 3 characters!"
        if postData['city'] != postData['city']:
            errors['city_blank'] = "City cannot be blank"
        if len(postData['address']) < 0:
            errors['address_blank'] = "Address cannot be blank"
        if len(postData['address']) < 5:
            errors['address_invalid'] = "Invalid Address"
        if postData['zipcode'] < 5:
            errors['zipcode_invalid'] = "Zipcode Invalid"
        if len(postData['state']) == 0:
            errors['state_blank'] = 'State must be selected'

        return errors


class Product(models.Model):
    title = models.CharField(max_length=140)
    colorway = models.CharField(max_length=140)
    size = models.IntegerField()
    user = models.ForeignKey(User, related_name="products",null=True)


class Order(models.Model):
    order_number = models.IntegerField()
    amount = models.IntegerField()
    user = models.ForeignKey(User, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shipping(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=40)
    user = models.OneToOneField(User, related_name="shipping_form")
    objects = FormManager()

    def __repr__(self):
        return f"<Shipping object: {self.first_name} {self.last_name} {self.address} {self.city} {self.state} {self.zipcode} >"

class Billing(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    zipcode = models.IntegerField()
    phone_number = models.IntegerField()
    state = models.CharField(max_length=40)
    user = models.OneToOneField(User, related_name="billing_form")
    objects = FormManager()

    def __repr__(self):
        return f"<Billing object: {self.first_name} {self.last_name} {self.address} {self.city} {self.state} {self.zipcode} {self.phone_number}>"

class Card(models.Model):
    card_number = models.IntegerField()
    card_date = models.IntegerField()
    card_cvv = models.IntegerField()
    user = models.ForeignKey(User, related_name="card",null=True)