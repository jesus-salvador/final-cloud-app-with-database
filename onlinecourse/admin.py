from django.contrib import admin

from onlinecourse.models import Choice
from onlinecourse.models import Course
from onlinecourse.models import Instructor
from onlinecourse.models import Learner
from onlinecourse.models import Lesson
from onlinecourse.models import Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ['course']
    list_display = ('content',)


# Register your models here.
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
