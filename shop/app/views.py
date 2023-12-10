from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category_filter = self.request.GET.get('category')
        application_area_filter = self.request.GET.get('application_area')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        min_quantity = self.request.GET.get('min_quantity')
        rating_filter = self.request.GET.get('rating')

        queryset = Product.objects.all()

        if query:
            queryset = queryset.filter(Q(name__icontains=query))

        if category_filter:
            queryset = queryset.filter(category=category_filter)

        if application_area_filter:
            queryset = queryset.filter(application_area=application_area_filter)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if min_quantity:
            queryset = queryset.filter(quantity__gte=min_quantity)

        if rating_filter:
            queryset = queryset.filter(rating__gte=rating_filter)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
