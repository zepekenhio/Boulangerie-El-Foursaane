from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('add_employee_cat', views.AddEmployeeCategory, name='add-personelCat'),
    path('add_rawmaterial', views.AddRawMaterial, name='add-rawmaterial'),
    path('add_employee', views.AddEmployee, name='add-employee'),
    path('add_purchase', views.AddPurchaise, name='add-purchase'),
    path('add_product', views.AddProduct, name='add-product'),
    path('add_period', views.AddPeriod, name='add-period'),
    path('add_production', views.AddProduction, name='add-production'),
    path('add_productioncost', views.AddProductionCost, name='add-productioncost'),
    
    path('employee_list', views.EmployeeList, name='employee-list'),
    path('rawmaterial_list', views.RawMaterialList, name='rawmaterial-list'),
    path('purchase_list', views.PurchaseList, name='purchase-list'),
    path('product_list', views.ProductList, name='product-list'),
    path('production_list', views.ProductionList, name='production-list'),
    
    path('production_detail/<production_id>', views.ProductionDetail, name='production-detail'),
    
]