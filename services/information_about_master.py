from django.core.exceptions import ObjectDoesNotExist

from services.models import Master


def get_master(context):
    try:
        context['master'] = Master.objects.get(telephone__contains='0933398818')
    except ObjectDoesNotExist:
        pass
    return context
