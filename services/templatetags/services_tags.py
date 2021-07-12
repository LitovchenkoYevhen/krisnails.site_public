from django import template
from services.models import Visit, Tag, Certificate

register = template.Library()

@register.inclusion_tag('services/education_table.html')
def get_education():
    certificates = Certificate.objects.all()
    return {'certificates': certificates}

@register.inclusion_tag('services/portfolio_table.html')
def get_portfolio():
    visit_list = Visit.objects.filter(completed=True, is_published=True, photo_after__contains='jpg')
    tags = Tag.objects.all()
    return {'visit_list': visit_list, 'tags': tags}
