from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
# Create your views here.
from django.views import View
class Input(View):
    def get(self,request):
        p_f=ProductForm()
        return render(request,'input.html',{"product_form":p_f})
class Insert(View):
    def post(self,request):
        data_product_form = ProductForm(request.POST)
        if data_product_form.is_valid():
            p1=Product(pid=data_product_form.cleaned_data['pid'],
                       pname=data_product_form.cleaned_data['pname'],
                       pcost=data_product_form.cleaned_data['pcost'],
                       pmfdt=data_product_form.cleaned_data['pmfdt'],
                       pexptdt=data_product_form.cleaned_data['pexptdt'])
            p1.save()
            return HttpResponse("data inserted successfully")