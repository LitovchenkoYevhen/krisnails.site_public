from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from django.views.decorators.cache import cache_page

from services import views

app_name = 'services'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('service/', views.Services.as_view(), name='service'),
    path('portfolio/', views.Portfolio.as_view(), name='portfolio'),
    path('contact/', views.show_contacts_and_send_message, name='contact'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('blog/<str:slug>', views.ShowPost.as_view(), name='show_post'),
    path('contact_form/', views.send_message, name='contact_form'),
]
