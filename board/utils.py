from django.db.models import Count

from board.models import *


class DataMixin:
    paginate_by = 5

    def get_user_contex(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('post'))
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context