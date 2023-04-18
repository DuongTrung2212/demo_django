from django.contrib import admin
from django.utils.html import mark_safe,format_html
from .models import *
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    class Media:
        css={
            'all':["/static/..."]
        }
        js=["/static/..."]
    list_display=["id","subject","created_date","active","course"]#hiện thị cột trên admin web
    search_fields=["subject","active","course__subject"]#Tìm kiếm trong các trường chỉ định(course_subject: tìm cả subject trong bảng courser)
    list_filter=["subject","course__subject"]#Lọc theo các trườNg chỉ định
    readonly_fields=["img"]
    def img(self, lesson):
        return format_html( "<img src='/static/{img_url}' width='120px' alt='{alt}'/> ".format(img_url=lesson.image.name,alt=lesson.subject))
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)

