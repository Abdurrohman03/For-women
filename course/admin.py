from django.contrib import admin
from course.models import Course, Comment, Lesson, LessonUser, LessonUserWatched


class LessonInline(admin.StackedInline):
    model = Lesson
    fk_name = "course_of_lesson"
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", 'author', 'price', 'language']
    list_display_links = ["id", "title"]
    readonly_fields = ['id', 'created_at']
    inlines = [LessonInline]
