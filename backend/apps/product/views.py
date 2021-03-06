from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
import json
# Create your views here.
from .models import SubCategory, Category, Product, BannerImage
from django.db.models import Q
from django_filters.views import FilterView
from .filters import ProductFilter


def get_subcategories(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banners = BannerImage.objects.all()
        if len(banners) > 6:
            banners = banners[:5]
        context['banners'] = banners
        print(context)
        return context


class ProductListView(FilterView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 6
    filterset_class = ProductFilter

    def get_queryset(self):
        print(self.kwargs)
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        if subcategory_slug:
            products = Product.objects.filter(is_active=True, subcategory__slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductSearchView(ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 10

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.filter(is_active=True)
        q = self.model.objects.filter(Q(name__icontains=search_text) | Q(description__icontains=search_text))
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return  context
