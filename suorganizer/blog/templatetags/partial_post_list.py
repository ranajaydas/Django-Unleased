from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag('blog/includes/partial_post_list.html', takes_context=True)
def format_post_list(context, detail_object, *args, **kwargs):
    request = context.get('request')
    post_list = detail_object.blog_posts.all()
    opposite = kwargs.get('opposite')
    perm_button = kwargs.get('perm_button')

    if not opposite:
        section_attr = ''
    elif opposite or perm_button:
        section_attr = mark_safe('class="meta one-third column"')
    else:
        section_attr = mark_safe('class="meta offset-by-two two-thirds column"')

    return {
        'post_list': post_list,
        'section_attr': section_attr,
    }
