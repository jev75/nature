from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'avatar_tag', 'user_email', 'user_is_active', 'user_is_staff')
    list_display_links = ('user',)
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__is_active', 'user__is_staff')
    fields = ('user', 'avatar_tag', 'avatar')
    readonly_fields = ('user', 'avatar_tag')

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.avatar.url))
        return '-'
    avatar_tag.short_description = 'Avatar'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

    def user_is_active(self, obj):
        return obj.user.is_active
    user_is_active.short_description = 'Is Active'
    user_is_active.boolean = True

    def user_is_staff(self, obj):
        return obj.user.is_staff
    user_is_staff.short_description = 'Is Staff'
    user_is_staff.boolean = True
