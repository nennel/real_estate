from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Property

# Create your views here.
class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    ordering = ['price']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_properties'] = Property.objects.count()
        return context

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property_obj = self.get_object()

        context['breadcrumb'] = [
            {'name': 'Home', 'url': '/'},
            {'name': 'Property', 'url':'/'},
            {'name': property_obj.name, 'url': ''}
        ]
        return context



