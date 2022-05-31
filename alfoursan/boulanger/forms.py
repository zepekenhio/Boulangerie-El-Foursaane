from django import forms
from django.forms import ModelForm
from .models import EmployeeCategory, Employee, Raw_Material, Purchase, Product, Period, Production, ProductionCost


class EmployeeCategoryForm(ModelForm):
    class Meta:
        model = EmployeeCategory
        fields= ('title', 'role' )

        labels = {
            'title': '',  
            'role': '',
            
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre',}),  
            'role': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Rôle',}),
        }
        
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields= ('category', 'first_name', 'last_name', 'registration_id', 'address', 'contact' )

        labels = {
            'category': '',  
            'first_name': '',
            'last_name': '',
            'registration_id': '',
            'address': '',
            'contact': '',            
        }

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cateorie',}),  
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prènom',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),
            'registration_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID',}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse',}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact',}),
        }    
        
class RawMaterialForm(ModelForm):
    class Meta:
        model = Raw_Material
        fields= ('name', 'description', )

        labels = {
            'name': '',  
            'description': '',         
        }

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields= ('material', 'description', 'quantity', 'unit_price' )

        labels = {
            'material': '',  
            'description': '',
            'quantity': '',  
            'unit_price': '',       
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields= ('name', 'description', )

        labels = {
            'name': '',  
            'description': '',         
        }

class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields= ('title', 'description' )

        labels = {
            'title': '',  
            'description': '',
            
        }

class ProductionForm(ModelForm):
    class Meta:
        model = Production
        fields= ('date', 'period', 'product', 'description', 'quantity'  )

        labels = {
             'date': '',
            'period': '',
            'product': '', 
            'description': '',
            'quantity': '',         
        }
        
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date',}),  
            'period': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Pèriode',}),
            'product': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Produit',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qunatité',}),
        } 

class ProductionCostForm(ModelForm):
    class Meta:
        model = ProductionCost
        fields= ('production_id', 'cost', 'description', 'quantity', 'unit_price',)

        labels = {
            'production_id': '',
            'cost': '',
            'description': '',
            'quantity': '', 
            'unit_price': '',
        }
        
        widgets = {
            'production_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ID Production',}),
            'cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coût',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qunatité',}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prix Uintaire',}),
        } 