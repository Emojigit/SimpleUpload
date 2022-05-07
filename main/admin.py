from django.contrib import admin
from django import forms
from main.models import Text

# Register your models here.

# https://stackoverflow.com/questions/6821161/django-admin-return-custom-error-message-during-model-saving#6821421
class TextAdminForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'

    def clean(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        location = cleaned_data.get('location')
        if location.__contains__("/"):
            raise forms.ValidationError("Hmm... DO NOT INCLUDE SLASHES IN LOCATION!")
        return super().clean(*args, **kwargs)
    def get_fields(self, request, obj=None):
        fields = ['location','content','MMIE']
        if request.user.is_superuser or (obj != None and obj.creator != None and request.user == obj.creator):
            fields.append('creator')
        return fields


class TextAdmin(admin.ModelAdmin):
    list_display = ('location','MMIE', 'creator')
    list_display_links = ('location', )
    save_as = True
    def save_model(self, request, obj, form, change):
        if not obj.creator:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

    # https://stackoverflow.com/questions/47182559/allow-user-modify-only-objects-created-by-this-user#47182678
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser: return True
        if obj is not None and obj.creator != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser: return True
        if obj is not None and obj.creator != request.user:
            return False
        return True

    form = TextAdminForm

admin.site.register(Text, TextAdmin)

admin.site.site_header = "SimpleUpload Management Panel"
admin.site.site_title = "SimpleUpload"
