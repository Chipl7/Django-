from django import template
import witcher.views as views

register = template.Library()


@register.simple_tag(name = 'get_character')
def get_categories():
    return views.character_db


@register.inclusion_tag('witcher/list_categories.html')
def show_categories(character_selected=0):
    character = views.character_db
    return {'character': character, 'character_selected': character_selected}