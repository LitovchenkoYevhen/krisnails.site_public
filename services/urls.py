from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from django.views.decorators.cache import cache_page

from services import views

app_name = 'services'
urlpatterns = [
    path('', cache_page(60 * 1)(views.Home.as_view()), name='home'),
    path('service/', cache_page(60 * 1)(views.Services.as_view()), name='service'),
    path('portfolio/', cache_page(60 * 1)(views.Portfolio.as_view()), name='portfolio'),
    path('contact/', views.send_message, name='contact'),
    path('about/', cache_page(60 * 1)(views.About.as_view()), name='about'),
    path('blog/', cache_page(60 * 1)(views.Blog.as_view()), name='blog'),
    path('blog/<str:slug>', cache_page(60 * 1)(views.ShowPost.as_view()), name='show_post'),
    path('contact_form/', views.send_message, name='contact_form'),
]
