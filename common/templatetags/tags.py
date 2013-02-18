from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search("^/landing/%s" % pattern, request.path):
        return 'active'
    return 'inactive'
