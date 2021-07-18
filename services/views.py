from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from services.models import *


from .forms import ContactForm
from .utils import *


class Home(ListView):
    model = Visit
    template_name = 'services/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master'] = Master.objects.get(pk=1)
        context['advantages'] = Advantage.objects.all()
        context['portfolio'] = Visit.objects.filter(completed=True, is_published=True, show_on_main=True, photo_after__contains='jpg')
        return context


class Services(ListView):
    model = Service
    template_name = 'services/service.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manicure'] = Service.objects.filter(header__contains='Маникюр', is_published=True)
        context['covering'] = Service.objects.filter(header__contains='Покрытие', is_published=True)
        return context


class Portfolio(ListView):
    model = Visit
    template_name = 'services/portfolio.html'



def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['subject'] = form.cleaned_data['telephone'] + ' | ' + form.cleaned_data['name'] + ' | ' + form.cleaned_data['email']
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'krisnails@ukr.net', ('litovchenkoyevhen@gmail.com',))
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('services:contact')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка ввода')
    else:
        form = ContactForm()
    path = request.path[1:-1]
    return render(request, f'services/{path}.html', {'form': form})


class About(ListView):
    model = Master
    template_name = 'services/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master'] = Master.objects.get(telephone__contains='0933398818')
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


# def show_post(request, slug):
#     post = Post.objects.get(slug=slug)
#     post.views = F('views') + 1
#     post.save()
#     return render(request, 'services/show_post.html', {'post': post})
