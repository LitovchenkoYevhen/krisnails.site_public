from django.db import models
from django.db.models import F
from django.urls import reverse_lazy


class Design(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя дизайна')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    tags = models.ManyToManyField('Material', blank=True)
    photo = models.ImageField(upload_to='photo/designs/%Y/%m/%d', blank=True, verbose_name='Фото')
    design_date = models.DateField(auto_now=True, verbose_name='Дата добавления дизайна')

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайны ногтей'

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название материала')
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    type = models.ForeignKey('MaterialType', on_delete=models.SET_NULL, null=True)
    price = models.CharField(max_length=4, blank=True, verbose_name='Стоимость')
    rating = models.IntegerField(verbose_name='Качество материала', blank=True, default='0')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель', blank=True)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.title


class MaterialType(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип материала')

    class Meta:
        verbose_name = 'Тип материала'
        verbose_name_plural = 'Типы материалов'

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    telephone = models.CharField(max_length=10, blank=True, verbose_name='Номер телефона (без "+38")')
    description = models.TextField(verbose_name='Заметка о клиенте', blank=True)
    registration_date = models.DateField(auto_now=True, verbose_name='Дата регистрации клиента')
    activity = models.CharField(max_length=50, verbose_name='Род деятельности', blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Visit(models.Model):
    visit_date = models.DateField(db_index=True, verbose_name='Дата визита')
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    info = models.TextField(verbose_name='Заметка о визите', blank=True)
    designs = models.ManyToManyField('Design', blank=True, verbose_name='Дизайн')
    price = models.CharField(max_length=4, verbose_name='Стоимость работ', blank=True)
    completed = models.BooleanField(verbose_name='Состоялся ли визит')
    visit_cancel_reason = models.CharField(max_length=200, blank=True, verbose_name='Причина отмены визита')
    photo_before = models.ImageField(upload_to='photos/visits/before/%Y/%m/%d', blank=True, verbose_name='Фото до')
    photo_after = models.ImageField(upload_to='photos/visits/after/%Y/%m/%d', blank=True, verbose_name='Фото после')
    is_published = models.BooleanField(verbose_name='Показывать в портфолио', default=False)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Теги')
    show_on_main = models.BooleanField(default=False, verbose_name='Показывать на главной странице')

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'

    def __str__(self):
        return str(self.visit_date)

    # def get_absolute_url(self, pk):


class Service(models.Model):
    title = models.CharField(max_length=80, verbose_name='Наименование услуги')
    price = models.CharField(max_length=50, verbose_name='Цена')
    is_published = models.BooleanField(verbose_name='Показывать в прайсе услуг')
    header = models.CharField(max_length=50, verbose_name='Заголовок', blank=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=80, verbose_name='Имя тега')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200, verbose_name='Сертификат')
    data = models.CharField(max_length=80, blank=True, verbose_name='Когда выдан')
    school = models.CharField(max_length=80, blank=True, verbose_name='Школа маникюра')
    photo = models.ImageField(upload_to='photos/certificates', blank=True, verbose_name='Сертификат')
    master = models.ForeignKey('Master', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.title


class Master(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True)
    telephone = models.CharField(max_length=10, verbose_name='Номер телефона без "+38"', blank=True)
    photo = models.ImageField(upload_to='photos/masters', blank=True, verbose_name='Фото мастера')
    about = models.TextField(verbose_name='Информация о мастере', blank=True)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return self.name


class Advantage(models.Model):
    advantage = models.CharField(max_length=200, verbose_name='Преимущество')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.advantage


class Quote(models.Model):
    speaker = models.CharField(max_length=200, verbose_name='Кому принадлежит', default='')
    content = models.TextField(verbose_name='Цитата')

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.speaker

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    is_published = models.BooleanField(verbose_name='Опубликовано')
    slug = models.SlugField(verbose_name='URL', unique=True)
    photo = models.ImageField(upload_to='photos/blog', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('services:show_post', kwargs={'slug': self.slug})



