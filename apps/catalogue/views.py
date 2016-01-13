from django.http.response import JsonResponse
from django.views.generic import DetailView, ListView
from .models import Product, Category
from django.db.models import F


class ProductList(ListView):
    model = Product
    paginate_by = 15
    context_object_name = 'products'

    def get_template_names(self):
        if 'category' in self.kwargs:
            return ['catalogue/product_list.html']
        else:
            return ['catalogue/all_products.html']

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['popular_items'] = Product.objects.most_popular()[:4]
        context['recent_items'] = Product.objects.added_recently()[:4]
        return context

    def get_queryset(self):
        filters = {}
        if 'q' in self.request.GET:
            filters['name__icontains'] = self.request.GET['q']
        return self.model.objects.filter(**filters)


class CategoryList(ProductList):

    def get_template_names(self):
        return ['catalogue/product_list.html']

    def get_queryset(self):
        queryset = super(CategoryList, self).get_queryset()
        filters = {}
        if 'category' in self.kwargs:
            category = Category.objects.filter(slug=self.kwargs['category']).get()
            descendants = list(category.get_descendants().all())
            filters['categories__in'] = descendants + [category, ]

        return queryset.filter(**filters)


def set_visit(request, category, slug):
    product = Product.objects.get(slug=slug)
    product.visits = F('visits') + 1
    product.save()
    return JsonResponse({'status': True})


class ProductDetail(DetailView):

    model = Product
    context_object_name = 'product'

