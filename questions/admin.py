from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Question, Choice, Module

class ChoiceInline(TabularInline):
    model = Choice
    extra = 1
    

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['module', 'text', 'course', 'year', 'answered']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text', 'correct']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Module)
admin.site.register(Choice, ChoiceAdmin)