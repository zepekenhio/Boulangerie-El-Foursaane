from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EmployeeCategory, Employee, Raw_Material, Purchase, Product, Period, Production, ProductionCost
from .forms import EmployeeCategoryForm, EmployeeForm, RawMaterialForm, PurchaseForm, PeriodForm, ProductForm, ProductionForm, ProductionCostForm
from django.http import HttpResponse, HttpResponseRedirect, response, Http404
from django.db.models import Sum

#@login_required
def accueil(request):
    return render(request, 'boulanger/accueil.html', {})

def AddEmployeeCategory(request):
    submitted = False
    if request.method == "POST":
        form = EmployeeCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_employee')
    else:
        form = EmployeeCategoryForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_personelCategory.html', {
        'form': form,
        'submitted': submitted,
    })

def AddEmployee(request):
    submitted = False
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('employee_list')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_employee.html', {
        'form': form,
        'submitted': submitted,
    })
    
def EmployeeList(request):
    employees = Employee.objects.all().order_by('first_name')
    return render(request, 'boulanger/employee_liste.html', {
        'employees': employees,
    })

def RawMaterialList(request):
    rawmaterials = Raw_Material.objects.all().order_by('name')
    return render(request, 'boulanger/rawmaterial_liste.html', {
        'rawmaterials': rawmaterials,
    })

def PurchaseList(request):
    purchases = Purchase.objects.all().order_by('material')
    return render(request, 'boulanger/purchase_list.html', {
        'purchases': purchases,
    })

def ProductList(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'boulanger/product_list.html', {
        'products': products,
    })

def ProductionList(request):
    productions = Production.objects.all().order_by('date')
    return render(request, 'boulanger/production_list.html', {
        'productions': productions,
    })
    
def AddRawMaterial(request):
    submitted = False
    if request.method == "POST":
        form = RawMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('rawmaterial_list')
    else:
        form = RawMaterialForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_rawmaterial.html', {
        'form': form,
        'submitted': submitted,
    })

def AddPurchaise(request):
    submitted = False
    if request.method == "POST":
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('purchase_list')
    else:
        form = PurchaseForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_purchase.html', {
        'form': form,
        'submitted': submitted,
    })

def AddProduct(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('product_list')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_product.html', {
        'form': form,
        'submitted': submitted,
    })
    
def AddPeriod(request):
    submitted = False
    if request.method == "POST":
        form = PeriodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_period')
    else:
        form = PeriodForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_period.html', {
        'form': form,
        'submitted': submitted,
    })

def AddProduction(request):
    submitted = False
    if request.method == "POST":
        form = ProductionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('production_list')
    else:
        form = ProductionForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_production.html', {
        'form': form,
        'submitted': submitted,
    })

def AddProductionCost(request):
    submitted = False
    if request.method == "POST":
        form = ProductionCostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('rawmaterial_list')
    else:
        form = ProductionCostForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'boulanger/add_productioncost.html', {
        'form': form,
        'submitted': submitted,
    })

def ProductionDetail(request, production_id):
    production = Production.objects.get(pk=production_id)
    costs = ProductionCost.objects.filter(production_id=production_id)
    #related_costs = ProductionCost.objects.filter(production_id=production_id).annotate(cost_counter=Sum('amount'))
    # for cost in costs:
    #     pcost = cost.amount.sum                
    #pcost = costs.objects.aggregate(Sum('amount'))
    return render(request, 'boulanger/production_detail.html', {
        'production': production,
        'costs': costs,
        # 'pcost': pcost,
    })