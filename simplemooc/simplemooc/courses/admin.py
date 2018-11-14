from django.contrib import admin

from .models import Course, Enrollment, Announcement, Comment


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class EnrrolmentAdmin(admin.ModelAdmin):

    list_display = ['user', 'course', 'status', 'created_at', 'updated_at']
    search_fields = ['user', 'course']

class AnnouncementAdmin(admin.ModelAdmin):

    list_display = ['course', 'title', 'content', 'created_at', 'updated_at']
    search_fields = ['course', 'title']

class CommentAdmin(admin.ModelAdmin):

    list_display = ['announcement', 'user', 'comment', 'created_at', 'updated_at']
    search_fields = ['announcement', 'user']


admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrrolmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Comment, CommentAdmin)
