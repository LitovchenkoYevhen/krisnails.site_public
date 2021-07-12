from .models import Visit, Tag, Certificate, Advantage, Master


class MasterMixin:

    def get_master_context(self, **kwargs):
        context = kwargs
        context['master'] = Master.objects.all()
        context['advantages'] = Advantage.objects.all()
        return context


