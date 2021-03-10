from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .models import Link
from .forms import LinkForm, LinkModelForm
from .shortener_repositories import create_short_link_with_save_in_db, copied_text


def main_view(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            full_link = form.data.get('full_link')
            designed_link = form.data.get('designed_link')
            if designed_link:
                full_short_link = create_short_link_with_save_in_db(request, full_link,  designed_link)
            else:
                full_short_link = create_short_link_with_save_in_db(request, full_link)
            copied_text(full_short_link)
            context = {'short_link': full_short_link}
            return JsonResponse(context, status=200)
    else:
        form = LinkForm()
        context = {'form': form}
    return render(request, 'shortener/main.html', context)


def redirect_full_link(request, short_link):
    full_link = Link.objects.get(Q(short_link=short_link) | Q(designed_link=short_link))
    full_link.count_use += 1
    full_link.save()
    return redirect(full_link.full_link)


def link_delete_view(request, pk):
    if request.method == 'POST':
        link = Link.objects.get(id=pk)
        link.delete()
    return redirect('main')


class DesignedLinksListView(ListView):
    model = Link
    template_name = 'shortener/designed_links.html'

    def get_queryset(self):
        data = Link.objects.filter(short_link='')
        # data = Link.objects.raw('SELECT * FROM shortener_link WHERE designed_link is not NULL')
        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        data = self.get_queryset()
        domain_name = self.request.headers['Host']
        context = {'links': data, 'domain_name': domain_name}
        return context


class StandardLinksListView(ListView):
    model = Link
    template_name = 'shortener/standard_links.html'

    def get_queryset(self):
        data = Link.objects.filter(designed_link='')
        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        data = self.get_queryset()
        domain_name = self.request.headers['Host']
        context = {'links': data, 'domain_name': domain_name}
        return context


class LinkUpdateView(UpdateView):
    model = Link
    context_object_name = 'link'
    form_class = LinkModelForm
    template_name = 'shortener/update.html'
    success_url = reverse_lazy('main')
