from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Product
from .forms import StockForm
# Create your views here.

def add_stock(request):
    if request.method == "GET":
        v = {
            'quantity': 100,
            'cost_price': 3500,
            'selling_price': 4000
        }
        form = StockForm(v)
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            drug = form.cleaned_data.get('checkbox')
            for d in drug:
                p = Product.objects.filter(name=d).first()
                if p:
                    p.quantity += form.cleaned_data.get('quantity')
                    p.cost_price = form.cleaned_data.get('cost_price')
                    p.selling_price = form.cleaned_data.get('selling_price')
                    print(p.quantity)
                    p.save()
            messages.info(request, "Stocks have been successfully added to inventory!")
            return redirect(reverse('stocks:stocks'))
    return render(request, 'add-stocks.html', {"form":form})

class HomeView(TemplateView):
    template_name = "home.html"

class OrderStock(TemplateView):
    template_name = "order-stocks.html"

    def post(self, request):
        messages.info(request, "Your order have been submitted successfully!")
        return redirect(reverse('stocks:order'))

class AddStocks(CreateView):
    template_name = "add-stocks.html"
    model = Product
    success_url = '/add-stocks/'
    fields = ['quantity', 'cost_price', 'selling_price']

    def post(self, request, kwargs):
        self.pk = kwargs.get('pk')
        return super().post(request, kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.quantity += Product.objects.get(self.pk_url_kwarg).first().quantity
        return super().form_valid(form)

class StockView(ListView):
    template_name = "stocks.html"
    model = Product