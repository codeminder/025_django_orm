from django import template
from django_orm_samples.models import *

register = template.Library()

@register.simple_tag(name="getbudg")
def get_budgets():
    return Budget.objects.all()