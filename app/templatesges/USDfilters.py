from django import template

register=template.Library()

@register.filter('swapping')
def Swap(data):
    return data.swapcase()