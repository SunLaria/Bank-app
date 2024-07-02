from django import template
import datetime
from django.db.models import Q

register = template.Library()


@register.filter(name="transactions_type_filter")
def transactions_type_filter(queryset, filter_word):
    if filter_word == "transfer":
        return queryset.filter(Q(t_type="sent") | Q(t_type="received"))
    return queryset.filter(t_type=filter_word)


@register.filter(name="filter_income_expense")
def filter_income_expense(queryset, filter_word):
    current_month = datetime.datetime.now().date().replace(day=1)
    if filter_word == "income":
        return sum([i.amount for i in queryset.filter(
            Q(t_type="deposit") | Q(t_type="received"),
            date__gte=current_month
        )])
    if filter_word == "expense":
        return sum([i.amount for i in queryset.filter(
            Q(t_type="withdraw") | Q(t_type="sent"),
            date__gte=current_month
        )])
