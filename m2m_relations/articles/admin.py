from django.contrib import admin

from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('true_false'):
                count += 1
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
