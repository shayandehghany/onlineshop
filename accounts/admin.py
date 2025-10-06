from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session
from django.utils import timezone

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


def user_logged_in(user):
    """Check if user has an active session"""
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    for session in sessions:
        data = session.get_decoded()
        if str(user.id) == str(data.get('_auth_user_id')):
            return True
    return False


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # ستون‌های نمایشی
    list_display = ('email', 'username', 'is_logged_in')

    def is_logged_in(self, obj):
        return user_logged_in(obj)

    is_logged_in.boolean = True  # نمایش تیک سبز/قرمز
    is_logged_in.short_description = "Active Session"
