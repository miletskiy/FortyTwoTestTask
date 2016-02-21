
from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def edit_link(anyobject):
    object_id = anyobject.id

    reverse_path = 'admin:{}_{}_change'.format(anyobject._meta.app_label,
                                            anyobject._meta.model_name)

    return reverse(reverse_path, args=(object_id,))
