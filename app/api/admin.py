from django import forms
from django.contrib import admin

from api.models import APIToken


class APITokenAddForm(forms.ModelForm):
    raw_token = forms.CharField(
        label="Token",
        help_text="Enter the raw token string. It will be hashed — write it down, it cannot be retrieved later.",
    )

    class Meta:
        model = APIToken
        fields = ("name", "raw_token")


@admin.register(APIToken)
class APITokenAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    readonly_fields = ("key_hash", "created_at")

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs["form"] = APITokenAddForm
        return super().get_form(request, obj, **kwargs)

    def get_fields(self, request, obj=None):
        if obj is None:
            return ("name", "raw_token")
        return ("name", "key_hash", "created_at")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_token(form.cleaned_data["raw_token"])
        super().save_model(request, obj, form, change)
