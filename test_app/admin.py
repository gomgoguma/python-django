from django.contrib import admin
from .models import Question
from .models import Answer

# admin.site.register(Question)
admin.site.register(Answer)


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
