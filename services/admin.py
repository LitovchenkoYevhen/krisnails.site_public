from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'design_date',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('design_date',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'rating', 'manufacturer')
    prepopulated_fields = {'slug': ('title',)}


class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'registration_date', 'activity')
    readonly_fields = ('registration_date',)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'visit_date', 'completed', 'is_published', 'show_on_main', 'visit_cancel_reason', 'get_photo')
    list_display_links = ('id', 'client', 'visit_date', 'visit_cancel_reason', 'get_photo')
    list_editable = ('is_published', 'show_on_main',)
    readonly_fields = ('get_photo',)
    save_as = True


    fieldsets = [
        ('Планирование визита', {'fields': ('client', 'visit_date')}),
        ('Дополнительная информация после визита', {'fields': ('info', 'designs', 'completed', 'visit_cancel_reason', 'photo_before', 'photo_after', 'get_photo')}),
        ('Портфолио', {'fields': ('is_published', 'show_on_main', 'tags',)})
    ]

    def get_photo(self, obj):
        if obj.photo_after:
            return mark_safe(f'<img src="{obj.photo_after.url}" width="150">')
        return 'Отсутствует фото'

    get_photo.short_description = 'Фото'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_published')
    list_editable = ('is_published',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', 'school')

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('speaker',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('pub_date',)



admin.site.register(Design, DesignAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialType, MaterialTypeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Master)
admin.site.register(Advantage)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Post, PostAdmin)


