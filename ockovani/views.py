from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from ockovani.models import Vakcina, Ockovani, Povolani

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html

    num_ockovani = Ockovani.objects.all().count()
    ockovani = Ockovani.objects.order_by('-id')
    vakciny = Vakcina.objects.order_by('id')

    context = {
        'num_ockovani': num_ockovani,
        'ockovani': ockovani,
        'vakciny': vakciny
    }

    return render(request, 'index.html', context=context)



def seznamvakcin(request):

    vakciny = Vakcina.objects.order_by('id')

    context = {
        'vakciny': vakciny
    }

    return render(request, 'seznam_vakcin.html', context=context)

# def seznam(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template index.html
#     return render(
#         request,
#         'seznam.html',
#     )

class OckovaniListView(ListView):
    model = Ockovani

    context_object_name = 'ockovani_list'   # your own name for the list as a template variable
    template_name = 'ockovany/list.html'  # Specify your own template name/location
    paginate_by = 6

    def get_queryset(self):
        if 'vakcina_nazev_firmy' in self.kwargs:
            return Ockovani.objects.filter(vakcina__nazev_firmy=self.kwargs['vakcina_nazev_firmy']).all() # Get 5 books containing the title war
        else:
            return Ockovani.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['num_ockovani'] = len(self.get_queryset())
        if 'vakcina_nazev_firmy' in self.kwargs:
            context['view_title'] = f"Vakcíny: {self.kwargs['vakcina_nazev_firmy']}"
            context['view_head'] = f"Vakcíny: {self.kwargs['vakcina_nazev_firmy']}"
        else:
            context['view_title'] = 'Očkovaní'
            context['view_head'] = 'Přehled očkovaných'
        return context


class OckovaniDetailView(DetailView):
    model = Ockovani

    context_object_name = 'osoba_detail'   # your own name for the list as a template variable
    template_name = 'ockovany/detail.html'  # Specify your own template name/location
