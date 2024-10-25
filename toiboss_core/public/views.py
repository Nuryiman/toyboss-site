from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from public.models import Publication


class PublicationsView(TemplateView):
    template_name = 'publications.html'

    def get_context_data(self, **kwargs):
        publications = Publication.objects.all()
        paginator = Paginator(publications, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'publications': page_obj.object_list,
            'page_obj': page_obj,
            'paginator': paginator,
        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publications-inner.html'
