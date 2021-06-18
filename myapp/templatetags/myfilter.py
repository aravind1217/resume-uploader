from django import template
register = template.Library()
@register.filter(name = 'remove_special')
def remove(value, arg):
    for char in arg:
        value = value.replace(char,'')
    return value
