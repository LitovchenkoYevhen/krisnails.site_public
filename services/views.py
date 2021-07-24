from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from services.models import *
from services import form_for_message, information_about_master

from .utils import *


class Home(ListView):
    """Показ главной страницы. Мастер, список преимуществ, портфолио для главной страницы"""
    model = Visit
    template_name = 'services/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = information_about_master.get_master(context)
        context['advantages'] = Advantage.objects.all()
        context['portfolio'] = Visit.objects.filter(completed=True, is_published=True, show_on_main=True,
                                                    photo_after__contains='after').order_by('-id')
        return context


class Services(ListView):
    """Список услуг """
    model = Service
    template_name = 'services/service.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manicure'] = Service.objects.filter(header__contains='Маникюр', is_published=True)
        context['covering'] = Service.objects.filter(header__contains='Покрытие', is_published=True)
        return context


class Portfolio(ListView):
    """Портфолио с templatetag 'get_portfolio'  """
    model = Visit
    template_name = 'services/portfolio.html'


def show_contacts_and_send_message(request):
    form = form_for_message.make_form(request)
    return render(request, f'services/contact.html', {'form': form})


def send_message(request):
    form = form_for_message.make_form(request)
    return render(request, f'services/contact_form.html', {'form': form})



class About(ListView):
    """Информация о мастере. Страница "Обо мне" """
    model = Master
    template_name = 'services/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = information_about_master.get_master(context)
        context['projects_done'] = Visit.objects.all().aggregate(cnt=Count('completed'))['cnt']
        context['clients'] = Client.objects.aggregate(cnt=Count('name'))['cnt']
        context['quotes'] = Quote.objects.all()
        return context


class Blog(ListView):
    model = Post
    template_name = 'services/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class ShowPost(DetailView):
    model = Post
    template_name = 'services/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'].views = F('views') + 1
        context['post'].save()
        context['post'] = Post.objects.get(slug=self.kwargs['slug'])
        return context



