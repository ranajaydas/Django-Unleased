from django.contrib import admin
from django.db.models import Count
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # List view
    list_display = ('title', 'pub_date', 'author', 'tag_count')
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date',)
    search_fields = ('title', 'text')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(tag_number=Count('tags'))

    def tag_count(self, post):
        return post.tag_number

    tag_count.short_description = 'Number of Tags'
    tag_count.admin_order_field = 'tag_number'

    # Form view
    fieldsets = ((None, {'fields': ('title', 'slug', 'author', 'text',)}),
                 ('Related', {'fields': ('tags', 'startups')}),)
    filter_horizontal = ('tags', 'startups',)
    prepopulated_fields = {'slug': ('title',)}

