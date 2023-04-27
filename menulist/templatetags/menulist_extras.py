from django import template
from django.shortcuts import get_object_or_404
from menulist.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menulist/menu_tree.html', takes_context=True)
def draw_menu(context, name):
    menu = MenuItem.objects.get(name=name)
    new_context = {'menu_item': menu,
                   'title': name}
    new_path = context['request'].path
    try:
        active_menu_item = MenuItem.objects.get(explicit_url=new_path)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = active_menu_item.get_parent_ids() + [active_menu_item.id]
        new_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids
    return new_context


@register.inclusion_tag('menulist/menu_tree.html', takes_context=True)
def draw_menu_item_children(context, id):
    menu_item = MenuItem.objects.get(pk=id)
    new_context = {'menu_item': menu_item,
                   'title': menu_item.name}
    if 'unwrapped_menu_item_ids' in context:
        new_context['unwrapped_menu_item_ids'] = context['unwrapped_menu_item_ids']
    return new_context
