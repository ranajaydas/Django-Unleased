from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .forms import UserRegisterForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    exclude = ('slug',)


class CustomUserAdmin(UserAdmin):
    # List view
    list_display = ('username', 'get_name', 'email', 'date_joined', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'get_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'profile__joined')
    ordering = ('email',)
    search_fields = ('email',)

    def get_name(self, user):
        return user.profile.name
    get_name.short_description = 'name'
    get_name.admin_order_field = 'profile__name'

    # Database calls optimization
    list_select_related = ('profile',)

    # Form to view users
    fieldsets = ((None, {'classes': ('wide',),
                         'fields': ('email', 'username',)}),
                 ('Permissions', {'classes': ('collapse',),
                                  'fields': ('is_active',
                                             'is_staff',
                                             'is_superuser',
                                             'groups',
                                             'user_permissions')}),
                 ('Important dates', {'classes': ('collapse',),
                                      'fields': ('last_login',)}),
                 )
    filter_horizontal = ('groups', 'user_permissions',)

    # Form to add users
    add_form = UserRegisterForm
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('username',
                                        'email',
                                        'password1',
                                        'password2')}),
                     )

    # Integrate Profiles with User
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return tuple()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
