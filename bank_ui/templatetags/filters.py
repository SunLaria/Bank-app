from django import template
from django.db.models import Q

register = template.Library()


@register.filter(name="transactions_filter")
def transactions_filter(queryset, filter_word):
    if filter_word == "transfer":
        return queryset.filter(Q(t_type="sent") | Q(t_type="received"))
    return queryset.filter(t_type=filter_word)
