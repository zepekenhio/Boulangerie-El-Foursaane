from django.db import models

class EmployeeCategory(models.Model):
    title = models.CharField(max_length=150, unique=True)
    role = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.title
    
class Employee(models.Model):
    category = models.ForeignKey(EmployeeCategory, blank=False, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    resgistration_id = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150, blank=False, null=False)
    contact = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.first_name

class Supplyer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)
    contact = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Raw_Material(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name
   
class Purchase(models.Model):
    material = models.ForeignKey(Raw_Material, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, blank=False, null=False)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.product
    
class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name

class Period(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Production(models.Model):
    product = models.ForeignKey(Product, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateField('production_date', )
    period = models.ForeignKey(Period, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, blank=False, null=False)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.product

class ProductionCost(models.Model):
    raw_material = models.ForeignKey(Raw_Material, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1500, blank=False, null=False)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.raw_material